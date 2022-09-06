# F1M Script Manager

Requirements : 
Python 3

Safety : 
Always make a copy of your save before running a script in case it breaks something

How to install :
Extract the contents of this archive in your F1 Manager 22 save folder (it should be "C:\Users\<USERNAME>\AppData\Local\F1Manager22\Saved\SaveGames").

How to use :
Launch script_manager.py, it allows you to select the script you want to run and the save you want to run it on. A dummy script that should simply display a short text in the console is included.

How does the sprint race simulation works :
1. Save your game before starting the Imola/Austria/Brazil weekends.
2. Execute the "set_sprint.py" script.
3. Reload your save.
4. Play the weekend with the sprint race.
5. Start the next race weekend that is at the same track.
6. SAVE BEFORE STARTING FP1.
7. Execute the "set_race.py" script.
8. Reload your save.
9. Play the normal race.

Known issues :
Unless they have damage, AI won't pit during this race and will be disqualified. The points are adjusted properly when running the "set_race.py" script.


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
