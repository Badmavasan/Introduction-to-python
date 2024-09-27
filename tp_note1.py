"""
Nom :
Prenom :
Contexte : Système de gestion d'un réseau de transports urbains

Dans ce contexte, vous êtes responsable du développement d'un système de gestion d'un réseau de transports urbains
dans une grande métropole. Ce réseau comprend différents types de véhicules (bus, tramways, métros), chaque véhicule
ayant des trajets, des horaires, et des passagers à gérer. Vous devez écrire des fonctions pour organiser, simuler et
gérer ces aspects complexes du réseau.
1. Fonction : Gestion des trajets de véhicules

Description de la tâche :
Écrivez une fonction gerer_trajets(liste_vehicules) qui prend en entrée une liste de dictionnaires représentant des
véhicules du réseau de transport. Chaque véhicule a les informations suivantes :

    type_vehicule (par exemple, "bus", "tramway", "métro").
    capacite (nombre de passagers que le véhicule peut transporter).
    trajets (une liste de trajets, chaque trajet étant un tuple de la forme (station_depart, station_arrivee, duree)).

La fonction doit classer les véhicules selon les critères suivants :

    En premier, par leur type (les bus, puis les tramways, puis les métros).
    Ensuite, par leur capacité (en ordre décroissant).
    Enfin, par la durée totale des trajets (somme des durées de tous les trajets).

La fonction retourne une liste de véhicules triés.
"""

def gerer_trajets(liste_vehicules):
    #TODO
    pass # A enlever

"""
2. Fonction : Simulation de la capacité des véhicules

Description de la tâche :
Écrivez une fonction simuler_capacite(vehicule, passagers) qui simule la gestion des passagers pour un véhicule 
spécifique. La fonction prend en entrée un dictionnaire représentant un véhicule et un nombre de passagers qui tentent 
de monter à bord. Le véhicule a les informations suivantes :

    type_vehicule.
    capacite.
    passagers_actuels (le nombre actuel de passagers à bord).

La fonction doit gérer les conditions suivantes :

    - Si le nombre de passagers actuels est inférieur à la capacité, ajoutez les nouveaux passagers à bord jusqu’à ce 
    que le véhicule soit plein.
    - Si le nombre de passagers dépasse la capacité, seuls les passagers pouvant entrer dans le véhicule sont acceptés.
    - La fonction retourne le nombre de passagers refusés (ceux qui n’ont pas pu monter).
"""


def simuler_capacite(vehicule, passagers):
    # TODO
    pass # A enlever


"""
3. Fonction : Mise à jour des horaires des trajets

Description de la tâche :
Écrivez une fonction mettre_a_jour_horaires(trajets, retard) qui met à jour les horaires des trajets pour un véhicule 
donné. La fonction prend en entrée une liste de trajets (chaque trajet étant un tuple de la forme (station_depart, 
station_arrivee, heure_depart, heure_arrivee)) et un nombre représentant le retard en minutes.

La fonction doit ajouter le retard à l'heure de départ et à l'heure d'arrivée de chaque trajet. La fonction retourne la 
nouvelle liste de trajets avec les horaires mis à jour.
"""

def mettre_a_jour_horaires(trajets, retard):
    #TODO
    pass # A enlever


# Exemple de véhicules (Données pour la fonction 1)
vehicules = [
    {'type_vehicule': 'bus', 'capacite': 50, 'trajets': [('A', 'B', 20), ('B', 'C', 30)]},
    {'type_vehicule': 'tramway', 'capacite': 120, 'trajets': [('D', 'E', 25), ('E', 'F', 35)]},
    {'type_vehicule': 'métro', 'capacite': 200, 'trajets': [('G', 'H', 15), ('H', 'I', 20)]},
]

# Tester fonction 1
print(gerer_trajets(vehicules))

# Exemple d'un véhicule et simulation pour la fonction 2
vehicule = {'type_vehicule': 'bus', 'capacite': 50, 'passagers_actuels': 40}
passagers = 15

# Tester fonction 2
print(simuler_capacite(vehicule, passagers))

# Exemple de trajets et mise à jour pour la fonction 3
trajets = [('A', 'B', 800, 830), ('B', 'C', 840, 900), ('C', 'D', 910, 940)]
retard = 10

# Tester fonction 3
print(mettre_a_jour_horaires(trajets, retard))
