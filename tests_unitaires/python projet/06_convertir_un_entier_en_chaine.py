"""
initiation à la programmation
le language python
saisir et afficher le nom et lage des utilisation
"""
#saisir des données
nom = input("quel est votre nom ?")
age = input("quel est votre age ?") 

#afficher les resultats
print("---------------")
print("Bonjour " + nom + ",")
print("vous vous appelez " + nom )
print("vous avez " + age + " ans ")
print("l'année prochaine vous aurez : " + str(int(age)+1) + "ans")