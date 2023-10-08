from plateau import *
from player import *
from analyse import *

joueur1 = Player(ID_JOUEUR1, 0) #joue aléatoirement
joueur2 = Player(ID_JOUEUR2, 0) #joue MC

analyse(joueur1, joueur2, 2000)
# plateau = Plateau(NB_COLONNES, NB_LIGNES) 

# plateau.run(joueur1, joueur2)

# print(plateau.show())
# print(plateau.has_won())
