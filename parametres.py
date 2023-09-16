NB_COLONNES = 7
NB_LIGNES = 6
PUISSANCE = 4
ID_JOUEUR1 = 1
ID_JOUEUR2 = -1

#Fonction pour la construction des combinaisons gagnantes:
def quadruplets_colonnes(x, y, puissance, my_list):
    for i in range(x) :
        for j in range(y - puissance + 1):
            my_list.append(((j,i),(j,i+1),(j,i+2),(j,i+3)))

def quadruplets_lignes(x, y, puissance, my_list):
    for j in range(y) :
        for i in range(x - puissance + 1):  
            my_list.append(((i,j),(i+1,j),(i+2,j),(i+3,j)))
            
        
def quadruplets_diagonales(x, y, puissance, my_list) :
    for i in range(x) :
        for j in range(y):
            if j+puissance <= y  and i+puissance<= x :
                my_list.append(((i,j),(i+1,j+1),(i+2,j+2),(j+3,j+3)))
            if j - puissance >= -1 and i + puissance <= x:
                    my_list.append(((i,j),(i+1,j-1),(i+2,j-2),(j+3,j-3)))
    
def quad_list(x, y, puissance) :
    my_list=[]
    quadruplets_lignes(x,y,puissance,my_list)
    quadruplets_colonnes(x,y,puissance,my_list)
    quadruplets_diagonales(x,y,puissance,my_list)
    for item in my_list:
        print(item)
