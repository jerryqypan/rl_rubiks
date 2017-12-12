from gym.envs.registration import register,make

register(
    id='rubiks-cross-v0',
    entry_point='gym_rubiks.envs:CrossEnv',

)
register(
    id='rubiks-2x2-5-v0',
    entry_point='gym_rubiks.envs:PocketCube5Env',
)

register(
    id='rubiks-2x2-7-v0',
    entry_point='gym_rubiks.envs:PocketCube7Env',
)
register(
    id='rubiks-2x2-8-v0',
    entry_point='gym_rubiks.envs:PocketCube8Env',
)
register(
    id='rubiks-2x2-10-v0',
    entry_point='gym_rubiks.envs:PocketCube10Env',
)
register(
    id='rubiks-2x2-11-v0',
    entry_point='gym_rubiks.envs:PocketCube11Env',
)
register(
    id='rubiks-2x2-100-v0',
    entry_point='gym_rubiks.envs:PocketCube100Env',
)