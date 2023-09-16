from partie1 import *
from parametres import * 

#quadruplets_possibles(NB_LIGNES, NB_COLONNES, PUISSANCE)

plateau1 = Plateau(NB_LIGNES, NB_COLONNES)
joueur1 = Player(ID_JOUEUR1)
plateau1.play(0, joueur1)
plateau1.play(0, joueur1)
plateau1.play(4, joueur1)
plateau1.show()
