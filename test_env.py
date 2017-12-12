import gym_rubiks


def main():
    env = gym_rubiks.make("rubiks-cross-v0")
    obs = env.reset()
    action = 0
    obs, r, done, info = env.step(action)
    print(obs)
if __name__ == '__main__':
    main()

