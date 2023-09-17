from parametres import NB_COLONNES, NB_LIGNES, PUISSANCE

def quadruplets_colonnes(x, y, puissance, my_list):
    """
        Cette fonction calcule toutes les combinaisons gagnantes de colonnes
    """
    for i in range(x) :
        for j in range(y - puissance + 1):
            my_list.append(((i,j),(i,j+1),(i,j+2),(i,j+3)))

def quadruplets_lignes(x, y, puissance, my_list):
    """
        Cette fonction calcule toutes les combinaisons gagnantes de lignes
    """
    for i in range(y) :
        for j in range(x - puissance + 1):  
            my_list.append(((j,i),(j+1,i),(j+2,i),(j+3,i)))
            
     
def quadruplets_diagonales(x, y, puissance, my_list) :
    """
        Cette fonction calcule toutes les combinaisons gagnantes de diagonales
        Pour plus d'explication, lire les fonctions quad_diagonales_droit et quad_diagonales_gauche
        qui sont les deux parties de cette fonction. En effet, pour éviter le surplus de boucle et
        améliorer la complexité, elles ont été combinées
    """
    for i in range(x) :
        for j in range(y):
            if j+puissance <= y  and i+puissance <= x :
                my_list.append(((i,j),(i+1,j+1),(i+2,j+2),(j+3,j+3)))
            if j - puissance >= -1 and i + puissance <= x:
                my_list.append(((i,j),(i+1,j-1),(i+2,j-2),(j+3,j-3)))

"""
def quad_diagonales_droit(x, y, puissance, my_list):
    for i in range(x):
        for j in range(y):
            if j+puissance <= y  and i+puissance <= x :
                my_list.append(((i,j),(i+1,j+1),(i+2,j+2),(j+3,j+3)))

def quad_diagonales_gauche(x, y, puissance, my_list):
    for i in range(x) :
        for j in range(y):
            if j - puissance >= -1 and i + puissance <= x:
                my_list.append(((i,j),(i+1,j-1),(i+2,j-2),(j+3,j-3)))
"""

def quad_list(x, y, puissance) :
    my_list=[]
    quadruplets_lignes(x,y,puissance,my_list)
    quadruplets_colonnes(x,y,puissance,my_list)
    quadruplets_diagonales(x,y,puissance,my_list)
    for item in my_list:
        print(item)
    return my_list