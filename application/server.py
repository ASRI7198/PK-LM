from flask import Flask, request, jsonify, send_from_directory
import re
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

# 📌 Charger le modèle GPT-2 fine-tuné
MODEL_PATH = "fine_tuned_gpt2-3"  # Mets ici le chemin de ton modèle
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)
model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)

# 📌 Charger les détails des Pokémon depuis un fichier
def load_pokemon_details(file_path="pokemon_data_cleaned.txt"):
    pokemon_data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read().strip().split("---")
        
        for entry in data:
            lines = entry.strip().split("\n")
            if not lines:
                continue

            match = re.match(r"Pokémon:\s*(.+)", lines[0])
            if match:
                pokemon_name = match.group(1).strip()
                pokemon_data[pokemon_name] = "\n".join(lines[1:])

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
    
    return pokemon_data

pokemon_details = load_pokemon_details()

# 📌 Fonction pour générer une équipe Pokémon
def generate_team(prompt="Donne-moi une équipe format UU:", max_length=100):
    # Supprimer tous les ":" dans le prompt sauf celui à la fin
    if ":" in prompt:
        # Retirer tous les ":" sauf celui à la fin
        prompt = re.sub(r":(?!$)", "", prompt)  # On remplace tous les ":" sauf celui à la fin
    
    # Ajouter un ":" à la fin si ce n'est pas déjà le cas
    if not prompt.endswith(":"):
        prompt += ":"

    inputs = tokenizer(prompt, return_tensors="pt")
    
    outputs = model.generate(
        inputs.input_ids,
        max_length=max_length,
        num_beams=3,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.pad_token_id,
    )

    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    pokemon_part = decoded_output.split(":")[-1]
    pokemons = re.findall(r"\b[A-Za-z-]+\b", pokemon_part)

    while len(pokemons) < 6:
        pokemons.append("Pikachu")  

    return pokemons[:6]


# 📌 Route API pour générer une équipe
@app.route("/generate", methods=["POST"])
def generate_team_with_details():
    data = request.json
    prompt = data.get("prompt", "Donne-moi une équipe format UU:")
    team = generate_team(prompt)

    team_details = {pokemon: pokemon_details.get(pokemon, "Aucun détail trouvé.") for pokemon in team}

    return jsonify({"team": team, "details": team_details})

# 📌 Route pour récupérer les détails d’un Pokémon
@app.route("/pokemon/<pokemon_name>", methods=["GET"])
def get_pokemon_details(pokemon_name):
    details = pokemon_details.get(pokemon_name, "Aucun détail trouvé.")
    return jsonify({"name": pokemon_name, "details": details})

# 📌 Route pour servir le fichier HTML
@app.route("/")
def serve_html():
    return send_from_directory(".", "index.html")

# 📌 Démarrer le serveur Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
