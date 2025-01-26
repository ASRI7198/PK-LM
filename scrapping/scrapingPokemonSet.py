from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Initialisation de Selenium avec Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Accéder à la page
driver.get('https://www.smogon.com/dex/sm/pokemon/')

# Attendre que la page se charge (parfois nécessaire pour éviter que le script se lance trop tôt)
time.sleep(3)

# Liste pour stocker les noms des Pokémon
pokemon_names = []

# Récupérer la première liste de Pokémon visibles
pokemon_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/dex/sm/pokemon/"] span:nth-child(2)')

# Ajouter les premiers noms à la liste
for pokemon in pokemon_elements:
    pokemon_names.append(pokemon.text)

# Défilement de la page jusqu'à ce que de nouveaux Pokémon soient ajoutés
last_pokemon_count = len(pokemon_names)  # Nombre initial de Pokémon récupérés

while True:
    # Récupérer le dernier Pokémon de la liste visible
    last_pokemon = pokemon_elements[-1]
    
    # Faire défiler la page jusqu'à ce dernier Pokémon
    driver.execute_script("arguments[0].scrollIntoView();", last_pokemon)
    
    # Attendre un peu pour laisser le temps aux nouveaux Pokémon de charger
    time.sleep(3)
    
    # Récupérer les nouveaux éléments de Pokémon après le défilement
    new_pokemon_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/dex/sm/pokemon/"] span:nth-child(2)')
    
    # Ajouter les nouveaux noms à la liste si ce sont de nouveaux Pokémon
    for pokemon in new_pokemon_elements:
        if pokemon.text not in pokemon_names:
            pokemon_names.append(pokemon.text)
    
    # Vérifier si de nouveaux Pokémon ont été ajoutés
    if len(pokemon_names) == last_pokemon_count:  # Aucun nouveau Pokémon ajouté
        print("Tous les Pokémon ont été récupérés.")
        break  # Si aucun nouveau Pokémon n'a été trouvé, on arrête
    
    # Mettre à jour le nombre de Pokémon récupérés pour la prochaine itération
    last_pokemon_count = len(pokemon_names)
    
    # Mettre à jour la liste de Pokémon
    pokemon_elements = new_pokemon_elements

# Ouvrir un fichier pour sauvegarder les noms
with open('pokemon_names.txt', 'w') as file:
    for pokemon in pokemon_names:
        file.write(pokemon + '\n')

# Fermer le navigateur
driver.quit()

print("Les noms des Pokémon ont été sauvegardés dans 'pokemon_names.txt'.")
