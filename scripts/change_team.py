from multiprocessing.resource_sharer import stop
import sqlite3
import tkinter as tk
import tkinter.font as tkFont
import tkinter
from tkinter import * 
from tkinter.ttk import *
from scripts.extractor import process_repack


team = str("")
new_team = 0
leave_change = False

def run_script():
    def ferrari():
        global team
        global new_team
        global option
        team = "Ferrari"
        new_team = 1
        choose_team(team)
        window_change_team.update()

    def mclaren():
        global team
        global new_team
        global option
        team = "Mclaren"
        new_team = 2
        choose_team(team)

    def red_bull():
        global team
        global new_team
        global option
        team = "Red Bull"
        new_team = 3
        choose_team(team)

    def mercedes():
        global team
        global new_team
        global option
        team = "Mercedes"
        new_team = 4
        choose_team(team)

    def alpine():
        global team
        global new_team
        global option
        team = "Alpine"
        new_team = 5
        choose_team(team)

    def williams():
        global team
        global new_team
        global option
        team = "Williams"
        new_team = 6
        choose_team(team)

    def haas():
        global team
        global new_team
        global option
        team = "Haas"
        new_team = 7
        choose_team(team)

    def alpha_tauri():
        global team
        global new_team
        global option
        team = "Alpha Tauri"
        new_team = 8
        choose_team(team)

    def alfa_romeo():
        global team
        global new_team
        global option
        team = "Alfa Romeo"
        new_team = 9
        choose_team(team)

    def aston_martin():
        global team
        global new_team
        global option
        team = "Aston Martin"
        new_team = 10
        choose_team(team)

    def change_team(new_team):
        print(new_team)

    def start_change(new_team):
        print(new_team)
        conn = sqlite3.connect("scripts/result/main.db")
        cursor = conn.cursor()
        
        # option = option.lower()
        # if "ferrari" in option: new_team = 1
        # elif "mclaren" in option: new_team = 2
        # elif "red bull" in option or "redbull" in option or "rb" in option: new_team = 3
        # elif "merc" in option: new_team = 4
        # elif "alpine" in option: new_team = 5
        # elif "williams" in option: new_team = 6
        # elif "haas" in option: new_team = 7
        # elif "alphatauri" in option or "alpha tauri" in option or "at" in option: new_team = 8
        # elif "alfa" in option or "romeo" in option: new_team = 9
        # elif "aston" in option or "martin" in option: new_team = 10
        # else: new_team = -1
        
        if new_team > 0:
            cursor.execute("UPDATE Player SET TeamID = " + str(new_team))
            print("Successfully changed player team")
        #    print(option, "was not recognized as a team")
        
        conn.commit()
        conn.close()
        window_change_team.quit()
        window_change_team.destroy()

    def choose_team(team):
        global team_selection
        team_selection = team
        chosen_team_entry.configure(state='normal')
        chosen_team_entry.delete(0, "end")
        chosen_team_entry.insert(0, team)
        chosen_team_entry.configure(state='disabled')
        return team_selection
    
    global window_change_team
    window_change_team=tkinter.Toplevel()
    window_change_team.title("Team Select")
    img=tk.PhotoImage(file="./images/script_manager/F1ManagerLogo.png")
    window_change_team.iconphoto(False, img)
    window_change_team.geometry("540x400")
    font = tkFont.Font(family="Sans Serif", size=12)

    ferrari_img = tk.PhotoImage(file = "./images/teams/ferrari.png")
    mclaren_img = tk.PhotoImage(file = "./images/teams/mclaren.png")
    red_bull_img = tk.PhotoImage(file = "./images/teams/red_bull.png")
    mercedes_img = tk.PhotoImage(file = "./images/teams/mercedes.png")
    alpine_img = tk.PhotoImage(file = "./images/teams/alpine.png")
    williams_img = tk.PhotoImage(file = "./images/teams/williams.png")
    haas_img = tk.PhotoImage(file = "./images/teams/haas.png")
    alpha_tauri_img = tk.PhotoImage(file = "./images/teams/alpha_tauri.png")
    alfa_romeo_img = tk.PhotoImage(file = "./images/teams/alfa_romeo.png")
    aston_martin_img = tk.PhotoImage(file = "./images/teams/aston_martin.png")

    button_ferrari=tkinter.Button(window_change_team, text="Ferrari", compound=BOTTOM, image = ferrari_img, bg='white', font=font, command=ferrari)
    button_ferrari.grid(row=1,column=0)

    button_mclaren=tkinter.Button(window_change_team, text="Mclaren", compound=BOTTOM, image = mclaren_img, bg='white', font=font, command=mclaren)
    button_mclaren.grid(row=1,column=1)

    button_red_bull=tkinter.Button(window_change_team, text="Red Bull", compound=BOTTOM, image = red_bull_img, bg='white', font=font, command=red_bull)
    button_red_bull.grid(row=1,column=3)

    button_mercedes=tkinter.Button(window_change_team, text="Mercedes", compound=BOTTOM, image = mercedes_img, bg='white', font=font, command=mercedes)
    button_mercedes.grid(row=1,column=4)

    button_alpine=tkinter.Button(window_change_team, text="Alpine", compound=BOTTOM, image = alpine_img, bg='white', font=font, command=alpine)
    button_alpine.grid(row=1,column=5)

    button_williams=tkinter.Button(window_change_team, text="Williams", compound=BOTTOM, image = williams_img, bg='white', font=font, command=williams)
    button_williams.grid(row=2,column=0)

    button_haas=tkinter.Button(window_change_team, text="Haas", compound=BOTTOM, image = haas_img, bg='white', font=font, command=haas)
    button_haas.grid(row=2,column=1)

    button_alpha_tauri=tkinter.Button(window_change_team, text="Alpha Tauri", compound=BOTTOM, image = alpha_tauri_img, bg='white', font=font, command=alpha_tauri)
    button_alpha_tauri.grid(row=2,column=3)

    button_alfa_romeo=tkinter.Button(window_change_team, text="Alfa Romeo", compound=BOTTOM, image = alfa_romeo_img, bg='white', font=font, command=alfa_romeo)
    button_alfa_romeo.grid(row=2,column=4)

    button_aston_martin=tkinter.Button(window_change_team, text="Aston Martin", compound=BOTTOM, image = aston_martin_img, bg='white', font=font, command=lambda : aston_martin)
    button_aston_martin.grid(row=2,column=5)


    chosen_team_label = tk.Label(master=window_change_team, text="Chosen team:", font=font)
    chosen_team_label.grid(column=3, row=3, padx=0, pady=10)
    chosen_team_entry = tk.Entry(master=window_change_team, width=10, font=font)
    chosen_team_entry.insert(0, team)
    chosen_team_entry.grid(column=3, row=4, padx=0, pady=5)
    chosen_team_entry.configure(state='disabled')

    button_run=tkinter.Button(window_change_team, text="Change Team", bg='white', font=font, command=lambda : start_change(new_team))
    button_run.grid(row=5,column=3)
    
    window_change_team.mainloop()
    return


def get_description():
    return "Choose a new team to manage using a GUI.\nAuthors: Tahkare, xhemals"


if __name__ == '__main__':
    run_script()