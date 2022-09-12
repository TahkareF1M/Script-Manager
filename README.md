# F1M Script Manager

**Requirements :**  
Python 3

**Safety :**  
Always make a copy of your save before running a script in case something goes wrong.

**How to install :**  
Extract the contents of this archive in your save folder (it should be `C:\Users\<USERNAME>\AppData\Local\F1Manager22\Saved\SaveGames`).

**How to use :**  
1. Launch `script_manager.py` and save your game (the order doesn't matter).  
2. Choose which script to run, the save you want to run it on and specify an argument for the scripts that require one.
3. Load your save.

Feel free to make your own scripts and send them to me if you want them to be included in this repository.

===============================================

### How to use the scripts

`change_team.py` : specify the name of the new team you want to manage as an argument (ex : Ferrari, McLaren, Alpha Tauri).  
`edit_drs.py` : specify the drs strength you want as an argument. Accepted values are "default", "reduced" and "disabled".  
`edit_grip.py` : specifiy the tyre behaviour you want as an argument. Accepted values are "default", "grip-", "durability-" and "both-".  
`shuffle_calendar.py` : run it before the first race of the season to shuffle the race calendar.  
`shuffle_engines.py` : run it before starting the new season if you want to know the new values before choosing a new engine or before the first race of the season if you want to be surprised.  

`set_sprint.py` and `set_race.py`:  
1. Save your game before starting the Imola/Austria/Brazil race weekends.
2. Run `set_sprint.py`.
3. Play the weekend with the sprint race.
4. Start the next race weekend at the same track but DO NOT START FP1 and save your game.
5. Run `set_race.py`.
6. Load your save and play the race.

**Known issues :**
Any driver not using 2 different tyre compounds during the sprint will show up as disqualified.
The standings are corrected properly when `set_race.py` is ran.

===============================================

The database unpacker/repacker was made by xAranaktu :
https://github.com/xAranaktu/F1-Manager-2022-SaveFile-Repacker

MIT License

Copyright (c) 2022 Paweł

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
