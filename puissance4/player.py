from plateau import *
from parametres import N
import random
from copy import deepcopy

class Player:
    """
    Classe qui représente un joueur du jeu Puissance 4
    """
    def __init__(self, id, mode):
        self.id = id  # (1 ou -1)
        self.mode= mode #(0 : aléatoire ou 1 : Monte-carlo)
    
    def play(self, plateau : Plateau):
        """
        Renvoie le coup à jouer pour le joueur
        Si mode vaut 0, on génere une colonne aléatoire
        Si mode vaut 1, le joueur utilise l'algorithme Monte-Carlo
        """

        if self.mode==0 :
            player_action = random.choice(plateau.possible_actions)
            plateau.play(player_action,self)

        if self.mode == 1 :
            player_action = self.monte_Carlo_play(plateau)
            plateau.play(player_action,self)

    def monte_Carlo_play(self, etat : Plateau) :
        """
        Renvoie le coup à jouer en utilisant l'algorithme de Monte Carlo
        """

        #Initialiser le tableau qui compte le nombre de jeu gagné avec une certaine colonne comme premier coup
        victory_count = np.zeros(etat.nb_colonnes, dtype=int)
        #Initialiser le tableau qui compte le nombre de fois une colonne a été tiré aléatoirement
        column_count = np.zeros(etat.nb_colonnes, dtype=int)

        #Simuler l'expérience N fois
        for i in range(N) :
            plateau_MC = deepcopy(etat)                          #Copier l'état actuel du plateau
            action =  random.choice(plateau_MC.possible_actions) #Tirer un premier coup aléatoirement
            column_count[action] += 1                            #Mettre à jour le compteur pour la colonne tirée
            plateau_MC.play(action, self)                        #Jouer le premier coup dans la simulation Monte Carlo

            # Mettre à jour le tour des joueurs Monte Carlo
            if self.id == ID_JOUEUR1 :
                plateau_MC.tour = ID_JOUEUR2
                joueur1 = Player(ID_JOUEUR2, 0)
            else :
                joueur1 = Player(ID_JOUEUR1, 0)

            joueur2 = Player(self.id, 0)
            res = plateau_MC.run(joueur1, joueur2) #Resultat de la partie jouée aléatoirement avec comme premier coup 'action'

            if res == self.id :     #Mettre à jour le tableau de victoire si le jeu est gagné
                victory_count[action] += 1 

        res_MC = np.divide(victory_count, column_count) #Calculer le nombre de victoire par rapport au nombre de tirage
      
        #Retourner le coups qui favorise le plus de victoire
        final_action = res_MC.argmax()

        if final_action in plateau_MC.possible_actions :  #vérifier que la colonne n'est pas pleine
            return final_action
        else :
            final_action  = correctAction(plateau_MC.possible_actions, res_MC, final_action)
            return final_action

def correctAction(poss_actions, res_MC, final_action) : 
    """
    Choisi la colonne la plus optimale parmi celles qui ne sont pas pleines
    """
    while final_action not in poss_actions :
        res_MC[final_action] = -1
        final_action = res_MC.argmax()
    return final_action


