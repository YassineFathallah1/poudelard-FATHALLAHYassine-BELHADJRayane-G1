import random
from utils.input_utils import load_fichier
from univers.personnage import afficher_personnage
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": list(equipe_data["joueurs"])
    }

    if est_joueur and joueur is not None:
        nom_joueur = joueur["Prenom"] + " " + joueur["Nom"] + " (Attrapeur)"
        nouvelle_liste = [nom_joueur]
        for j in equipe_data["joueurs"]:
            if "(Attrapeur)" not in j and "(Attrapeuse)" not in j:
                nouvelle_liste.append(j)
        equipe["joueurs"] = nouvelle_liste

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba = random.randint(1, 10)

    if proba >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])
        equipe_attaque["score"]    = equipe_attaque["score"]    + 10
        equipe_attaque["a_marque"] = equipe_attaque["a_marque"] + 1
        print(buteur + " marque un but pour " + equipe_attaque["nom"] + " ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] = equipe_defense["a_stoppe"] + 1
        print(equipe_defense["nom"] + " bloque l'attaque !")


def apparition_vifdor():
    return random.randint(1, 6) == 6


def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])
    gagnant["score"]         = gagnant["score"] + 150
    gagnant["attrape_vifdor"] = True
    print("Le Vif d'Or a ete attrape par " + gagnant["nom"] + " ! (+150 points)")
    return gagnant


def afficher_score(e1, e2):
    print("\nScore actuel :")
    print("  -> " + e1["nom"] + " : " + str(e1["score"]) + " points")
    print("  -> " + e2["nom"] + " : " + str(e2["score"]) + " points")


def afficher_equipe(maison, equipe):
    print("\nEquipe de " + maison + " :")
    for j in equipe["joueurs"]:
        print("  - " + j)


def match_quidditch(joueur, maisons):
    data = load_fichier("data/equipes_quidditch.json")
    maison_joueur = joueur.get("Maison", "Gryffondor")

    adversaires = []
    for m in data:
        if m != maison_joueur:
            adversaires.append(m)
    maison_adverse = random.choice(adversaires)

    eq1 = creer_equipe(maison_joueur,  data[maison_joueur],  est_joueur=True, joueur=joueur)
    eq2 = creer_equipe(maison_adverse, data[maison_adverse])

    print("\n" + "=" * 50)
    print("Match de Quidditch : " + maison_joueur + " vs " + maison_adverse + " !")
    print("=" * 50)
    afficher_equipe(maison_joueur,  eq1)
    afficher_equipe(maison_adverse, eq2)
    print("\nTu joues pour " + maison_joueur + " en tant qu'Attrapeur !")

    vifdor = False
    for tour in range(1, 21):
        print("\n--- Tour " + str(tour) + " ---")
        tentative_marque(eq1, eq2, joueur_est_joueur=True)
        tentative_marque(eq2, eq1, joueur_est_joueur=False)
        afficher_score(eq1, eq2)

        if apparition_vifdor():
            attraper_vifdor(eq1, eq2)
            vifdor = True
            print("Fin du match !")
            break

        input("\nAppuyez sur Entree pour continuer...")

    print("\n" + "=" * 50)
    print("SCORE FINAL :")
    afficher_score(eq1, eq2)

    if eq1["score"] > eq2["score"]:
        print("\n" + maison_joueur + " remporte le match !")
        actualiser_points_maison(maisons, maison_joueur, 500)
    elif eq2["score"] > eq1["score"]:
        print("\n" + maison_adverse + " remporte le match...")
        actualiser_points_maison(maisons, maison_adverse, 500)
    else:
        print("\nMatch nul !")

    afficher_maison_gagnante(maisons)


def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n" + "=" * 50)
    print("  CHAPITRE 4 - Le Match de Quidditch")
    print("=" * 50)

    match_quidditch(joueur, maisons)

    print("\n" + "=" * 50)
    print("Fin du Chapitre 4 - Quelle performance !")
    print("\nClassement final de la Coupe des Quatre Maisons :")
    for nom in maisons:
        print("  " + nom + " : " + str(maisons[nom]) + " points")
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
