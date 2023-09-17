def quad_lignes(x, y, puissance):
    my_list = list()

    for i in range(y+1):
        for i in range(x - puissance +  1):
            my_list.append(((i,0),(i+1,0),(i+2,0),(i+3,0)))
    
    return my_list
            

for item in quad_lignes(7, 6, 4):
    print(item)