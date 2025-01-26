# PK-LM
Large Language Model-based System for Optimizing Competitive Pokémon Teams

# Membres du groupe

Rida ASRI

Loric GROS

Mathys SAMBET

## Description
PK-LM est un projet visant à développer un système basé sur des grands modèles de langage (LLMs), comme LLaMA 2, pour optimiser les équipes de Pokémon en fonction des préférences des utilisateurs et des tendances du métagame. Ce projet vise à simplifier le processus de construction d'équipes pour les joueurs, tout en offrant des recommandations stratégiques avancées.

## Contexte
L'optimisation dans les batailles Pokémon compétitives est souvent complexe et chronophage. Les outils actuels, tels que les bases de données statiques comme [Smogon](https://www.smogon.com), manquent de flexibilité pour intégrer les préférences des joueurs ou pour proposer des équipes adaptées aux stratégies personnelles. PK-LM vise à combler cette lacune en utilisant la puissance des LLMs pour générer des équipes optimales de manière dynamique.

## Objectifs

### Objectif 1 : Génération d'équipes stratégiques optimisées
- Utiliser GPT-2, ajusté avec des données spécifiques aux batailles Pokémon.
- Prendre en compte les tendances du métagame, les synergies entre Pokémon, et les règles compétitives.
- Simuler des combats pour évaluer la compétitivité des équipes générées.

### Objectif 2 : Intégration des préférences stratégiques des utilisateurs
- Permettre aux utilisateurs de personnaliser leurs équipes en fonction de leurs stratégies.
- Tester la pertinence des équipes générées avec des utilisateurs pour affiner les recommandations.

### Objectif 3 : Interface utilisateur et exportation vers Pokémon Showdown
- Développer une interface interactive permettant aux joueurs de visualiser et personnaliser leurs équipes.
- Exporter les équipes dans un format compatible avec [Pokémon Showdown](https://pokemonshowdown.com) pour une utilisation facile.

## Méthodologie

### WP 1 : Coordination du projet
- **Tâche 1.1** : Création de l'équipe.

### WP 2 : Collecte et préparation des données
- **Tâche 2.1** : Collecter des données sur les équipes et stratégies Pokémon.
- **Tâche 2.2** : Préparer les données pour l'entraînement de LLaMA 2.
- **Tâche 2.3** : Nettoyer et traiter les jeux de données.

### WP 3 : Développement et ajustement des LLMs
- **Tâche 3.1** : Ajuster LLaMA 2 pour la génération d'équipes Pokémon.
- **Tâche 3.2** : Développer des algorithmes d'optimisation pour les équipes.
- **Tâche 3.3** : Tester les performances du modèle et ajuster.

### WP 4 : Tests et validation
- **Tâche 4.1** : Tests utilisateurs pour évaluer les recommandations.
- **Tâche 4.2** : Collecter des retours et itérer sur le modèle.
- **Tâche 4.3** : Évaluer les performances des équipes dans des batailles simulées.

### WP 5 : Rapport final et achèvement du projet
- **Tâche 5.1** : Rédaction du rapport final.

## Technologies Utilisées
- **Langage Modèle** : GPT-2
- **Frameworks** : Fine-tuning sur des modèles pré-entraînés
- **Outils d’exportation** : Format compatible avec Pokémon Showdown

# Application
Pour lancer l'application il faut télécharger le fine tune du llm sur ce lien drive : https://drive.google.com/drive/folders/1FmU-AZMbrtgC_lMqhotP5BX6NxUEuDh-?usp=sharing . Placer le ensuite dans le dossier application, puis lancer config.py avec la commande "python config.py" dans un cmd pour installer les dépendances et cela lancera aussi automatiquement le server flask. Aller ensuite sur l'adresse suivante 127.0.0.1:5000 pour ouvrir l'application

## Références
- [Smogon](https://www.smogon.com)
- [Pokémon Showdown](https://pokemonshowdown.com)
- [Mewtagen - Jeffrey Cheng](https://github.com/jeffreyscheng/Mewtagen)
- "From Large Language Models and Optimization to Decision Optimization CoPilot: A Research Manifesto"
- "StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving"



