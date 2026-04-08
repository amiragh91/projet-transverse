"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
"""
""" 
Exercice : Améliorer le programme pour redemander la saisie s'un âge valide par l'utilisateur. 
tant que l'utilisateur ne renseigne pas un âge numérique alors le système redemande de saisir un âge.

Tant que (la valeur de l'âge n'est pas valide)
  demander la saisie d'une nouvelle valeur d'âge
Continuer le traitement
"""

#saisir le nom
nom = input("quel est votre nom ?")

#saisir l'age
age = ""
while age == "" :
    age_str = input("quel est votre age ?") 
    try : 
        age = int(age_str)
    except :
        print("Erreur : vous devez saisir une valeur numérique pour l'age")
 
#afficher les resultats
print("Bonjour " + nom + ",")
print("vous vous appelez " + nom )
print("vous avez " + age_str + " ans ")
print("l'année prochaine vous aurez : " + str(age+1) + "ans")
if age <= 1 or age == 2 :
    print("Vous êtes Bébé")   
elif age < 12 :
    print("vous etes mineur(e)")
elif age >= 12 and age < 17 :
    print("Vous êtes Adolescent(e)")
elif not age == 17 :
    print("vous etes presque majeur(e)")
elif age == 18 :
    print("Félicitations! Vous êtes tout juste Majeur(e)")
else :
    print("vous etes majeur(e)")
    
