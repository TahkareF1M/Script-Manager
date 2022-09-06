import sqlite3

def run_script():
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    conn.commit()
    conn.close()
    
    print("Hello there !\nIf this text shows up, then your script manager is running properly")
    
def get_description():
    return "Dummy script to check if it works properly.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()
