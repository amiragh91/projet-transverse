"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
"""
def saisir_nom():
    un_nom = ""
    while un_nom == "":
        un_nom = input("Quel est votre nom ? ")
    return un_nom


def saisir_age():
    un_age = 0
    while un_age == 0:
        age_str = input("Quel est votre âge ? ")
        try:
            un_age = int(age_str)
        except:
            print("Erreur : vous devez saisir une valeur numérique pour l'âge")
    return un_age


def afficher_resultats(un_nom, un_age, taille=0):
    print("--------------")
    print("Bonjour " + un_nom + ",")
    print("Vous vous appelez " + un_nom)
    print("Vous avez " + str(un_age) + " ans")
    print("L'année prochaine vous aurez : " + str(un_age + 1) + " ans")

    if un_age == 1 or un_age == 2:
        print("Vous êtes Bébé")
    elif un_age < 12:
        print("Vous êtes mineur(e)")
    elif 12 <= un_age < 17:
        print("Vous êtes Adolescent(e)")
    elif un_age == 17:
        print("Vous êtes presque majeur(e)")
    elif un_age == 18:
        print("Félicitations ! Vous êtes tout juste majeur(e)")
    else:
        print("Vous êtes majeur(e)")

    if taille != 0:
        print("Votre taille est : " + str(taille) + " m")
    print("--------------")

# # saisir le nom
# nom = saisir_nom()

# # saisir l'âge
# age = saisir_age()

# # afficher les résultats
# afficher_resultats(nom, age)

NB_UTILISATEURS = 1

for i in range(NB_UTILISATEURS) :
    nom = saisir_nom()
    age = saisir_age()
    afficher_resultats(nom, age)

  
