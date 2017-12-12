import random
import numpy as np
import pycuber as pc

move = ["R","R'","R2","U","U'","U2","F","F'","F2","D","D'","D2","B","B'","B2","L","L'","L2"]
shuffle = ' '.join(np.random.choice(move,20))
cube = pc.Cube()
cube(shuffle)
print(cube)