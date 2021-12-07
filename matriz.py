import numpy as np
from fractions import Fraction
from itertools import permutations
matriz = np.linalg.det(np.array([[1 ,3 ,4 ],[3 ,1 ,5 ],[4 ,5 ,1 ]]))
S1 = np.array([[1*2,5],[4*2,-1*5]])
S2 = np.array([13,7])
solu = np.linalg.solve(S1,S2)
xy = 'X:'+str(solu[0])+ '  Y:' +str(solu[1])
#print(xy)
#print(matriz)

fraM = Fraction(4/36).limit_denominator()
print(round(float(fraM*100),2),fraM)
fraX = Fraction(10 * (1/6)**2 * (5/6)**3).limit_denominator()
print(round(float(fraX*100),2),fraX)
var = [1,2,3,4]
permsList = set(permutations(var,4))
lista = len(permsList)
print(permsList,lista)