from cryptography.fernet import Fernet

# Génération d'une clé Fernet
cle = Fernet.generate_key()

# Affichage de la clé
print("Clé générée :", cle.decode())
