def convertYenEuro():
    x = input("1: conersion yen vers euro, 2: conversion euro vers yen, exit: pour quitter le programme\n")
    if(x == "exit"):
        print("Terminé")
        return
    y = float(input("Veuillez entrer le nombre à convertir: \n"))
    if(x == "1"):
        y = y*0.00757
        print(y)
        print(" €")
        convertYenEuro()
    elif(x == "2"):
        y = y*132.1085
        print(y)
        print(" ¥")
        convertYenEuro()

    else:
        print("Erreur option entrée non valide")
        convertYenEuro()

convertYenEuro()
    
    


