nom = "Ali"
age = 18
taille = 1.8
print(f"Vous vous appelez " + nom +", vous avez " + str(age) + " ans, et vous mesurez " + str(taille) + "m")

print(f"vous vous appelez {nom}, vous avez {age} ans, et vous mesurez {taille}m")

print(f"vous vous appelez %s, vous avez %s ans, et vous mesurez %sm" %(nom,age,taille))

print("""
------------------------
vous vous appelez Ali, vous avez 18 ans, et vous mesurez 1.8m
vous vous appelez Ali, vous avez 18 ans, et vous mesurez 1.8m
vous vous appelez Ali, vous avez 18 ans, et vous mesurez 1.8m
-----------------------
""")
print("Vous vous appelez ", nom, ", vous avez" , age," ans, et vous mesurez" ,taille,"m")