from gpiozero import Motor, Button
from time import sleep

# Configuration des capteurs et des moteurs
capteur_salle_A = Button(2)  # Capteur pour vérifier l'état de la salle A
capteur_salle_B = Button(3)  # Capteur pour vérifier l'état de la salle B
moteur_droite = Motor(forward=4, backward=5)  # Moteur pour aller à droite
moteur_gauche = Motor(forward=6, backward=7)  # Moteur pour aller à gauche
aspirateur = Motor(forward=8)  # Simule l'activation de l'aspirateur

# État initial
position = "A"  # Le robot commence dans la salle A

# Fonction pour aspirer
def aspirer():
    print(f"Le robot aspire dans la salle {position}.")
    aspirateur.forward()
    sleep(3)  # Simulation de l'aspiration pendant 3 secondes
    aspirateur.stop()

# Fonction pour aller à droite
def aller_a_droite():
    print("Le robot se déplace vers la salle B.")
    moteur_droite.forward()
    sleep(2)  # Temps pour atteindre la salle B
    moteur_droite.stop()

# Fonction pour aller à gauche
def aller_a_gauche():
    print("Le robot se déplace vers la salle A.")
    moteur_gauche.forward()
    sleep(2)  # Temps pour atteindre la salle A
    moteur_gauche.stop()

# Boucle principale
try:
    while True:
        if position == "A":
            if capteur_salle_A.is_pressed:  # La salle A est sale
                print("Salle A détectée sale.")
                aspirer()
            else:  # La salle A est propre
                print("Salle A détectée propre.")
                aller_a_droite()
                position = "B"
        elif position == "B":
            if capteur_salle_B.is_pressed:  # La salle B est sale
                print("Salle B détectée sale.")
                aspirer()
            else:  # La salle B est propre
                print("Salle B détectée propre.")
                aller_a_gauche()
                position = "A"
        sleep(1)  # Pause entre chaque vérification

except KeyboardInterrupt:
    print("Arrêt du robot.")
