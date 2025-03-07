from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

url = "https://docs.google.com/forms/d/e/1FAIpQLScMvP2H3blvAqGZxBAlDkcUdz7PvOPSWPSkYYxL9YyBy_J6hA/viewform?usp=header"

driver = webdriver.Chrome()

def remplir_formulaire():
    driver.get(url)
    time.sleep(3)

    # Localiser les champs de texte (ajuste les sélecteurs si nécessaire)
    champs = driver.find_elements(By.XPATH, "//input[@type='text']")
    if champs:
        champs[0].send_keys("Réponse automatique 1")
        champs[1].send_keys("Réponse automatique 2")

    # Sélectionner une option aléatoire pour les questions à choix multiple
    questions_choix_multiple = driver.find_elements(By.XPATH, "//div[@role='radiogroup']")
    for question in questions_choix_multiple:
        options = question.find_elements(By.XPATH, ".//div[@role='radio']")
        if options:
            random.choice(options).click()

    # Soumettre le formulaire
    bouton_envoyer = driver.find_element(By.XPATH, "//span[text()='Envoyer']")
    bouton_envoyer.click()

    time.sleep(2)

# Nombre de fois à soumettre le formulaire
for _ in range(5):
    remplir_formulaire()

driver.quit()
