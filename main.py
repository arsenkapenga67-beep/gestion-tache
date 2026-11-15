# Amélioration finale
# Amélioration:projet binome 
taches = []

def afficher_menu():
    print("\n** GESTION DES TÂCHES **")
    print("1. Ajouter une tâche  2. Afficher  3. Rechercher  0. Quitter")

def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : titre vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")

def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        i = 0
        while i < len(taches):
            print(f"{i+1}. {taches[i]}")
            i += 1

def rechercher_tache():
    mot = input("Mot-clé : ").strip().lower()
    trouve = False
    i = 0
    while i < len(taches):
        if mot in taches[i].lower():
            print(f"{i+1}. {taches[i]}")
            trouve = True
        i += 1
    if not trouve:
        print("Aucune tâche trouvée.")

while True:
    afficher_menu()
    choix = input("Votre choix : ").strip()
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Erreur : choix invalide.")
