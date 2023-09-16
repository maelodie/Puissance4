from parametres import NB_COLONNES, NB_LIGNES, ID_JOUEUR1, ID_JOUEUR2
from elements import Plateau, Player 

class Game : 
    def __init__(self):
        self.plateau = Plateau(NB_COLONNES, NB_LIGNES)
        self.joueur1 = Player(ID_JOUEUR1)
        self.joueur2 = Player(ID_JOUEUR2)
        self.running = True 


    def is_finished(self) :
        if self.joueur1.has_won() or self.joueur2.has_won() or self.plateau.is_full():
            self.running=True

#Avec ce constructeur, pour la fonction run, on fait while self.running et on appelle la focntion is_finished a la fin de la boucle pour la mise a jour de la condition
        

