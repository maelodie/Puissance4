from parametres import NB_COLONNES, NB_LIGNES, ID_JOUEUR1, ID_JOUEUR2, PUISSANCE, quad_list
from elements import Plateau, Player 

class Game : 
    def __init__(self):
        self.plateau = Plateau(NB_COLONNES, NB_LIGNES)
        self.joueur1 = Player(ID_JOUEUR1)
        self.joueur2 = Player(ID_JOUEUR2)
        self.running = True 
        self.tour = 1
        self.end = 0

    def run(self, mode) : 
        """
        Permet de jouer une partie entre le joueur 1 et le joueur 2 : ils jouent à tour de rôle tant que la partie n'est pas finie.
        Elle renvoie 1 ou -1 selon la victoire du joueur 1 ou 2, et 0 en cas de nul.
        Si mode vaut 0, l'utilisateur saisie le colonne souhaitée du prochain coup via la ligne de commande
        Si mode vaut 1, on génere une colonne aléatoire
        """
        while self.running :
            if self.tour == 1 :
                self.joueur1.play(self.plateau, mode)
                self.tour = 2
                if self.is_finished():
                    break

            if self.tour == 2 :
                self.joueur2.play(self.plateau, mode)
                self.tour = 1
                if self.is_finished():
                    break

        return self.end

    def is_finished(self) :
        has_won = self.plateau.has_won()
        if has_won[0] :
            self.running = False
            self.end = has_won[1]
            return True
        if self.plateau.is_full() :
            print("Le plateau est complet ! ")
            self.running = False
            return True


        

