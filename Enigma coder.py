import string

# Définition des rotors et du réflecteur
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Définition des positions initiales des rotors
position_rotor1 = input("Entrez la position initiale du rotor 1 (A-Z) : ").upper()
position_rotor2 = input("Entrez la position initiale du rotor 2 (A-Z) : ").upper()
position_rotor3 = input("Entrez la position initiale du rotor 3 (A-Z) : ").upper()

# Fonction pour faire avancer un rotor
def avancer_rotor(rotor):
    return rotor[1:] + rotor[0]

# Initialisation des rotors avec les positions initiales
for _ in range(ord(position_rotor1) - ord('A')):
    rotor1 = avancer_rotor(rotor1)
for _ in range(ord(position_rotor2) - ord('A')):
    rotor2 = avancer_rotor(rotor2)
for _ in range(ord(position_rotor3) - ord('A')):
    rotor3 = avancer_rotor(rotor3)

# Fonction pour chiffrer une lettre
def chiffrer_lettre(lettre, rotor):
    index = string.ascii_uppercase.index(lettre)
    return rotor[index]

# Fonction pour déchiffrer une lettre
def dechiffrer_lettre(lettre, rotor):
    index = rotor.index(lettre)
    return string.ascii_uppercase[index]

# Demander la phrase à chiffrer
phrase = input("Entrez la phrase à chiffrer : ").upper()
message_chiffre = ""

# Chiffrer la phrase lettre par lettre
for lettre in phrase:
    if lettre in string.ascii_uppercase:
        lettre = chiffrer_lettre(lettre, rotor1)
        lettre = chiffrer_lettre(lettre, rotor2)
        lettre = chiffrer_lettre(lettre, rotor3)
        lettre = reflector[string.ascii_uppercase.index(lettre)]
        lettre = dechiffrer_lettre(lettre, rotor3)
        lettre = dechiffrer_lettre(lettre, rotor2)
        lettre = dechiffrer_lettre(lettre, rotor1)
        rotor1 = avancer_rotor(rotor1)
        if rotor1[0] == position_rotor1:
            rotor2 = avancer_rotor(rotor2)
            if rotor2[0] == position_rotor2:
                rotor3 = avancer_rotor(rotor3)
        message_chiffre += lettre
    else:
        message_chiffre += lettre

# Afficher le message chiffré
print("Message chiffré : " + message_chiffre)
