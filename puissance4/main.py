from plateau import *
from player import *
from analyse import *

#Initialiser les deux joueurs
joueur1 = Player(ID_JOUEUR1, 0) #joue aléatoirement
joueur2 = Player(ID_JOUEUR2, 1) #joue MC

#Initialiser une partie de Puissance 4
plateau = Plateau(NB_COLONNES, NB_LIGNES) 
res = plateau.run(joueur1, joueur2)
print(plateau.show())
print("Le joueur", res[0], "gagne avec", res[1], "coups !")

#Lancer une session d'analyse avec nb_parties répititions pour collecter des données
# nb_parties = 100
# analyse(joueur1, joueur2, nb_parties, 0)

