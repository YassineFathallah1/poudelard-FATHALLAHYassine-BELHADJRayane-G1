from utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier
from univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_objet


def introduction():
    print("\n" + "=" * 50)
    print("  CHAPITRE 1 - L'arrivee dans le monde magique")
    print("=" * 50)
    print("\nBienvenue dans le monde des sorciers !")
    print("Une grande aventure vous attend a Poudlard...")
    input("\nAppuyez sur Entree pour commencer...")


def creer_personnage():
    print("\n--- Creation de votre personnage ---")
    nom    = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prenom de votre personnage : ")

    print("\nChoisissez vos attributs (entre 1 et 10) :")
    courage      = demander_nombre("Niveau de courage (1-10) : ",      1, 10)
    intelligence = demander_nombre("Niveau d'intelligence (1-10) : ",  1, 10)
    loyaute      = demander_nombre("Niveau de loyaute (1-10) : ",      1, 10)
    ambition     = demander_nombre("Niveau d'ambition (1-10) : ",      1, 10)

    attributs = {
        "courage":      courage,
        "intelligence": intelligence,
        "loyaute":      loyaute,
        "ambition":     ambition
    }

    personnage = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(personnage)
    return personnage


def recevoir_lettre():
    print("\n" + "~" * 50)
    print("Une chouette apporte une lettre scellee...")
    print("\n<< Cher eleve,")
    print("Nous avons le plaisir de vous informer que vous")
    print("avez ete admis a l'ecole de sorcellerie de Poudlard ! >>")
    print("~" * 50)

    choix = demander_choix(
        "\nAcceptez-vous cette invitation ?",
        ["Oui, bien sur !", "Non, je prefere rester avec l'oncle Vernon..."]
    )

    if choix == "Non, je prefere rester avec l'oncle Vernon...":
        print("\nL'oncle Vernon pousse un cri de joie.")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)

    print("\nExcellent ! L'aventure commence !")


def rencontrer_hagrid(personnage):
    print("\n" + "-" * 50)
    print("Un homme immense frappe a la porte...")
    print("-" * 50)
    print("\nHagrid : 'Salut " + personnage["Prenom"] + " ! Je viens t'emmener")
    print("faire tes achats sur le Chemin de Traverse !'")

    choix = demander_choix("\nVoulez-vous suivre Hagrid ?", ["Oui", "Non"])

    if choix == "Non":
        print("\nHagrid sourit et vous entraine quand meme avec lui !")
    else:
        print("\nVous suivez Hagrid avec enthousiasme !")


def acheter_fournitures(personnage):
    catalogue = load_fichier("data/inventaire.json")
    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    print("\n" + "=" * 50)
    print("Bienvenue sur le Chemin de Traverse !")
    print("=" * 50)

    print("\nCatalogue des objets disponibles :")
    for num in catalogue:
        print("  " + num + ". " + catalogue[num][0] + " - " + str(catalogue[num][1]) + " galions")

    restants = []
    for o in obligatoires:
        restants.append(o)

    while len(restants) > 0:
        print("\nVous avez " + str(personnage["Argent"]) + " galions.")
        print("Objets obligatoires restants : " + ", ".join(restants))

        numero = demander_texte("Entrez le numero de l'objet a acheter : ")

        if numero not in catalogue:
            print("Numero invalide, reessayez.")
            continue

        nom_objet  = catalogue[numero][0]
        prix_objet = catalogue[numero][1]

        if nom_objet in personnage["Inventaire"]:
            print("Vous avez deja cet objet.")
            continue

        if personnage["Argent"] < prix_objet:
            print("Pas assez de galions !")
            peut = False
            for obj in restants:
                for n in catalogue:
                    if catalogue[n][0] == obj and personnage["Argent"] >= catalogue[n][1]:
                        peut = True
            if not peut:
                print("\nVous ne pouvez pas acheter les objets obligatoires. Fin du jeu.")
                exit(0)
            continue

        modifier_argent(personnage, -prix_objet)
        ajouter_objet(personnage, "Inventaire", nom_objet)
        print("Vous avez achete : " + nom_objet + " (-" + str(prix_objet) + " galions).")

        if nom_objet in restants:
            restants.remove(nom_objet)

    print("\nTous les objets obligatoires ont ete achetes !")

    # Animal de compagnie
    print("\nChoisissez votre animal de compagnie :")
    animaux   = ["Chouette (20 galions)", "Chat (15 galions)", "Rat (10 galions)", "Crapaud (5 galions)"]
    prix_anim = [20, 15, 10, 5]
    noms_anim = ["Chouette", "Chat", "Rat", "Crapaud"]

    print("Vous avez " + str(personnage["Argent"]) + " galions.")
    choix_anim = demander_choix("Quel animal voulez-vous ?", animaux)
    idx = animaux.index(choix_anim)

    if personnage["Argent"] < prix_anim[idx]:
        print("Pas assez de galions pour un animal. Vous partez sans compagnon.")
    else:
        modifier_argent(personnage, -prix_anim[idx])
        ajouter_objet(personnage, "Inventaire", noms_anim[idx])
        print("Vous avez choisi : " + noms_anim[idx] + " (-" + str(prix_anim[idx]) + " galions).")

    print("\nInventaire final :")
    afficher_personnage(personnage)


def lancer_chapitre_1():
    introduction()
    personnage = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(personnage)
    acheter_fournitures(personnage)
    print("\n" + "=" * 50)
    print("Fin du Chapitre 1 ! Votre aventure commence a Poudlard...")
    print("=" * 50)
    return personnage
