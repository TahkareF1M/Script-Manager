import sqlite3

def run_script():
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    # Getting infos to create a duplicate weekend
    day_season = cursor.execute("SELECT Day, CurrentSeason FROM Player_State").fetchone()
    next_event = cursor.execute("SELECT * FROM Races WHERE Day >= ? AND SeasonID = ? ORDER BY Day", day_season).fetchone()
    race_count = cursor.execute("SELECT MAX(RaceID) FROM Races").fetchone()
    
    # Duplicating the weekend
    new_event = (race_count[0]+1, next_event[1], next_event[2]+3, next_event[3], next_event[4], next_event[5], next_event[6], next_event[7], next_event[8], next_event[9], next_event[10], next_event[11], next_event[12], next_event[13])
    cursor.execute("INSERT INTO Races VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", new_event)
    
    # Updating lap count
    cursor.execute("UPDATE Races_Tracks SET Laps = 21 WHERE TrackID = 24")
    cursor.execute("UPDATE Races_Tracks SET Laps = 24 WHERE TrackID = 9")
    cursor.execute("UPDATE Races_Tracks SET Laps = 24 WHERE TrackID = 20")
    print("Sprint race has been set up")
    
    # Updating point system
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 8 WHERE PointScheme = 3 AND RacePos = 1")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 7 WHERE PointScheme = 3 AND RacePos = 2")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 6 WHERE PointScheme = 3 AND RacePos = 3")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 5 WHERE PointScheme = 3 AND RacePos = 4")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 4 WHERE PointScheme = 3 AND RacePos = 5")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 3 WHERE PointScheme = 3 AND RacePos = 6")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 2 WHERE PointScheme = 3 AND RacePos = 7")
    cursor.execute("UPDATE Regulations_NonTechnical_PointSchemes SET Points = 1 WHERE PointScheme = 3 AND RacePos = 8")
    cursor.execute("UPDATE Regulations_Enum_Changes SET CurrentValue = 3 WHERE Name = 'PointScheme'")
    cursor.execute("UPDATE Regulations_Enum_Changes SET CurrentValue = 0 WHERE Name = 'FastestLapBonusPoint'")
    print("Point scheme has been set up")
    
    conn.commit()
    conn.close()

def get_description():
    return "Sets up the sprint race at Imola, Spielberg and Interlagos. Use it before starting the weekend.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()