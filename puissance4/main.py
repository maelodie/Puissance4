from plateau import *
from player import *
from analyse import *

joueur1 = Player(ID_JOUEUR1, 0) #joue aléatoirement
joueur2 = Player(ID_JOUEUR2, 1) #joue MC

analyse(joueur1, joueur2, 10)
# tab_1= [0] * 43
# tab_2= [0] * 43
# for i in range(1000):
# plateau = Plateau(NB_COLONNES, NB_LIGNES) 
# res = plateau.run(joueur1, joueur2)
#     if res[0] == 1:
#         tab_1[res[1]] += 1
#     # if res[0] == -1:
#     #     tab_2[res[1]] += 1
            
# print("Joueur 1 ", tab_1)
# print("Joueur 2 ", tab_2)
# print(plateau.show())

