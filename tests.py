from plateau import *
from parametres import * 

#quadruplets_possibles(NB_LIGNES, NB_COLONNES, PUISSANCE)

plateau=Plateau(NB_COLONNES,NB_LIGNES)
isFull= plateau.is_full()
print("Is the plateau full ? ", isFull)
#plateau.show()
#plateau.has_won()