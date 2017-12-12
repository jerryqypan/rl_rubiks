import pycuber as pc
import numpy as np

faces = ['L','U','R','D','F','B']
colors = ['[r]','[y]','[o]','[w]','[g]','[b]']
possible_moves = ["R","R'","R2","U","U'","U2","F","F'","F2","D","D'","D2","B","B'","B2","L","L'","L2"]
opposite_sides = {
    0:2,
    1:3,
    2:0,
    3:1,
    4:5,
    5:4
}
direction_to_check = {
    0:{1:(1,0),3:(1,0),4:(1,0),5:(1,2)},
    1:{0:(0,1),2:(0,1),4:(0,1),5:(0,1)},
    2:{1:(1,2),3:(1,2),4:(1,2),5:(1,0)},
    3:{0:(2,1),2:(2,1),4:(2,1),5:(2,1)},
    4:{0:(1,2),1:(2,1),2:(1,0),3:(0,1)},
    5:{0:(1,0),1:(0,1),2:(1,2),3:(2,1)}
}
color_by_orientation = {
    0:{(0,1):1,(1,0):5,(1,2):4,(2,1):3},
    1:{(0,1):5,(1,0):0,(1,2):2,(2,1):4},
    2:{(0,1):1,(1,0):4,(1,2):5,(2,1):3},
    3:{(0,1):4,(1,0):0,(1,2):2,(2,1):5},
    4:{(0,1):1,(1,0):0,(1,2):2,(2,1):3},
    5:{(0,1):1,(1,0):2,(1,2):0,(2,1):3}
}
def cube2np(mycube):
    # transform cube object to np array
    # works around the weird data type used
    global faces
    global colors
    cube_np = np.zeros((6,3,3))
    for i,face in enumerate(faces):
        face_tmp = mycube.get_face(face)
        for j in range(3):
            for k in range(len(face_tmp[j])):
                caca = face_tmp[j][k]
                cube_np[i,j,k] = colors.index(str(caca))
    return cube_np
def check_finished(cube_np):
    for face in cube_np:
        color = face[0][0]
        if color != face[0][1] or color != face[1][0] or color != face[1][1]:
            return False
    return True

def cubeto2x2(cube_np):
    new_cube = np.zeros((6,2,2))
    for i,face in enumerate(cube_np):
        new_cube[i][0][0] = face[0][0]
        new_cube[i][0][1] = face[0][2]
        new_cube[i][1][0] = face[2][0]
        new_cube[i][1][1] = face[2][2]
    return new_cube

mycube = pc.Cube()
mycube("R U F")
print(check_finished(cubeto2x2(cube2np(mycube))))
# mycube("D U B L D U B' F B' L R2")
# print(mycube)
# mycube("B' L B2 D2 R2 F U' R U")
# print(mycube)
# np_cube = cube2np(mycube)
# #print(np_cube[0,[1,2]])
# success, val,correct_edges = checkYellowCross(np_cube)
# print(correct_edges)