"""
TODO
Nom (complèt) :
Contexte:
Vous travaillez pour une entreprise qui gère un entrepôt de produits. Chaque produit a un nom, une quantité et un prix.
Votre tâche est de créer deux fonctions qui permettent de gérer et de suivre l'état du stock.

1. Vous devrez créer une fonction `ajouter_produits` qui permet d'ajouter une liste de nouveaux produits au stock.
Cette fonction prendra en entrée un dictionnaire représentant le stock actuel et une liste de nouveaux produits.
Si un produit existe déjà dans le stock, la quantité doit être mise à jour. Sinon, il doit être ajouté.

2. La deuxième fonction `afficher_stock` prendra le dictionnaire du stock et un prix minimum. Elle affichera uniquement
les produits qui ont un prix supérieur ou égal à ce prix, ainsi que leur quantité.

"""


# Fonction pour ajouter des produits au stock
def ajouter_produits(stock, nouveaux_produits):
    """
    TODO
    stock: dict, Dictionnaire du stock actuel {nom_produit: [quantité, prix]}
    nouveaux_produits: list, Liste de tuples représentant les nouveaux produits (nom_produit, quantité, prix)
    """



# Fonction pour afficher le stock selon un prix minimum
def afficher_stock(stock, prix_minimum):
    """
    TODO
    stock: dict, Dictionnaire du stock actuel {nom_produit: [quantité, prix]}
    prix_minimum: float, Le prix minimum à partir duquel afficher les produits
    """



# Exemple d'utilisation:
if __name__ == "__main__":
    # Dictionnaire représentant le stock actuel
    stock_actuel = #TODO: A definir au moins 3 produits dans le stock actuel

    # Liste des nouveaux produits à ajouter
    nouveaux_produits = #TODO: A definir au moins 3 nouveaux produits

    # Ajout des nouveaux produits
    ajouter_produits(stock_actuel, nouveaux_produits)

    # Afficher le stock avec les produits ayant un prix >= 100
    afficher_stock(stock_actuel, 100)
