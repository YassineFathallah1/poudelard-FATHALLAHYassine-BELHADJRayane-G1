import json


def demander_texte(message):
    while True:
        saisie = input(message).strip()
        if saisie:
            return saisie
        print("La saisie ne peut pas etre vide. Reessayez.")


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()
        if not saisie:
            print("Veuillez entrer un nombre.")
            continue

        debut = 1 if saisie[0] == '-' else 0
        if debut == len(saisie):
            print("Veuillez entrer un nombre entier valide.")
            continue

        valide = True
        for c in saisie[debut:]:
            if not ('0' <= c <= '9'):
                valide = False
                break

        if not valide:
            print("Veuillez entrer un nombre entier valide.")
            continue

        # Conversion manuelle sans int()
        negatif = saisie[0] == '-'
        chiffres = saisie[1:] if negatif else saisie
        nombre = 0
        for c in chiffres:
            nombre = nombre * 10 + (ord(c) - ord('0'))
        if negatif:
            nombre = -nombre

        if min_val is not None and nombre < min_val:
            print("Entrez un nombre entre " + str(min_val) + " et " + str(max_val) + ".")
            continue
        if max_val is not None and nombre > max_val:
            print("Entrez un nombre entre " + str(min_val) + " et " + str(max_val) + ".")
            continue

        return nombre


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print("  " + str(i + 1) + ". " + options[i])
    choix = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix - 1]


def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        return json.load(f)
