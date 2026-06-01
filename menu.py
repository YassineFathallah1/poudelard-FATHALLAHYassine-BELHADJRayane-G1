from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch


def afficher_menu_principal():
    print("\n" + "=" * 50)
    print("         POUDLARD - Jeu d'aventure")
    print("=" * 50)
    print("  1. Lancer le jeu")
    print("  2. Quitter")
    print("=" * 50)


def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard":  0,
        "Poufsouffle": 0,
        "Serdaigle":   0
    }

    while True:
        afficher_menu_principal()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            personnage = lancer_chapitre_1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage, maisons)
            lancer_chapitre4_quidditch(personnage, maisons)

        elif choix == "2":
            print("\nAu revoir ! Que la magie soit avec vous.")
            break

        else:
            print("Choix invalide. Entrez 1 ou 2.")
