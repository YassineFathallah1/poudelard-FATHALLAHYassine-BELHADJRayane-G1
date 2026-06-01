import random
from utils.input_utils import load_fichier
from univers.personnage import afficher_personnage, ajouter_objet
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    tous = load_fichier(chemin_fichier)

    offensifs   = []
    defensifs   = []
    utilitaires = []
    for sort in tous:
        if sort["type"] == "Offensif":
            offensifs.append(sort)
        elif sort["type"] == "Defensif" or sort["type"] == "Défensif":
            defensifs.append(sort)
        else:
            utilitaires.append(sort)

    appris = []
    print("\nTu commences tes cours de magie a Poudlard...")

    # 1 offensif
    while True:
        s = random.choice(offensifs)
        if s not in appris:
            appris.append(s)
            break

    # 1 defensif
    while True:
        s = random.choice(defensifs)
        if s not in appris:
            appris.append(s)
            break

    # 3 utilitaires
    compteur = 0
    while compteur < 3:
        s = random.choice(utilitaires)
        if s not in appris:
            appris.append(s)
            compteur = compteur + 1

    for sort in appris:
        print("Tu viens d'apprendre : " + sort["nom"] + " (" + sort["type"] + ")")
        ajouter_objet(joueur, "Sortileges", sort["nom"])
        input("Appuie sur Entree pour continuer...")

    print("\nSortileges maitrisés :")
    for sort in appris:
        print("  - " + sort["nom"] + " (" + sort["type"] + ") : " + sort["description"])


def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    toutes = load_fichier(chemin_fichier)

    choisies = []
    while len(choisies) < 4:
        q = random.choice(toutes)
        if q not in choisies:
            choisies.append(q)

    print("\n" + "=" * 50)
    print("Quiz de magie de Poudlard !")
    print("4 questions - bonne reponse = +25 pts pour ta maison")
    print("=" * 50)

    score = 0
    for i in range(len(choisies)):
        q = choisies[i]
        print("\n" + str(i + 1) + ". " + q["question"])
        reponse = input("> ").strip()
        if reponse.lower() == q["reponse"].lower():
            print("Bonne reponse ! +25 points.")
            score = score + 25
        else:
            print("Mauvaise reponse. La bonne reponse etait : " + q["reponse"])
        input("Appuie sur Entree pour continuer...")

    print("\nScore obtenu : " + str(score) + " points")
    return score


def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)
    score = quiz_magie(personnage)

    if "Maison" in personnage and score > 0:
        actualiser_points_maison(maisons, personnage["Maison"], score)

    afficher_maison_gagnante(maisons)
    afficher_personnage(personnage)

    print("\n" + "=" * 50)
    print("Fin du Chapitre 3 ! Vous maitrisez les bases de la magie.")
    print("=" * 50)
