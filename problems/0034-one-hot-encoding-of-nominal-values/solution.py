import numpy as np
import pandas as pd

def to_categorical(x, n_col=None):
	# Your code here
	if n_col == None:
		n_col = np.max(x) + 1

	empty = np.zeros((len(x),n_col)) #tuple a l'interieur de np.zeros pour avoir une matrice avec m ligne et n colonne

	# np.arange(len(x)) va prendre x et rendre liste [0,1,2,3,4] si len(x) = 4 par exemple, 	
	#empty[ligne, colonne]
	empty[np.arange(len(x)), x] = 1
	# en prenant la position de x apparier avec son nombre, ca va donner quelque chose comme ca 
	#	Liste A (lignes) :  [0,  1,  2,  3,  4]
	#	Liste B (colonnes): [0,  1,  2,  1,  0]
    #                 ↓   ↓   ↓   ↓   ↓
	#	Paires (ligne, col): (0,0) (1,1) (2,2) (3,1) (4,0)

	return empty


	