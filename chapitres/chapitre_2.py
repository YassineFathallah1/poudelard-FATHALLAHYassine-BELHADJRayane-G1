from utils.input_utils import demander_choix, load_fichier
from univers.personnage import afficher_personnage
from univers.maison import repartition_maison


def rencontrer_amis(joueur):
    print("\n" + "=" * 50)
    print("Vous montez a bord du Poudlard Express...")
    print("=" * 50)

    # Ron
    print("\nUn garcon roux entre dans votre compartiment.")
    print("- Salut ! Moi c'est Ron Weasley. On s'assoit ensemble ?")
    choix = demander_choix("Que repondez-vous ?", [
        "Bien sur, assieds-toi !",
        "Desole, je prefere voyager seul."
    ])
    if choix == "Bien sur, assieds-toi !":
        print("Ron sourit : - Genial ! Tu verras, Poudlard c'est incroyable !")
        joueur["Attributs"]["loyaute"] = joueur["Attributs"]["loyaute"] + 1
    else:
        print("Ron hausse les epaules et s'installe ailleurs.")
        joueur["Attributs"]["ambition"] = joueur["Attributs"]["ambition"] + 1

    # Hermione
    print("\nUne fille entre avec une pile de livres.")
    print("- Bonjour, je suis Hermione Granger. Vous avez lu 'Histoire de la Magie' ?")
    choix = demander_choix("Que repondez-vous ?", [
        "Oui, j'adore apprendre !",
        "Non, je prefere les aventures aux bouquins."
    ])
    if choix == "Oui, j'adore apprendre !":
        print("Hermione sourit : - Parfait, nous allons bien nous entendre !")
        joueur["Attributs"]["intelligence"] = joueur["Attributs"]["intelligence"] + 1
    else:
        print("Hermione fronce les sourcils : - Il faudrait pourtant s'y mettre !")
        joueur["Attributs"]["courage"] = joueur["Attributs"]["courage"] + 1

    # Drago
    print("\nUn garcon blond entre avec un air arrogant.")
    print("- Je suis Drago Malefoy. Mieux vaut bien choisir ses amis.")
    choix = demander_choix("Comment reagissez-vous ?", [
        "Je lui serre la main poliment.",
        "Je l'ignore completement.",
        "Je lui reponds avec arrogance."
    ])
    if choix == "Je lui serre la main poliment.":
        print("Drago hoche la tete.")
        joueur["Attributs"]["ambition"] = joueur["Attributs"]["ambition"] + 1
    elif choix == "Je l'ignore completement.":
        print("Drago fronce les sourcils : - Tu le regretteras !")
        joueur["Attributs"]["loyaute"] = joueur["Attributs"]["loyaute"] + 1
    else:
        print("Drago recule, surpris.")
        joueur["Attributs"]["courage"] = joueur["Attributs"]["courage"] + 1

    print("\nVos attributs mis a jour : " + str(joueur["Attributs"]))


def mot_de_bienvenue():
    print("\n" + "~" * 50)
    print("Professeur Dumbledore :")
    print("<< Bienvenue a tous a Poudlard !")
    print("Que vous soyez de Gryffondor, Serpentard,")
    print("Poufsouffle ou Serdaigle, la magie est en vous. >>")
    print("~" * 50)
    input("\nAppuyez sur Entree pour continuer...")


def ceremonie_repartition(joueur):
    print("\n" + "=" * 50)
    print("La ceremonie de repartition commence...")
    print("Le Choixpeau vous observe attentivement.")
    print("=" * 50)

    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je reflechis a un plan", "Je cherche de l'aide", "Je reste calme et j'observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te decrit le mieux ?",
            ["Courageux et loyal", "Ruse et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face a un defi difficile, tu...",
            ["Fonces sans hesiter", "Cherches la meilleure strategie", "Comptes sur tes amis", "Analyses le probleme"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    maison = repartition_maison(joueur, questions)
    joueur["Maison"] = maison

    print("\nLe Choixpeau s'exclame : " + maison + " !!!")
    print("Tu rejoins les eleves de " + maison + " sous les acclamations !")


def installation_salle_commune(joueur):
    maisons_data = load_fichier("data/maisons.json")
    maison = joueur["Maison"]
    data = maisons_data[maison]

    print("\nVous suivez les prefets a travers les couloirs...")
    print("\n" + data["description"])
    print("\n" + data["message_installation"])
    print("Couleurs de votre maison : " + ", ".join(data["couleurs"]))


def lancer_chapitre_2(personnage):
    rencontrer_amis(personnage)
    mot_de_bienvenue()
    ceremonie_repartition(personnage)
    installation_salle_commune(personnage)
    afficher_personnage(personnage)
    print("\n" + "=" * 50)
    print("Fin du Chapitre 2 ! Les cours commencent demain...")
    print("=" * 50)
