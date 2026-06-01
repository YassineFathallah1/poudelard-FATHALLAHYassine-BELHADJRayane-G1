def initialiser_personnage(nom, prenom, attributs):
    return {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortileges": [],
        "Attributs": attributs
    }


def afficher_personnage(joueur):
    print("\n========== Profil du personnage ==========")
    for cle in joueur:
        valeur = joueur[cle]
        if type(valeur) == dict:
            print(cle + " :")
            for sous_cle in valeur:
                print("  - " + str(sous_cle) + " : " + str(valeur[sous_cle]))
        elif type(valeur) == list:
            if len(valeur) == 0:
                print(cle + " : (vide)")
            else:
                print(cle + " : " + ", ".join([str(e) for e in valeur]))
        else:
            print(cle + " : " + str(valeur))
    print("==========================================\n")


def modifier_argent(joueur, montant):
    joueur["Argent"] = joueur["Argent"] + montant


def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
