import requests
import time
import random

# URL de l'API
url = "https://backend-iot.cafe-numerique.org/api/create-data"

# Fonction pour envoyer les données
def envoyer_donnees():
    while True:
        # Génération de valeurs légèrement altérées
        humidite = random.uniform(70, 75)  # Humidité variant entre 70 et 75
        temperature = random.uniform(28, 30)  # Température entre 28 et 30
        pollution = random.uniform(60, 65)  # Pollution entre 60 et 65
        lumiere = random.uniform(320, 360)  # Lumière entre 320 et 360

        # Construction des paramètres
        params = {
            "hum": round(humidite, 1),
            "temp": round(temperature, 1),
            "pol": round(pollution, 1),
            "lum": round(lumiere, 1)
        }

        # Envoi de la requête GET
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                print(f"✅ Données envoyées avec succès : {params}")
            else:
                print(f"❌ Erreur {response.status_code} : {response.text}")
        except Exception as e:
            print(f"⚠️ Erreur lors de l'envoi : {e}")

        # Pause de 3 minutes
        time.sleep(10)

# Lancement du script
envoyer_donnees()
