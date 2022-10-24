montuple = ("Pomme", "Kiwi", "Citron", "Cerise", "Melon")

longeur=len(montuple)

for i in range(longeur):
    print(i, montuple[i])

x=0
while x < len(montuple):
    print(montuple[x])
    x=x+1


#liste de 1 à 100

liste1 = range(2,101,2)
print(list(liste1))

#lancé de dés
import random
def lancerDes():
    for i in range(6):
        print("Lancé n°",i, "résultat : " ,random.randrange(1,7))

lancerDes()


#Extension
def lancerDesInput():
    nombreLancers = 0
    #vérifie la saisie de l'utilisateur
    while True:
        nombreSaisi = input()
        #permet de savoir si la saisi est un nombre et s'il est strictement positif
        if nombreSaisi.isdigit(): 
            nombreLancers = int(nombreSaisi)
            break
        else:
            print("Mauvaise saisi, veuillez saisir un nombre : ")

    moyenne = 0.0
    for i in range(nombreLancers):
        moyenne = moyenne + random.randrange(1,7)

    moyenneFinale = moyenne/nombreLancers
    return("La moyenne est de : ", moyenneFinale)

print(lancerDesInput())

#Compter le nombre d'occurence

"""
def countLetterOccurence(phrase):
    chosenLetter = input()
    counter = 0
    for i in phrase:
        if i == chosenLetter.upper() or i == chosenLetter.lower():
            counter+=1

    return "Le nombre d'occurence trouvé : ", counter

phrase="Salut ça va"
print(countLetterOccurence(phrase))
"""

#Extension

def countEachOccurence():
    phrase="Salut ça va"

    #enleve les espaces dans la phrase
    strippedPhrase = phrase.replace(" ","")
    #passe tout en minuscule
    minPhrase = strippedPhrase.lower()
    #créer un dictionnaire avec toutes les lettres de la phrase
    listeDic = {}

    #boucle pour chaque caractère dans la phrase
    for char in minPhrase:
        #si la lettre n'est pas dans le dictionnaire,
        #alors on l'ajoute
        if not listeDic or char not in listeDic.keys():
            listeDic.update({char: 1})
        #sinon l'on incrémente la valeur
        else:
            listeDic[char] += 1

    return listeDic

print(countEachOccurence())


