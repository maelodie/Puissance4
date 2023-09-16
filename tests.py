from partie1 import *
from parametres import * 


print(quad_list(NB_LIGNES, NB_COLONNES, PUISSANCE))
plateau1 = Plateau(NB_LIGNES, NB_COLONNES)
joueur1 = Player(ID_JOUEUR1)
plateau1.show()
print(plateau1.has_won())
