from data import *
from settings import * 
from algo import *

# VALEURS INITIALES 
count_victory = [0] * N
recomp_estimees = [0] * N
count = [0] * N

analysis(rendements_1, recomp_estimees, count, count_victory, UCB, T)