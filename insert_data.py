import mysql.connector
from datetime import datetime, timedelta
import random 

config = {
    'host': 'localhost',      
    'user': 'root',           
    'password': 'joseph04',   
    'database': 'iot_exam'  
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    start_time = datetime(2025, 1, 18, 8, 0, 0)
    end_time = datetime(2025, 3, 4, 18, 0, 0)
    current_time = start_time

    insert_query = """
    INSERT INTO data (temperature, humidite, pollution, lumiere, timestamp)
    VALUES (%s, %s, %s, %s, %s)
    """

    while current_time <= end_time:
        temperature = round(28 + (random.uniform(0, 4)), 1)  
        humidite = round(70 + (random.uniform(0, 7)), 1)     
        pollution = round(50 + (random.uniform(0, 30)), 1)   
        lumiere = round(300 + (random.uniform(0, 150)), 1)   

        data = (temperature, humidite, pollution, lumiere, current_time)

        cursor.execute(insert_query, data)
        current_time += timedelta(minutes=20)  

    conn.commit()
    print("Insertion terminée avec succès !")

except mysql.connector.Error as err:
    print(f"Erreur MySQL : {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connexion MySQL fermée.")
