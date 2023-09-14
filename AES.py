from cryptography.fernet import Fernet

# Clé fixe (vous pouvez générer une clé avec Fernet.generate_key() et la remplacer ici)
CLE_FIXE = b'ZST3Au2mXdUfctSJVFt3ZWFS6tjJnUinSFK7t5i-4IU='

# Chiffrement d'un message avec la clé AES
def crypter_message(message):
    f = Fernet(CLE_FIXE)
    message_chiffre = f.encrypt(message.encode())
    return message_chiffre

# Déchiffrement d'un message avec la clé AES
def decrypter_message(message_chiffre):
    f = Fernet(CLE_FIXE)
    try:
        message_dechiffre = f.decrypt(message_chiffre).decode()
        return message_dechiffre
    except Exception as e:
        print("Erreur lors du déchiffrement :", str(e))
        return None

# Saisir une phrase
def saisir_phrase():
    return input("Entrez la phrase : ")

# Exemple d'utilisation
if __name__ == "__main__":
    # Demander à l'utilisateur de choisir entre chiffrement et déchiffrement
    action = input("Voulez-vous chiffrer (C) ou déchiffrer (D) un message ? ").strip().lower()

    if action == 'c':
        # Saisir une phrase à chiffrer
        message_original = saisir_phrase()

        # Chiffrer le message
        message_chiffre = crypter_message(message_original)
        print("Message chiffré :", message_chiffre.decode())  # Décoder le message chiffré en chaîne de caractères
    elif action == 'd':
        # Saisir le message chiffré
        message_chiffre = input("Entrez le message chiffré : ")

        # Déchiffrer le message
        message_dechiffre = decrypter_message(message_chiffre.encode())
        if message_dechiffre is not None:
            print("Message déchiffré :", message_dechiffre)
        else:
            print("Déchiffrement échoué. Veuillez vérifier le message chiffré.")
    else:
        print("Choix invalide. Veuillez entrer 'C' pour chiffrer ou 'D' pour déchiffrer.")
#gAAAAABlAxxLC5PHSK4RiKyhFkl_1owu4vGsxLOyxEMPR_Z6EccPlHS2JFWAk4Bp-Nq8ToxVhzOYO7GXoyeMlOLOmIKd2AxNww==