NB_COLONNES = 7 #x
NB_LIGNES = 6 #y
PUISSANCE = 4
ID_JOUEUR1 = 1
ID_JOUEUR2 = -1

#Fonction pour la construction des combinaisons gagnantes:
def printlist(list):
    for item in list:
        print(item)

def quadruplets_colonnes(x, y, puissance, my_list):
    for i in range(x + 1) :
        for j in range(y - puissance + 1):
            my_list.append(((j,i),(j,i+1),(j,i+2),(j,i+3)))

def quadruplets_lignes(x, y, puissance):
    my_list = list()
    for j in range(y + 1) :
        for i in range(x - puissance + 1):  
            my_list.append(((i,0),(i+1,0),(i+2,0),(i+3,0)))
    return my_list
            
        
def quadruplets_diagonales(x, y, puissance, my_list) :
    for i in range(x) :
        for j in range(y):
            if j+puissance < y  and i+puissance< x :
                my_list.append(((i,j),(i+1,j+1),(i+2,j+2),(j+3,j+3)))
            if j - puissance >= -1 and i + puissance <= x:
                    my_list.append(((i,j),(i+1,j-1),(i+2,j-2),(j+3,j-3)))
    
def quad_list(x, y, puissance) :
    for item in quadruplets_lignes(NB_COLONNES, NB_LIGNES, PUISSANCE):
        print(item)
    print("---------------------")
