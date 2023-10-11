import numpy as np
import pandas as pd
from parametres import *

class Plateau: 
    """
    Classe qui représente le plateau du jeu Puissance 4
    """

    #Attributs statiques
    w_combos = quad_list(NB_LIGNES, NB_COLONNES, PUISSANCE) #liste des quadruplets gagnants
    def __init__(self, nb_colonnes, nb_lignes):
        #Attributs de classe
        self.plateau = np.zeros((nb_lignes, nb_colonnes), dtype=int)
        self.filled_cases = np.zeros(NB_COLONNES, dtype=int) #nb de lignes occupées par colonne
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.running = True 
        self.tour = 1
        self.end = 0
        self.possible_actions = [0,1,2,3,4,5,6] #colonne qu'on peut jouer
        self.nb_coups = 0
    
    def reset(self):
        """
        Réinitialise le plateau
        """
        self.plateau = np.zeros((NB_LIGNES, NB_COLONNES) , dtype = int)
  
    def show(self):
        """ 
        Affiche le plateau de dimensions nb_lignes  x nb_colonnes
        """
        data = self.plateau
        df = pd.DataFrame(data)
        print("Voici un visuel du plateau")
        print(df)

    def is_full(self) :
        """"
        Renvoie True si le plateau est complet, False sinon
        """
        return np.all(self.plateau != 0)
    
    def play(self, x, joueur):
        """
        Permet au joueur de placer un jeton dans la colonne x
        """
        #Cette ligne permet de placer le jeton sur la première ligne libre (filled_cases étant les lignes occupées)
        y = (NB_LIGNES - 1) - self.filled_cases[x]
        self.filled_cases[x] += 1
        self.plateau[y,x] = joueur.id
        self.nb_coups += 1

        if self.filled_cases[x]>=self.nb_lignes and  x in self.possible_actions :
            self.possible_actions.remove(x)
 
    def has_won(self):
        """
        Renvoie (True,1) si le joueur 1 a gagné, (True,-1) si le joueur 2 a gagné, (False, 0) sinon.
        """
        combo = []
        for quad in self.w_combos:
            combo = [self.plateau[x][y] for x,y in quad] #recupere l'indice (1, -1 ou 0) des cases pour l'ensemble des quadruplets gagnants

            #Verifie si le joueur 1 a aligné 4 jetons
            if all(item == ID_JOUEUR1 for item in combo) :
                return (True, 1)
            
            #Verifie si le joueur 2 a aligné 4 jetons
            if all(item == ID_JOUEUR2 for item in combo):
                return (True, -1)
        return (False, 0)
    
    def run(self, joueur1, joueur2) : 
        """
        Permet de jouer une partie entre le joueur 1 et le joueur 2 : ils jouent à tour de rôle tant que la partie n'est pas finie.
        Elle renvoie 1 ou -1 selon la victoire du joueur 1 ou 2, et 0 en cas de nul.
        Si mode vaut 0, on génere une colonne aléatoire
        Si mode vaut 1, on utilise l'algorithme de Monte-carlo pour choisir une colonne
        """
        while self.running :
            if self.tour == 1 :
                joueur1.play(self)
                self.tour = -1
                if self.is_finished():
                    break

            if self.tour == -1 :
                joueur2.play(self)
                self.tour = 1
                if self.is_finished():
                    break

        return(self.end, self.nb_coups)

    def is_finished(self) :
        """
        Renvoie True si un des deux joueurs a gagné ou si le plateau est complet et termine la partie en cours
        """
        has_won = self.has_won()
        if has_won[0] :      #Vérifie si un joueur a gagné
            self.running = False
            self.end = has_won[1]
            return True
        
        if self.is_full() :   #Vérifie si le plateau est complet
            self.running = False
            return True

