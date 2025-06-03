import discord
import asyncio
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json

with open('settings.json', 'r') as f:
    settings = json.load(f)

file_path = os.path.abspath(settings['FILE_PATH'])    

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_content = None


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.last_trigger_time = None
        self.debounceSec = 1.0 
        
    def on_modified(self, event):
        if os.path.abspath(event.src_path) != file_path:
            return

        now = datetime.datetime.now().timestamp()
        if self.last_trigger_time is None or (now - self.last_trigger_time) > self.debounceSec:
            self.last_trigger_time = now
            print(f"[{datetime.datetime.now()}] Detected file change: {event.src_path}")
            self.loop.create_task(post_file_if_changed())
        else:
            print(f"[{datetime.datetime.now()}] Ignored duplicate event.")


async def post_file_if_changed():
    global settings
    global file_path
    global last_content
    await client.wait_until_ready()
    channel = client.get_channel(settings['CHANNEL_ID'])

    try:
        with open(os.path.abspath(file_path), 'r', encoding='utf-8') as file:
            content = file.read().strip()

        if content and content != last_content:
            embed = discord.Embed(
                title="Current Haul:",
                description=content,
                color=discord.Color.green(),
                timestamp=datetime.datetime.now(datetime.UTC)
            )
            await channel.send(embed=embed)
            last_content = content
    except Exception as e:
        print(f"Error reading or sending file: {e}")


@client.event
async def on_ready():
    print(f'Bot is now running.')
    loop = asyncio.get_event_loop()
    event_handler = FileChangeHandler(loop)

    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(file_path), recursive=False)
    observer.start()


    # Keep alive
    while not client.is_closed():
        await asyncio.sleep(1)


def main():
    client.run(settings['TOKEN'])


if __name__ == "__main__":
    main()
