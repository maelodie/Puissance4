from plateau import *
import random

class Player:

    def __init__(self, id, mode):
        self.id = id
        self.mode= mode
    
    def play(self, plateau : Plateau, mode):
        """
        Renvoie le coup à jouer pour le joueur
        Si mode vaut 0, on génere une colonne aléatoire
        Si mode vaut 1, le joueur utilise l'algorithme Monte-Carlo
        """
        if self.id == ID_JOUEUR1:
            print("C'est le tour du Joueur 1")
        elif self.id == ID_JOUEUR2:
            print("C'est le tour du Joueur 2")

        if self.mode==0 :
            player_action = random.choice(plateau.possible_actions)
            print("Le coup à jouer est la colonne ", player_action)
            plateau.play(player_action,self)

        if mode == 1 :
            player_action =self.monte_carlo(plateau, self)
            print("Le coup à jouer est la colonne ", player_action)
            plateau.play(player_action,self)

