import discord
import asyncio
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import logging
import shutil
import sys

# Suppress discord.py logging below WARNING level
logging.basicConfig(level=logging.WARNING)
logging.disable(logging.CRITICAL)

with open('settings.json', 'r') as f:
    settings = json.load(f)

file_path = os.path.abspath(settings['FILE_PATH'])    

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_content = None

# ASCII art for "Knedyz"
KNEDYZ_ASCII = r"""
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░  
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓██▓▒░    
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓██▓▒░      
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓████████▓▒░ 
                                                                                
                                                                                                                          
"""

RED = '\033[91m'
RESET = '\033[0m'

def clear_terminal():
    # Clear terminal for Windows and Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text):
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    for line in text.splitlines():
        print(line.center(terminal_width))

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
            print(f"You have completed a haul at: [{datetime.datetime.now()}]")
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
    clear_terminal()
    print_centered(KNEDYZ_ASCII)
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    notification_text = "DISCORD NOTIFICATION BOT \n\n\n"
    print(notification_text.center(terminal_width).replace(notification_text, f"{RED}{notification_text}{RESET}"))
    print("Everything's ready, awaiting your haul updates!")
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
