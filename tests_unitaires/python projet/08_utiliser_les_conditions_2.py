"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
"""
""" 
Exercice : Modifier le code pour prendre en compte les exigences suivantes :

- Le système doit affiche la mention suivante si l'âge est égal à 17 ans : "Vous êtes presque Majeur(e)"
- Le système doit affiche la mention suivante si l'âge est égal à 18 ans : "Félicitations! Vous êtes tout juste Majeur(e)"
"""

nom = input("quel est votre nom ?")
age_str = input("quel est votre age ?") 

age = int(age_str)

#afficher les resultats
print("---------------")
print("Bonjour " + nom + ",")
print("vous vous appelez " + nom )
print("vous avez " + age_str + " ans ")
print("l'année prochaine vous aurez : " + str(age+1) + "ans")

#Boolean : True/false
# == égal
# < inferieur
# <= inferieur ou egal
# > superieur
# >= superieur ou egal

# 0----------16-17-18-19-------------infini
if age < 17 :
    print("vous etes mineur(e)")
elif age == 17 :
    print("vous etes presque majeur(e)")
elif age == 18 :
    print("Félicitations! Vous êtes tout juste Majeur(e)")
else :
     print("vous etes majeur(e)")
 