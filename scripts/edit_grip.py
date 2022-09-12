import sqlite3

def run_script(option=""):
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    # For each option, the values are for C1/C2/C3/C4/C5/inter/wets
    option = option.lower()
    if option == "default":
        grip_values = [0.85, 0.908, 0.93, 0.968, 1, 0.799, 0.726]
        durability_values = [1.75, 1.5, 1.089, 0.733, 0.578, 1.25, 2.25]
        for i in range(7):
            cursor.execute("UPDATE Tyres SET Grip = " + str(grip_values[i]) + " WHERE Type = " + str(i))
            cursor.execute("UPDATE Tyres SET Durability = " + str(durability_values[i]) + " WHERE Type = " + str(i))
        print("Default grip and durability values set")
    elif option == "grip-":
        grip_values = [0.57, 0.69, 0.78, 0.89, 1, 0.5, 0.4]
        durability_values = [1.75, 1.5, 1.089, 0.733, 0.578, 1.25, 2.25]
        for i in range(7):
            cursor.execute("UPDATE Tyres SET Grip = " + str(grip_values[i]) + " WHERE Type = " + str(i))
            cursor.execute("UPDATE Tyres SET Durability = " + str(durability_values[i]) + " WHERE Type = " + str(i))
        print("Reduced grip and default durability values set")
    elif option == "durability-":
        grip_values = [0.85, 0.908, 0.93, 0.968, 1, 0.799, 0.726]
        durability_values = [1.15, 1, 0.73, 0.50, 0.38, 0.83, 1.50]
        for i in range(7):
            cursor.execute("UPDATE Tyres SET Grip = " + str(grip_values[i]) + " WHERE Type = " + str(i))
            cursor.execute("UPDATE Tyres SET Durability = " + str(durability_values[i]) + " WHERE Type = " + str(i))
        print("Default grip and reduced durability values set")
    elif option == "both-":
        grip_values = [0.57, 0.69, 0.78, 0.89, 1, 0.5, 0.4]
        durability_values = [1.15, 1, 0.73, 0.50, 0.38, 0.83, 1.50]
        for i in range(7):
            cursor.execute("UPDATE Tyres SET Grip = " + str(grip_values[i]) + " WHERE Type = " + str(i))
            cursor.execute("UPDATE Tyres SET Durability = " + str(durability_values[i]) + " WHERE Type = " + str(i))
        print("Reduced grip and durability values set")
    
    conn.commit()
    conn.close()

def get_description():
    return "Choose the tyre behaviour you want. Available options are: default, grip-, durability-, both-.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()