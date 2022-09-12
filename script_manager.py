import tkinter as tk
import tkinter.font as tkFont
import os
from datetime import datetime
from scripts.extractor import process_unpack, process_repack

def script_select(event):
    if len(script_listbox.curselection()) > 0:
        script = scripts[script_listbox.curselection()[0]]
        chosen_script_entry.configure(state='normal')
        chosen_script_entry.delete(0, "end")
        chosen_script_entry.insert(0, script)
        chosen_script_entry.configure(state='disabled')
        desc_script_text.configure(state='normal')
        desc_script_text.delete('1.0', "end")
        desc_script_text.insert('1.0', script_map[script].get_description())
        desc_script_text.configure(state='disabled')
        run_label_var.set("")
        
def save_select(event):
    if len(save_listbox.curselection()) > 0:
        save = saves[save_listbox.curselection()[0]]
        chosen_save_entry.configure(state='normal')
        chosen_save_entry.delete(0, "end")
        chosen_save_entry.insert(0, save)
        chosen_save_entry.configure(state='disabled')
        run_label_var.set("")

def run_script():
    script = chosen_script_entry.get()
    save = chosen_save_entry.get()
    if len(script) > 0 and len(save) > 0:
        process_unpack(save, "scripts/result")
        try:
            script_map[script].run_script(option_entry.get())
            log.write("[" + str(datetime.now()) + "] Execution - Script : " + script + " - Argument : " + option_entry.get() + " - Savefile : " + save + "\n")
        except:
            script_map[script].run_script()
            log.write("[" + str(datetime.now()) + "] Execution - Script : " + script + " - Savefile : " + save + "\n")
        log.flush()
        process_repack("scripts/result", save)
        run_label_var.set("Ran " + script + " on " + save)

# Listing all the scripts and saves
scripts = [element for element in os.listdir("./scripts") if ".py" in element]
if "extractor.py" in scripts:
    scripts.remove("extractor.py")
if "script_manager.py" in scripts:
    scripts.remove("script_manager.py")
saves = [element for element in os.listdir(".") if ".sav" in element]
if "player.sav" in saves:
    saves.remove("player.sav")
    
# Loading the content and the description of each script
script_map = {elt : __import__("scripts." + elt[:-3], fromlist=[None]) for elt in scripts}

# Start logging
log = open("scripts/log.txt", 'a', encoding='utf-8')

window = tk.Tk()
window.title("F1 Manager 22 Script Manager")
window.columnconfigure(0)
window.columnconfigure(1)
window.columnconfigure(2, weight=5)
window.geometry('770x430')
window.resizable(False, False)
font = tkFont.Font(family="Sans Serif", size=12)
font_small = tkFont.Font(family="Sans Serif", size=10)

LIST_HEIGHT = 22

script_label = tk.Label(master=window, text="Script list", font=font)
script_label.grid(column=0, row=0, rowspan=1, padx=10, pady=5)
script_listbox = tk.Listbox(master=window, height=LIST_HEIGHT, width=25, listvariable=tk.StringVar(value=scripts), font=font_small)
script_listbox.grid(column=0, row=1, rowspan=LIST_HEIGHT, padx=10, pady=5)
script_listbox.bind('<<ListboxSelect>>', script_select)

save_label = tk.Label(master=window, text="Savefile list", font=font)
save_label.grid(column=1, row=0, rowspan=1, padx=10, pady=5)
save_listbox = tk.Listbox(master=window, height=LIST_HEIGHT, width=25, listvariable=tk.StringVar(value=saves), font=font_small)
save_listbox.grid(column=1, row=1, rowspan=LIST_HEIGHT, padx=10, pady=5)
save_listbox.bind('<<ListboxSelect>>', save_select)

chosen_script_label = tk.Label(master=window, text="Selected script :", font=font)
chosen_script_label.grid(column=2, row=1, padx=10, pady=0)
chosen_script_entry = tk.Entry(master=window, width=45, font=font_small)
chosen_script_entry.grid(column=2, row=2, padx=10, pady=0)
chosen_script_entry.configure(state='disabled')

desc_script_label = tk.Label(master=window, text="Script description :", font=font)
desc_script_label.grid(column=2, row=4, padx=10, pady=0)
desc_script_text = tk.Text(master=window, height=8, width=45, wrap="word", font=font_small)
desc_script_text.grid(column=2, row=5, rowspan=6, padx=10, pady=0)
desc_script_text.configure(state='disabled')

chosen_save_label = tk.Label(master=window, text="Selected savefile :", font=font)
chosen_save_label.grid(column=2, row=12, padx=10, pady=0)
chosen_save_entry = tk.Entry(master=window, width=45, font=font_small)
chosen_save_entry.grid(column=2, row=13, padx=10, pady=0)
chosen_save_entry.configure(state='disabled')

option_label = tk.Label(master=window, text="Script argument (if needed) :", font=font)
option_label.grid(column=2, row=15, padx=10, pady=0)
option_entry = tk.Entry(master=window, width=45, font=font_small)
option_entry.grid(column=2, row=16, padx=10, pady=0)

run_button = tk.Button(master=window, text="Run script", command=run_script, font=font)
run_button.grid(column=2, row=18, padx=10, pady=0)
run_label_var = tk.StringVar()
run_label = tk.Label(master=window, textvariable=run_label_var, width=45, font=font_small)
run_label.grid(column=2, row=19, padx=10, pady=0)

window.mainloop()

log.close()