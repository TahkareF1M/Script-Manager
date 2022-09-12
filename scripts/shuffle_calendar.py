import sqlite3
import random

def run_script():
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    track_ids = [i for i in range(1,25) if i != 3 and i != 16]
    random.shuffle(track_ids)
    
    # Getting all the current season races
    day_season = cursor.execute("SELECT Day, CurrentSeason FROM Player_State").fetchone()
    season_events = cursor.execute("SELECT RaceID FROM Races WHERE SeasonID = " + str(day_season[1])).fetchall()
    
    # Inserting the new calendar
    for i in range(len(track_ids)):
        cursor.execute("UPDATE Races SET TrackID = " + str(track_ids[i]) + " WHERE RaceID = " + str(season_events[i][0]))
    print("Shuffled the calendar")
    
    conn.commit()
    conn.close()

def get_description():
    return "Shuffles the current season calendar randomly. Use it before the first race of the season.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()