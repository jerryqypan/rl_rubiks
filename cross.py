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
def checkCross(cube_np):
    #find a cross
    global opposite_sides
    global direction_to_check
    cross = False
    possible_crosses = []
    for i,face in  enumerate(cube_np):
        if face[0][1] == i and face[1][0] == i and face[1][2] == i and face[2][1] == i:
            possible_crosses.append(i)
    for i in possible_crosses:
        #print('i',i)
        faces_to_check = [j for j in range(6) if j != opposite_sides[i] and j!=i]
        is_edge_correct = True
        for j in faces_to_check:
            #print(cube_np[j,direction_to_check[i][j]])
            #print('j',j)
            if cube_np[j,direction_to_check[i][j][0],direction_to_check[i][j][1]] != j:
                is_edge_correct = False
                break
        if is_edge_correct == True:
            return True,i
    return False,-1
def checkYellowCross(cube_np):
    #find a cross
    global opposite_sides
    global direction_to_check
    faces_to_check = []
    correct_edges = []
    if cube_np[1][0][1] == 1:
        faces_to_check.append(5)

    if cube_np[1][1][0] == 1:
        faces_to_check.append(0)

    if cube_np[1][1][2] == 1:
        faces_to_check.append(2)
    if  cube_np[1][2][1] == 1:
        faces_to_check.append(4)
    is_edge_correct = True
    for j in faces_to_check:
        #print(cube_np[j,direction_to_check[i][j]])
        #print('j',j)
        if cube_np[j,direction_to_check[1][j][0],direction_to_check[1][j][1]] != j:
            is_edge_correct = False
        else:
            correct_edges.append(j)
    if len(faces_to_check)==4 and is_edge_correct == True:
        return True,1,faces_to_check
    return False,-1,correct_edges
def keep_yellow_edge(cube_np):
    global color_by_orientation
    global direction_to_check
    # yellow is 1
    vals_to_keep = []
    yellow_edges = []
    for i,face in enumerate(cube_np):
        if face[0][1] == 1:
            yellow_edges.append((i,0,1))
            vals_to_keep.append((i,0,1))
        if face[1][0] == 1:
            yellow_edges.append((i,1,0))
            vals_to_keep.append((i,1,0))
        if face[1][2] == 1:
            yellow_edges.append((i,1,2))
            vals_to_keep.append((i,1,2))
        if face[2][1] == 1:
            yellow_edges.append((i,2,1))
            vals_to_keep.append((i,2,1))
    for yellow in yellow_edges:
        center = color_by_orientation[yellow[0]][(yellow[1],yellow[2])]
        vals_to_keep.append((center,direction_to_check[yellow[0]][center][0],direction_to_check[yellow[0]][center][1]))
    new_cube = -1*np.ones(cube_np.shape)
    for coord in vals_to_keep:
        #print(coord)
        #print(cube_np[coord])
        new_cube[coord] = cube_np[coord]
    return new_cube

mycube = pc.Cube()
print(checkYellowCross(keep_yellow_edge(cube2np(mycube))))
# mycube("D U B L D U B' F B' L R2")
# print(mycube)
# mycube("B' L B2 D2 R2 F U' R U")
# print(mycube)
# np_cube = cube2np(mycube)
# #print(np_cube[0,[1,2]])
# success, val,correct_edges = checkYellowCross(np_cube)
# print(correct_edges)