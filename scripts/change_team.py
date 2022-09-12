import sqlite3

def run_script(option=""):
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    option = option.lower()
    if "ferrari" in option: new_team = 1
    elif "mclaren" in option: new_team = 2
    elif "red bull" in option or "redbull" in option or "rb" in option: new_team = 3
    elif "merc" in option: new_team = 4
    elif "alpine" in option: new_team = 5
    elif "williams" in option: new_team = 6
    elif "haas" in option: new_team = 7
    elif "alphatauri" in option or "alpha tauri" in option or "at" in option: new_team = 8
    elif "alfa" in option or "romeo" in option: new_team = 9
    elif "aston" in option or "martin" in option: new_team = 10
    else: new_team = -1
    
    if new_team > 0:
        cursor.execute("UPDATE Player SET TeamID = " + str(new_team))
        print("Successfully changed player team")
    else:
        print(option, "was not recognized as a team")
    
    conn.commit()
    conn.close()

def get_description():
    return "Choose a new team to manage by typing its name as an argument.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()