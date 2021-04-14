from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')

    # Connection avec la database et la collection produit
    produitDB = client['tpmongodb']
    c = produitDB['produit']

    # Création des différents produits
    produit1 = {'_id': 'ac3',
                "type": "Phone",
                "price": 600,
                "name": "AC3 Phone",
                "rating": 3.8,
                }

    produit2 = {'_id': 'ac7',
                "type": "Phone",
                "price": "900",
                "name": "AC7 Phone",
                "rating": 4.5,
                }

    produit3 = {'_id': 'ac9',
                "type": "Phone",
                "price": 1200,
                "name": "AC9 Phone",
                "rating": 4.8,
                }

    produits = [produit1, produit2, produit3]

    # Création du stock de l'inventaire
    inventaireProduit = {'AC3': 40,
                         'AC7': 30,
                         'AC9': 20}


    # Création des commandes selon les produit
    commande = {'AC3': 7,
                'AC7': 10,
                'AC9': 2,
                }


    # Création des différentes caisses et produits vendus par caisse
    caisse1 = {'_id': 'caisse1',
               "sales": [3, 3, 0],
               }

    caisse2 = {'_id': 'caisse2',
               "sales": [4, 7, 2],
               }

    # Question 1 : Combien de produits ont été vendus hier pour la Caisse 1 ?

    pipe = [{'$addFields': {'_id': caisse1, 'totalsales': {'$sum': 'sales'}}}]
    sales.aggregate(pipeline=pipe)

    print(Elements with aggregation)

    #Question 2 : Combien de produits (identifiés par un identifiant que vous choisirez), toutes caisses confondues, ont été vendus hier ?

    pipe = [{'$addFields': {'_id': None, 'totalsales': {'$sum': 'sales'}}}]
    sales.aggregate(pipeline=pipe)

    print(Elements with aggregation)

    #Question 3 : Après une journée de ventes, quels sont les produits en rupture de stock ?



