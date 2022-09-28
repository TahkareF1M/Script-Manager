import sqlite3

def run_script(option="default"):
    option = option.lower()
    settings = {
        "MinDRSTopSpeedMultiplier": "1.005",
        "MaxDRSTopSpeedMultiplier": "1.044",
        "MinDRSAccelerationMultiplier": "1.05",
        "MaxDRSAccelerationMultiplier": "1.65",
    }
    message = "Default DRS values set"

    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    if option == "reduced":
        settings["MaxDRSAccelerationMultiplier"] = "1.35" 
        message = "Reduced DRS values set"

    elif option == "disabled":
        for property in settings:
            settings[property] = "1"
        message = "Disabled DRS"
    
    for property, value in settings.items():
        cursor.execute(f"UPDATE Parts_RaceSimConstants SET {property} = {value}")
    print(message)
    
    conn.commit()
    conn.close()

def get_description():
    return "Choose the DRS behaviour you want. Available options are: default, reduced, disabled.\nAuthor: Tahkare"

if __name__ == "__main__":
    run_script()