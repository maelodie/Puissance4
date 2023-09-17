NB_COLONNES = 7
NB_LIGNES = 6
PUISSANCE = 4
ID_JOUEUR1 = 1
ID_JOUEUR2 = -1

def quadruplets_colonnes(x, y, puissance, my_list):
    for k in range(x) :
        for j in range(y - puissance + 1):  
            quadruple = set()
            for i in range(j, j + puissance):
                quadruple.add((k, i))
            my_list.append(quadruple)
            print(quadruple)

def quadruplets_lignes(x, y, puissance, my_list):
    for j in range(y) :
        for k in range(x - puissance + 1):  
            quadruple = set()
            for i in range(k, k + puissance):
                quadruple.add((i, j))
            my_list.append(quadruple)
            print(quadruple)
        
def quadruplets_diagonales_droit(x, y, puissance, my_list) :
    for i in range(x) :
        for j in range(y):
            quadruple= set()
            if j+puissance <= y  and i+puissance<= x :
                for l in range(4) :
                    quadruple.add((i+l ,j + l))
                my_list.append(quadruple)
                print(quadruple)

def quadruplets_diagonales_gauche(x, y, puissance, my_list):
    for i in range(x):
        for j in range(y):
            quadruple = set()
            if j - puissance >= -1 and i + puissance <= x:
                for l in range(4):
                    quadruple.add((i + l, j - l))
                my_list.append(quadruple)
                print(quadruple)
    
def quad_list(x, y, puissance) :
    my_list=[]
    quadruplets_lignes(x,y,puissance,my_list)
    quadruplets_colonnes(x,y,puissance,my_list)
    quadruplets_diagonales_droit(x,y,puissance,my_list)
    quadruplets_diagonales_gauche(x,y,puissance,my_list)
    return my_list