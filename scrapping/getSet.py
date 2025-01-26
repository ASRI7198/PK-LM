from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Fonction pour récupérer les stratégies et les sauvegarder dans le même fichier
def save_strategies(pokemon_name, file):
    url = f"https://www.smogon.com/dex/sm/pokemon/{pokemon_name}/"  # URL de base pour Smogon
    driver.get(url)

    try:
        # Attendre que la page soit complètement chargée et que le bouton soit visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div/div[2]/div/button')))
        
        # Faire défiler la page vers le bas jusqu'à ce que le bouton soit visible
        button = driver.find_element(By.XPATH, '//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div/div[2]/div/button')
        driver.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(2)  # Attendre que le défilement soit terminé

        # Cliquer sur le bouton
        button.click()

        # Attendre que le contenu soit chargé après le clic
        time.sleep(2)

        # Extraire le contenu du Pokémon (en fonction de la structure de la page Smogon)
        content = driver.find_element(By.XPATH, '//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div/div[2]/div/div').text

        # Sauvegarder dans le fichier avec un séparateur entre les Pokémon
        file.write(content + "\n")
        file.write("---\n")  # Ajout du séparateur entre les Pokémon

        print(f"Les stratégies de {pokemon_name} ont été sauvegardées.")

    except Exception as e:
        print(f"Erreur lors de la récupération des stratégies pour {pokemon_name}: {e}")
        
        
# Lire les noms de Pokémon depuis le fichier pokemon_names.txt
with open("pokemon_names.txt", "r", encoding="utf-8") as f:
    pokemon_names = [line.strip() for line in f.readlines()]

# Ouvrir un fichier en mode écriture pour sauvegarder toutes les stratégies
with open("pokemon_strategies.txt", "w", encoding="utf-8") as file:
    # Boucle pour traiter chaque Pokémon
    for pokemon in pokemon_names:
        save_strategies(pokemon, file)

# Fermer le driver après avoir récupéré les informations
driver.quit()
