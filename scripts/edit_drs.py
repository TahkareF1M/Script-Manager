import sqlite3

def run_script(option=""):
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    option = option.lower()
    if option == "default":
        cursor.execute("UPDATE Parts_RaceSimConstants SET MinDRSTopSpeedMultiplier = 1.005")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MaxDRSTopSpeedMultiplier = 1.044")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MinDRSAccelerationMultiplier = 1.05")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MaxDRSAccelerationMultiplier = 1.65")
        print("Default DRS values set")
    elif option == "reduced":
        cursor.execute("UPDATE Parts_RaceSimConstants SET MinDRSTopSpeedMultiplier = 1.005")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MaxDRSTopSpeedMultiplier = 1.044")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MinDRSAccelerationMultiplier = 1.05")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MaxDRSAccelerationMultiplier = 1.35")
        print("Reduced DRS values set")
    elif option == "disabled":
        cursor.execute("UPDATE Parts_RaceSimConstants SET MinDRSTopSpeedMultiplier = 1")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MaxDRSTopSpeedMultiplier = 1")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MinDRSAccelerationMultiplier = 1")
        cursor.execute("UPDATE Parts_RaceSimConstants SET MaxDRSAccelerationMultiplier = 1")
        print("Disabled DRS")
    
    conn.commit()
    conn.close()

def get_description():
    return "Choose the DRS behaviour you want. Available options are: default, reduced, disabled.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()