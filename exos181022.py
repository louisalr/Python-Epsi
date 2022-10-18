prenom="Pierre"
age=20
majeur=True
compte_en_banque=round(20135.384)#arrondi supp
amis=["Marie, Julien", "Adrien"]
parents=("Marc", "Caroline")

print(compte_en_banque)
print(type(amis))
print(type(parents))


#exo2
nombre=str(15)
print("Le nombre est " + nombre)

#exo3
a=2
b=6
c=3

print(f'{a}+{b}+{c}')
print(a,b,c, sep="+")

#exo4

liste1 = range(3)
list2 = range(5)

print(list(list2))

#exo5

def checkString():
    if (type(prenom) == str):
        print("prenom est bien une chaîne de caractères")

prenom="Pierre"
checkString()
prenom=0
checkString()

#sol2
def checkString():
    if isinstance(prenom,str):
        print("prenom est bien une chaîne de caractères")


prenom="Pierre"
checkString()
prenom=0
checkString()

#exo6

a = "Bonjour voici"
x= a.find("j",3,6)
print(x)

#exo7

phrase = "Bonjour tout le monde"
nouvelle_phrase=phrase.replace("Bonjour", "Bonsoir")
print(nouvelle_phrase)

phrase= "Bonjour tout le monde. Je répète Bonjour"
nouvelle_phrase=phrase.replace("Bonjour", "Bonsoir",1 )
print(nouvelle_phrase)

#exo9

chaine = ["Pierre", "Julien", "Anne"]
chaine_tri = sorted(chaine)
print(chaine_tri)

#exo10

import math
def calculSphere(rayon):
    res = ((4*math.pi)/3)*(rayon**3)
    return ("Le volume est de", "%.2f"% res)
print(calculSphere(10))

#exo11


import random

"""

def checkIfGreater():
    nbrand = random.randrange(11)
    a=int(input())
    
    while nbrand != a:
        if nbrand > a:
            print("Le nombre aléa est plus petit!")
            break
        elif nbrand < a:
            print("Le nombre aléa est plus grand!")
            break
        else:
            print("Vous avez trouvé le nombre aléa",a)

checkIfGreater()
"""
"""
    print("nb alea", nbrand)
    if nbrand>10:
        return "Le nombre saisi est plus grand que 10"
    elif nbrand == 10:
        return "Le nombre saisi est bien le nombre aléa"
    else: 
        return "Le nombre saisi est inférieur à 10"
a = input()

print(checkIfGreater(int(a)))
"""

def checkIfGreater():
    nbrand = random.randrange(11)
    print(nbrand)
    while True:
        n = int(input("Saisissez un entier :"))
        if nbrand==n:
            print("Vous avez trouvé le nombre correct")
            break;
        elif nbrand>n:
            print("Le nombre cherché est plus grand")
        else:
            print("Le nombre cherché est plus petit")
    
    print("Nombre trouvé", nbrand)

checkIfGreater()

#exo12

liste_de_nombres = range(5,16)
print(list(liste_de_nombres))