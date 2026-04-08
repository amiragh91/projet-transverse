"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
"""
""" 
Exercice : Modifier le code pour que le système prennent en compte les exigences suivantes

- Afficher le message "Vous êtes Adolescent(e)" si l'âge est supérieur ou égal à 12 ans ET strictement inférieur à 17
- Afficher le message "Vous êtes Bébé" si l'âge est égal à 1 an OU l'âge est égale à 2 ans
"""

nom = input("quel est votre nom ?")
age_str = input("quel est votre age ?") 

try : 
    age = int(age_str)
except :
    print("Erreur : vous devez saisir une valeur numérique pour l'age")
else :
    #afficher les resultats
    print("---------------")
    print("Bonjour " + nom + ",")
    print("vous vous appelez " + nom )
    print("vous avez " + age_str + " ans ")
    print("l'année prochaine vous aurez : " + str(age+1) + "ans")

    
    # Solution 2
    if age <= 1 or age == 2 :
        print("Vous êtes Bébé")   
    elif age < 12 :
        print("vous etes mineur(e)")
    elif age >= 12 and age < 17 :
        print("Vous êtes Adolescent(e)")
    elif age == 17 :
        print("vous etes presque majeur(e)")
    elif age == 18 :
        print("Félicitations! Vous êtes tout juste Majeur(e)")
    else :
        print("vous etes majeur(e)")
    
