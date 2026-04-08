"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
"""
#saisir des données
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


if age < 18 :
    print("vous etes mineur(e)")
else :
     print("vous etes majeur(e)")
 