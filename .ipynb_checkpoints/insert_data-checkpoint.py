import mysql.connector
from datetime import datetime, timedelta
import random

# Configuration de la connexion à MySQL
config = {
    'host': 'localhost',      # Remplace par l'adresse du serveur MySQL
    'user': 'root',           # Remplace par ton nom d'utilisateur MySQL
    'password': '1206',   # Remplace par ton mot de passe MySQL
    'database': 'iot_exam'  # Remplace par le nom de ta base de données
}

try:
    # Connexion à MySQL
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Définition des dates de début et de fin
    start_time = datetime(2025, 1, 18, 8, 0, 0)
    end_time = datetime(2025, 3, 4, 18, 0, 0)
    current_time = start_time

    # Requête SQL pour insérer des données
    insert_query = """
    INSERT INTO data (temperature, humidite, pollution, lumiere, timestamp)
    VALUES (%s, %s, %s, %s, %s)
    """

    # Boucle pour générer les données toutes les 20 minutes
    while current_time <= end_time:
        temperature = round(28 + (random.uniform(0, 4)), 1)  # Entre 28°C et 32°C
        humidite = round(70 + (random.uniform(0, 7)), 1)     # Entre 70% et 77%
        pollution = round(50 + (random.uniform(0, 30)), 1)   # Entre 50 et 80 ppm
        lumiere = round(300 + (random.uniform(0, 150)), 1)   # Entre 300 et 450 lux

        data = (temperature, humidite, pollution, lumiere, current_time)

        cursor.execute(insert_query, data)
        current_time += timedelta(minutes=20)  # Avancer de 20 minutes

    # Valider les insertions
    conn.commit()
    print("Insertion terminée avec succès !")

except mysql.connector.Error as err:
    print(f"Erreur MySQL : {err}")

finally:
    # Fermer la connexion
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Connexion MySQL fermée.")
