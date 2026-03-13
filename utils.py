# Fonctions utilitaires pour le reporting des produits

def print_summary(products):
    total = len(products)
    print(f"Nombre total de produits : {total}\n")

    # Afficher les 3 premiers produits
    print("3 premiers produits :")
    for p in products[:3]:
        print(f"{p['name']} - ${p['price']} - {p['rating']} étoiles")
    print()

    # Produit le moins cher
    if products:
        cheapest = min(products, key=lambda x: x['price'])
        print(f"Produit le moins cher : {cheapest['name']} - ${cheapest['price']}")

        # Produit le plus cher
        most_expensive = max(products, key=lambda x: x['price'])
        print(f"Produit le plus cher : {most_expensive['name']} - ${most_expensive['price']}")