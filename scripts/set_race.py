import sqlite3

def run_script():
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    # Getting infos to set up the race properly
    day_season = cursor.execute("SELECT Day, CurrentSeason FROM Player_State").fetchone()
    next_event = cursor.execute("SELECT RaceID FROM Races WHERE Day >= "+str(day_season[0])+" ORDER BY Day").fetchone()
    last_event = cursor.execute("SELECT RaceID, TrackID FROM Races WHERE Day <= "+str(day_season[0])+" ORDER BY Day DESC").fetchone()
    
    # Skipping ahead to the race
    cursor.execute("UPDATE Player_State SET Day = "+str(day_season[0]+2))
    cursor.execute("UPDATE Save_Weekend SET WeekendStage = 9")
    cursor.execute("UPDATE Save_Weekend SET SimulatedQ1 = 1")
    cursor.execute("UPDATE Save_Weekend SET SimulatedQ2 = 1")
    cursor.execute("UPDATE Save_Weekend SET SimulatedQ3 = 1")
    
    # Restoring the proper lap count
    cursor.execute("UPDATE Races_Tracks SET Laps = 63 WHERE TrackID = 24")
    cursor.execute("UPDATE Races_Tracks SET Laps = 71 WHERE TrackID = 9")
    cursor.execute("UPDATE Races_Tracks SET Laps = 71 WHERE TrackID = 20")
    print("Main race has been set up")
    
    # Restoring the point scheme
    cursor.execute("UPDATE Regulations_Enum_Changes SET CurrentValue = 1 WHERE Name = 'PointScheme'")
    cursor.execute("UPDATE Regulations_Enum_Changes SET CurrentValue = 1 WHERE Name = 'FastestLapBonusPoint'")
    print("Point scheme has been set up")
    
    conn.commit()
    
    # Correcting sprint finish order
    sprint_result = cursor.execute("SELECT Season, FinishingPos, DriverID, TeamID, Laps, Time, Points FROM Races_Results WHERE RaceID = "+str(last_event[0])).fetchall()
    adjusted_result = sorted(sprint_result, key=lambda x:x[4]*10000-x[5], reverse=True)
    for i in range(20):
        cursor.execute("UPDATE Races_Results SET FinishingPos = FinishingPos + 20 WHERE RaceID = " + str(last_event[0]) + " AND DriverID = " + str(adjusted_result[i][2]))
    
    for i in range(20):
        if adjusted_result[i][1] != i+1:
            point_change = adjusted_result[i][6] - max(0, 8-i)
        else:
            point_change = 0
        cursor.execute("UPDATE Races_Results SET Points = "+ str(max(0, 8-i)) + " WHERE RaceID = " + str(last_event[0]) + " AND DriverID = " + str(adjusted_result[i][2]))
        cursor.execute("UPDATE Races_Results SET DNF = 0 WHERE RaceID = " + str(last_event[0]) + " AND DriverID = " + str(adjusted_result[i][2]))
        cursor.execute("UPDATE Races_Results SET FinishingPos = " + str(i+1) +" WHERE RaceID = " + str(last_event[0]) + " AND DriverID = " + str(adjusted_result[i][2]))
        cursor.execute("UPDATE Races_DriverStandings SET Points = Points + " + str(point_change) + " WHERE SeasonID = " + str(adjusted_result[i][0]) + " AND DriverID = " + str(adjusted_result[i][2]))
        cursor.execute("UPDATE Races_DriverStandings SET LastPointsChange = LastPointsChange + " + str(point_change) + " WHERE SeasonID = " + str(adjusted_result[i][0]) + " AND DriverID = " + str(adjusted_result[i][2]))
        cursor.execute("UPDATE Races_DriverStandings SET LastPositionChange = 0 WHERE SeasonID = " + str(adjusted_result[i][0]) + " AND DriverID = " + str(adjusted_result[i][2]))
        cursor.execute("UPDATE Races_TeamStandings SET Points = Points + " + str(point_change) + " WHERE SeasonID = " + str(adjusted_result[i][0]) + " AND TeamID = " + str(adjusted_result[i][3]))
        cursor.execute("UPDATE Races_TeamStandings SET LastPointsChange = LastPointsChange + " + str(point_change) + " WHERE SeasonID = " + str(adjusted_result[i][0]) + " AND TeamID = " + str(adjusted_result[i][3]))
        cursor.execute("UPDATE Races_TeamStandings SET LastPositionChange = 0 WHERE SeasonID = " + str(adjusted_result[i][0]) + " AND TeamID = " + str(adjusted_result[i][3]))
        
        conn.commit()
    print("Sprint race results have been validated")
        
    
    # Setting up the grid properly
    sprint_result = cursor.execute("SELECT Season, FinishingPos, DriverID, TeamID, Laps, Time, Points FROM Races_Results WHERE RaceID = "+str(last_event[0])).fetchall()
    if last_event[1] == 24:
        lap_count = 21
    else:
        lap_count = 24
    for element in sprint_result:
        cursor.execute("INSERT INTO Races_QualifyingResults VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (element[0], next_event[0], 1, element[1], element[2], element[3], element[5], 0, lap_count))
        if element[1] <= 15:
            cursor.execute("INSERT INTO Races_QualifyingResults VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (element[0], next_event[0], 2, element[1], element[2], element[3], element[5], 0, lap_count))
        if element[1] <= 10:
            cursor.execute("INSERT INTO Races_QualifyingResults VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (element[0], next_event[0], 3, element[1], element[2], element[3], element[5], 0, lap_count))
    print("Starting grid has been set up")
    
    conn.commit()
    conn.close()

def get_description():
    return "Sets up the main race at Imola, Spielberg and Interlagos. Use it after starting the second weekend and before FP1.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()
