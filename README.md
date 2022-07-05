### Attribution
This package is based on [_Jspeleers'_](https://github.com/JSpeleers/BloonsTD6Bot) github repo. I am revamping it here since he is no longer active.

# BloonsTD6Bot

The BloonsTD6Bot is a farming bot for the popular tower defence game [_Bloons TD 6_](https://ninjakiwi.com/Games/Steam/Bloons-TD-6-Steam.html). 
It is intended to be used to farm [_Insta-Monkeys_](https://bloons.fandom.com/wiki/Insta-Monkey) during time-limited 
events such as Easter or Halloween. Bot navigation is done through fuzzy image matching.

The bot is able to finish the map _Dark Castle_ on easy difficulty, standard mode in ~ 7 minutes. 

## Setup

#### Prerequisite

- _Bloons TD 6_ on [Steam](https://store.steampowered.com/app/960090/Bloons_TD_6/)
- Python3

#### Install

- (OPTIONAL) Create a Python virtual environment: `$ python -m venv btd6bot`
- (OPTIONAL) Activate the virtual environment
    - Windows: `$ btd6bot\Scripts\activate.bat` 
    - Unix & MacOS: `$ source btd6bot/bin/activate`
- You might need to upgrade setuptools: `$ pip install setuptools -U`
- Install requirements: `$ pip install -r requirements.txt`

## Start

Starting the bot can be done using the following steps:

1. Run _Bloons TD 6_  from Steam, windowed, with a resolution of 1440x900 and leave it at the home menu
2. Run the bot: `$ python dark_castle.py` for map _Dark Castle_ 
   1. You may need to put `sudo` in front of the command to get it to work propperly. Otherwise it may throw `segmentation fault: 11`.
   2. On the first couple run throughs, you will need to give your terminal or VS code permissions for Accessability, Screen Recording, and ultimately Full Disk Access in order to run this bot successfully. Your system should prompt for the first two, or you can add them manually before the first run.
3. During the initialisation of this bot, switch to the _Bloons TD 6_ game so it is the top most window 
**and** place your mouse on the top left corner of this window

The bot will now navigate the menu and start the game.

<sub>**Remark**: have the commandline and BTD6 open on the same monitor. 
This is a [known issue](https://github.com/asweigart/pyautogui/issues/9) of `pyautogui`.</sub>

## Stop

Stopping this bot, while it is clicking or searching the screen, is done in two ways:

- Move mouse to the top-left corner of the screen. This activates the failsafe of `pyautogui`. 
You can read more about this failsafe [here](https://pyautogui.readthedocs.io/en/latest/introduction.html#fail-safes).
- `Ctrl+C` in the commandline window

#
