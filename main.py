from plateau import *
from player import *
from data import *

joueur1 = Player(ID_JOUEUR1, 0) #joue aléatoirement
joueur2 = Player(ID_JOUEUR2, 1) #joue MC

#plateau = Plateau(NB_COLONNES, NB_LIGNES) 

analyse(joueur1, joueur2, 50)
#plateau.run(joueur1, joueur2)

#print(plateau.show())
#print(plateau.has_won())
