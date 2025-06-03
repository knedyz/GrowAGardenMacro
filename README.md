# Grow a Garden Macro
Game: https://www.roblox.com/games/126884695634066/Grow-a-Garden

This is a small project I made because I am very bored. It works for me, idk if it'll work for you too but better to try. <br/>
_If you want to change the script to fit your own needs, feel free to do so. But if you were to re-publish it, please credit. Thank._

Requires you to have:
- Automatic Mouse and Keyboard application 
- Task Scheduler
- Latest Python version
- Discord Bot Token (https://discord.com/developers)
- **Very Caveman knowledge**
- 1920x1080 screen resolution
- Electricity money
- A SHIT TON OF RECALL WRENCH

## What it currently gathers
**Seeds**
- Bamboo
- Mango
- Pepper
- Beanstalk

**Gear**
- Basic Sprinkler
- Advanced Sprinkler
- Godly Sprinkler
- Lightning Rod
- Master Sprinkler

# How to use it
Explanation/instructions before you start farming.

## General
1. Install the ones in requirements.txt. (Google if you don't know to install it)
2. Make sure to have the Automatic Mouse and Keyboard (**AMK**) application installed. (https://www.robot-soft.com/mouse-keyboard-recorder.html)<br/>
   _It doesn't matter if it's cracked, but it's gotta be premium._
3. Along with the Automatic Mouse and Keyboard, it usually comes pre-installed with "Scheduling Tasks" application. We will be using that.
4. Download the Macro
5. (**Optional**) If you want to use the Discord Notification script, change the config in settings.json:
```json
{ 
    "TOKEN": "change-me", << Here goes your Discord Bot token.
    "CHANNEL_ID": 12345678, << Here goes your Discord Channel ID (Where you want to see the items you bought)
    "FILE_PATH": "change-me" << Here goes the file path to the "Grow a Garden Farm Stats.txt"
}
``` 

## In-game
1. Put your Recall wrench on the 2nd hotbar.
2. Angle your camera where it can see both seed vendor and gear vendor. <br/>(Theres a scroll feature in the script you can activate for the perfect distance)
3. Make sure your shift-lock is off

## To begin
1. Open the Scheduling Tasks application.
   - Add a new task:
   <br/>![Task Scheduler](https://i.imgur.com/aVZFppW.png)
   - On the "Script File", browse to the .amk macro script and select it.
   - Change the time to your current time's nearest 5 minute mark.<br/>
     (_ex. if you current time is 3:57, your closest time will be 4:00. So put 4:00._)
   - Your settings should look like this (I am not showing my path). <br/> ![Task Scheduler](https://i.imgur.com/XwlhKyw.png)
   - Press Okay on both. Now your script is running on a timer.
2. (**Optional**) If you want to see your hauls, or the items you bought at each run, you can run the GaGM Discord Notification python script. (It only detects the gear shop ones. Will add for seed shop eventually)
3. Profit????

It will automatically run every 5 minutes (The seed shop and gear shop reset every 5 minute interval, but 2 seconds before hitting the 5 minute mark). <br/>Make sure to keep your MONITOR OPEN (I actually fucked up my runs because I closed my monitor).

# My overnight haul only got me this much :( :
![MrBeast](https://i.imgur.com/rGUaxiL.png)



