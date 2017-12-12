import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pycuber as pc
import numpy as np
import random

def cube2np(mycube):
    # transform cube object to np array
    # works around the weird data type used
    faces = ['L', 'U', 'R', 'D', 'F', 'B']
    colors = ['[r]', '[y]', '[o]', '[w]', '[g]', '[b]']
    cube_np = np.zeros((6,3,3))
    for i,face in enumerate(faces):
        face_tmp = mycube.get_face(face)
        for j in range(3):
            for k in range(len(face_tmp[j])):
                caca = face_tmp[j][k]
                cube_np[i,j,k] = colors.index(str(caca))
    return cube_np
def cubeto2x2(cube_np):
    new_cube = np.zeros((6,2,2))
    for i,face in enumerate(cube_np):
        new_cube[i][0][0] = face[0][0]
        new_cube[i][0][1] = face[0][2]
        new_cube[i][1][0] = face[2][0]
        new_cube[i][1][1] = face[2][2]
    return new_cube
def check_finished(cube_np):
    for face in cube_np:
        color = face[0][0]
        if color != face[0][1] or color != face[1][0] or color != face[1][1]:
            return False
    return True

class PocketCube5Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.actions = ["R","R'","R2","U","U'","U2","F","F'","F2"]
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(0,5,(6,2,2))
        self.cube = pc.Cube()
        self.state = cubeto2x2(cube2np(self.cube))
        self.edgereward = []


    def _step(self, action):
        self.cube(self.actions[action])
        self.state = cubeto2x2(cube2np(self.cube))
        done = check_finished(self.state)
        reward = 100.0 if done else -1.0
        return self.state,reward,done,self.cube


    def _reset(self):
        done = True
        self.edgereward = []
        while done:
            shuffle = ' '.join(np.random.choice(self.actions, 5))
            self.cube = pc.Cube()
            self.cube(shuffle)
            self.state = cubeto2x2(cube2np(self.cube))
            done = check_finished(self.state)
        return self.state

    def _render(self, mode='human', close=False):
        #print(self.state)
        #return
        ...

class PocketCube7Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.actions = ["R","R'","R2","U","U'","U2","F","F'","F2"]
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(0,5,(6,2,2))
        self.cube = pc.Cube()
        self.state = cubeto2x2(cube2np(self.cube))
        self.edgereward = []


    def _step(self, action):
        self.cube(self.actions[action])
        self.state = cubeto2x2(cube2np(self.cube))
        done = check_finished(self.state)
        reward = 100.0 if done else -1.0
        return self.state,reward,done,self.cube


    def _reset(self):
        done = True
        self.edgereward = []
        while done:
            shuffle = ' '.join(np.random.choice(self.actions, 7))
            self.cube = pc.Cube()
            self.cube(shuffle)
            self.state = cubeto2x2(cube2np(self.cube))
            done = check_finished(self.state)
        return self.state

    def _render(self, mode='human', close=False):
        #print(self.state)
        #return
        ...

class PocketCube8Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.actions = ["R","R'","R2","U","U'","U2","F","F'","F2"]
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(0,5,(6,2,2))
        self.cube = pc.Cube()
        self.state = cubeto2x2(cube2np(self.cube))
        self.edgereward = []


    def _step(self, action):
        self.cube(self.actions[action])
        self.state = cubeto2x2(cube2np(self.cube))
        done = check_finished(self.state)
        reward = 100.0 if done else -1.0
        return self.state,reward,done,self.cube


    def _reset(self):
        done = True
        self.edgereward = []
        while done:
            shuffle = ' '.join(np.random.choice(self.actions, 8))
            self.cube = pc.Cube()
            self.cube(shuffle)
            self.state = cubeto2x2(cube2np(self.cube))
            done = check_finished(self.state)
        return self.state

    def _render(self, mode='human', close=False):
        #print(self.state)
        #return
        ...

class PocketCube10Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.actions = ["R","R'","R2","U","U'","U2","F","F'","F2"]
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(0,5,(6,2,2))
        self.cube = pc.Cube()
        self.state = cubeto2x2(cube2np(self.cube))
        self.edgereward = []


    def _step(self, action):
        self.cube(self.actions[action])
        self.state = cubeto2x2(cube2np(self.cube))
        done = check_finished(self.state)
        reward = 100.0 if done else -1.0
        return self.state,reward,done,self.cube


    def _reset(self):
        done = True
        self.edgereward = []
        while done:
            shuffle = ' '.join(np.random.choice(self.actions, 10))
            self.cube = pc.Cube()
            self.cube(shuffle)
            self.state = cubeto2x2(cube2np(self.cube))
            done = check_finished(self.state)
        return self.state

    def _render(self, mode='human', close=False):
        #print(self.state)
        #return
        ...

class PocketCube11Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.actions = ["R","R'","R2","U","U'","U2","F","F'","F2"]
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(0,5,(6,2,2))
        self.cube = pc.Cube()
        self.state = cubeto2x2(cube2np(self.cube))
        self.edgereward = []


    def _step(self, action):
        self.cube(self.actions[action])
        self.state = cubeto2x2(cube2np(self.cube))
        done = check_finished(self.state)
        reward = 100.0 if done else -1.0
        return self.state,reward,done,self.cube


    def _reset(self):
        done = True
        self.edgereward = []
        while done:
            shuffle = ' '.join(np.random.choice(self.actions, 11))
            self.cube = pc.Cube()
            self.cube(shuffle)
            self.state = cubeto2x2(cube2np(self.cube))
            done = check_finished(self.state)
        return self.state

    def _render(self, mode='human', close=False):
        #print(self.state)
        #return
        ...

class PocketCube100Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.actions = ["R","R'","R2","U","U'","U2","F","F'","F2"]
        self.action_space = spaces.Discrete(len(self.actions))
        self.observation_space = spaces.Box(0,5,(6,2,2))
        self.cube = pc.Cube()
        self.state = cubeto2x2(cube2np(self.cube))
        self.edgereward = []


    def _step(self, action):
        self.cube(self.actions[action])
        self.state = cubeto2x2(cube2np(self.cube))
        done = check_finished(self.state)
        reward = 100.0 if done else -1.0
        return self.state,reward,done,self.cube


    def _reset(self):
        done = True
        self.edgereward = []
        while done:
            shuffle = ' '.join(np.random.choice(self.actions, 100))
            self.cube = pc.Cube()
            self.cube(shuffle)
            self.state = cubeto2x2(cube2np(self.cube))
            done = check_finished(self.state)
        return self.state

    def _render(self, mode='human', close=False):
        #print(self.state)
        #return
        ...