import sqlite3
import random

def run_script():
    conn = sqlite3.connect("scripts/result/main.db")
    cursor = conn.cursor()
    
    # The engine id, ers id and gearbox id for each powertrain
    design_ids = [[], [1,2,3], [10,11,12], [4,5,6], [7,8,9]]
    
    for i in range(1, 5):
        powertrain_cost = cursor.execute("SELECT Cost FROM Parts_Enum_EngineManufacturers WHERE Value = " + str(i)).fetchone()
        engine_stats = cursor.execute("SELECT DesignID, StatID, Value, UnitValue FROM Parts_DesignStatValues WHERE DesignID = " + str(design_ids[i][0])).fetchall()
        ers_stat = cursor.execute("SELECT DesignID, StatID, Value, UnitValue FROM Parts_DesignStatValues WHERE DesignID = " + str(design_ids[i][1])).fetchone()
        gearbox_stat = cursor.execute("SELECT DesignID, StatID, Value, UnitValue FROM Parts_DesignStatValues WHERE DesignID = " + str(design_ids[i][2])).fetchone()
        stats = engine_stats + [ers_stat] + [gearbox_stat]
        
        perf_difference = 0
        for j in range(7):
            change = max(min(random.randint(-3, 3), 100-stats[j][3]), -stats[j][3])
            print(change)
            perf_difference += change
            if stats[j][1] == 12:
                change = change/10
            if change >= 0:
                cursor.execute("UPDATE Parts_DesignStatValues SET Value = Value + " + str(change*10) + " WHERE DesignID = " + str(stats[j][0]) + " AND StatID = " + str(stats[j][1]))
                cursor.execute("UPDATE Parts_DesignStatValues SET UnitValue = UnitValue + " + str(change) + " WHERE DesignID = " + str(stats[j][0]) + " AND StatID = " + str(stats[j][1]))
            else:
                change = -change
                cursor.execute("UPDATE Parts_DesignStatValues SET Value = Value - " + str(change*10) + " WHERE DesignID = " + str(stats[j][0]) + " AND StatID = " + str(stats[j][1]))
                cursor.execute("UPDATE Parts_DesignStatValues SET UnitValue = UnitValue - " + str(change) + " WHERE DesignID = " + str(stats[j][0]) + " AND StatID = " + str(stats[j][1]))
        
        cost_change = abs(perf_difference) // 3
        print(cost_change)
        if perf_difference >= 0:
            cursor.execute("UPDATE Parts_Enum_EngineManufacturers SET Cost = Cost + " + str(cost_change * 500000) + " WHERE Value = " + str(i))
        else:
            cursor.execute("UPDATE Parts_Enum_EngineManufacturers SET Cost = Cost - " + str(cost_change * 500000) + " WHERE Value = " + str(i))
            
        conn.commit()
        print("Successfully updated engine", i)
    
    conn.commit()
    conn.close()

def get_description():
    return "Randomly updates the engines performances. Use it before the first race of the season.\nAuthor: Tahkare"

if __name__ == '__main__':
    run_script()