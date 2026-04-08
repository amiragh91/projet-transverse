"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
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
print("l'année prochaine vous aurez : " + str(age+2) + "ans")
if age == 1 and age == 2 :
    print("Vous êtes Bébé")   
elif age <= 12 :
    print("vous etes mineur(e)")
elif  12 < age <= 17 :
    print("Vous êtes Adolescent(e)")
elif age == 17 :
    print("vous etes presque majeur(e)")
elif age == 18 :
    print("Félicitations! Vous êtes tout juste Majeur(e)")
else :
    print("vous etes majeur(e)")
    
