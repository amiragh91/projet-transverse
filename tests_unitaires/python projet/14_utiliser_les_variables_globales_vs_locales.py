""" 
Langage Python
Initiation à la programmation
Saisir et afficher le nom et l'âge d'un utilisateur 
"""

""" 
Exercice : Faire évoluer le code pour utiliser une variable globales dans les fonctions
"""
nom = ""
age = 0

def demander_nom() :
    global nom
    while nom == "" :
        nom = input("Quel est votre nom? ")
    return nom

def demander_age(nom) :
    global age
    while age == 0 :
        age_str = input("Quel est vôte âge " + nom +"? ")
        try :
           age = int(age_str)
        except :
            print("ERREUR : Vous devez saisir une valeur numérique pour l'âge")
    return age

def afficher_resultats(nom, age) :
    print("----------------------------")
    print("----------------------------")
    print("Bonjour " + nom +", vous avez " + str(age)+ " ans.")
    print("L'année prochaine vous aurez " + str(age+1) + " ans.") 
    if age == 1 or age == 2 :
        print("Vous êtes Bébé")
    elif 2 < age < 12 :
        print("Vous êtes Mineur(e).")
    elif 12 <= age < 17 :
        print("Vous êtes Adolescent(e)")
    elif age == 17 :
        print("Vous êtes presque Majeur(e)")
    elif age == 18 :
        print("Félicitations! Vous êtes tout juste Majeur(e)")
    else :
        print("Vous êtes Majeur(e).")

# Partie 1 : demander le nom
nom = demander_nom()

# Partie 2 : demander l'âge
age = demander_age(nom)

# Partie 3 : afficher les résultats
afficher_resultats(nom, age)