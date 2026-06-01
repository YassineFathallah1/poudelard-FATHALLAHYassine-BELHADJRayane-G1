from utils.input_utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print("+" + str(points) + " points pour " + nom_maison + " ! Total : " + str(maisons[nom_maison]) + " points.")
    else:
        print("Maison introuvable : " + nom_maison)


def afficher_maison_gagnante(maisons):
    score_max = 0
    for nom in maisons:
        if maisons[nom] > score_max:
            score_max = maisons[nom]

    gagnantes = []
    for nom in maisons:
        if maisons[nom] == score_max:
            gagnantes.append(nom)

    if len(gagnantes) == 1:
        print("La maison gagnante est " + gagnantes[0] + " avec " + str(score_max) + " points !")
    else:
        print("Egalite entre : " + ", ".join(gagnantes) + " avec " + str(score_max) + " points chacune !")


def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attributs = joueur["Attributs"]
    scores["Gryffondor"]  = scores["Gryffondor"]  + attributs["courage"]      * 2
    scores["Serpentard"]  = scores["Serpentard"]   + attributs["ambition"]     * 2
    scores["Poufsouffle"] = scores["Poufsouffle"]  + attributs["loyaute"]      * 2
    scores["Serdaigle"]   = scores["Serdaigle"]    + attributs["intelligence"] * 2

    for question, options, maisons_associees in questions:
        reponse = demander_choix(question, options)
        index = options.index(reponse)
        maison_choisie = maisons_associees[index]
        scores[maison_choisie] = scores[maison_choisie] + 3

    print("\nResultat des scores :")
    for nom in scores:
        print("  " + nom + " : " + str(scores[nom]) + " points")

    score_max = 0
    for nom in scores:
        if scores[nom] > score_max:
            score_max = scores[nom]

    maison_finale = ""
    for nom in scores:
        if scores[nom] == score_max:
            maison_finale = nom
            break

    return maison_finale
