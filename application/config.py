import os
import subprocess
import sys

# Vérifier si pip est installé
def check_pip():
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Pip n'est pas installé. Installez-le d'abord.")
        sys.exit(1)

# Installer Flask et Transformers
def install_requirements():
    print("Installation des dépendances...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "flask", "torch", "transformers"], check=True)
    print("Installation terminée !")

# Lancer le serveur Flask
def start_server():
    print("Démarrage du serveur Flask...")
    os.system(f"{sys.executable} server.py")

if __name__ == "__main__":
    check_pip()
    install_requirements()
    start_server()
