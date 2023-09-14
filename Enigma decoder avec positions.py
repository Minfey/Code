import string

# Définition des rotors et du réflecteur
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


# Fonction pour faire avancer un rotor
def avancer_rotor(rotor):
    return rotor[1:] + rotor[0]


# Fonction pour chiffrer une lettre
def chiffrer_lettre(lettre, rotor):
    index = string.ascii_uppercase.index(lettre)
    return rotor[index]


# Fonction pour déchiffrer une lettre
def dechiffrer_lettre(lettre, rotor):
    index = rotor.index(lettre)
    return string.ascii_uppercase[index]


# Fonction pour déchiffrer une phrase avec des positions de rotor spécifiées
def dechiffrer_phrase(phrase, position_rotor1, position_rotor2, position_rotor3):
    phrase = phrase.upper()
    rotor1_temp = rotor1
    rotor2_temp = rotor2
    rotor3_temp = rotor3
    message_dechiffre = ""

    # Initialisation des rotors avec les positions spécifiées
    for _ in range(ord(position_rotor1) - ord('A')):
        rotor1_temp = avancer_rotor(rotor1_temp)
    for _ in range(ord(position_rotor2) - ord('A')):
        rotor2_temp = avancer_rotor(rotor2_temp)
    for _ in range(ord(position_rotor3) - ord('A')):
        rotor3_temp = avancer_rotor(rotor3_temp)

    # Déchiffrer la phrase lettre par lettre
    for lettre in phrase:
        if lettre in string.ascii_uppercase:
            lettre = dechiffrer_lettre(lettre, rotor1_temp)
            lettre = dechiffrer_lettre(lettre, rotor2_temp)
            lettre = dechiffrer_lettre(lettre, rotor3_temp)
            lettre = reflector[string.ascii_uppercase.index(lettre)]
            lettre = chiffrer_lettre(lettre, rotor3_temp)
            lettre = chiffrer_lettre(lettre, rotor2_temp)
            lettre = chiffrer_lettre(lettre, rotor1_temp)
            rotor1_temp = avancer_rotor(rotor1_temp)
            if rotor1_temp[0] == position_rotor1:
                rotor2_temp = avancer_rotor(rotor2_temp)
                if rotor2_temp[0] == position_rotor2:
                    rotor3_temp = avancer_rotor(rotor3_temp)
            message_dechiffre += lettre
        else:
            message_dechiffre += lettre

    # Afficher le message déchiffré
    print(f"Rotors initiaux : {position_rotor1}{position_rotor2}{position_rotor3}")
    print(f"Message déchiffré : {message_dechiffre}")


# Demander la phrase à déchiffrer et les positions des rotors
phrase_chiffree = input("Entrez la phrase à déchiffrer : ")
position_rotor1 = input("Entrez la position initiale du rotor 1 (A-Z) : ").upper()
position_rotor2 = input("Entrez la position initiale du rotor 2 (A-Z) : ").upper()
position_rotor3 = input("Entrez la position initiale du rotor 3 (A-Z) : ").upper()

# Appeler la fonction de déchiffrement
dechiffrer_phrase(phrase_chiffree, position_rotor1, position_rotor2, position_rotor3)
