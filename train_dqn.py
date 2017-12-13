import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import gym_rubiks
import numpy as np
import argparse

def setup_dqn(env):
    n_actions = 9
    obs_size = 24
    q_func = chainerrl.q_functions.FCStateQFunctionWithDiscreteAction(
        obs_size, n_actions,
        n_hidden_layers=2, n_hidden_channels=2000)
    q_func.to_gpu(0)
    optimizer = chainer.optimizers.Adam(eps=1e-2)
    optimizer.setup(q_func)
    gamma = 0.95
    explorer = chainerrl.explorers.LinearDecayEpsilonGreedy(
        0.3, 0.01, 10000, random_action_func=env.action_space.sample)
    replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=10 ** 6)
    phi = lambda x: x.astype(np.float32, copy=False)
    agent = chainerrl.agents.DQN(
        q_func, optimizer, replay_buffer, gamma, explorer,
        replay_start_size=500, update_interval=1,
        target_update_interval=100, phi=phi)
    return agent


def train_constant(shuffle, model='', n_episodes=10000):
    env = gym_rubiks.make("rubiks-2x2-"+str(100) + '-v0')
    agent = setup_dqn(env)
    total_episodes = n_episodes
    max_episode_len = 15
    reward_array = []
    qval_array = []
    if model != '':
        agent.load('agent_'+str(shuffle)+'_10000')
        #total_episodes += int(model.split('_')[2])
        total_episodes += 10000
    for i in range(1, n_episodes + 1):
        obs = env.reset()
        reward = 0
        done = False
        R = 0  # return (sum of rewards)
        t = 0  # time step
        Q = 0
        while not done and t < max_episode_len:
            # Uncomment to watch the behaviour
            # env.render()
            action,q_value = agent.act_and_train(obs, reward) #changed function to return q value
            obs, reward, done, _ = env.step(action)
            R += reward
            t += 1
            Q += q_value
        reward_array.append(R)
        qval_array.append(Q/t)
        if i % 1000 == 0:
            print('episode:', i,
                  'R:', R,
                  'statistics:', agent.get_statistics())
        agent.stop_episode_and_train(obs, reward, done)
    print('Finished.')
    save_dir = 'agent_'+str(shuffle)+'_'+str(total_episodes)
    agent.save(save_dir)
    np.save('./'+save_dir+'/'+'rewards.npy',reward_array)
    np.save('./' + save_dir + '/' + 'qval.npy', qval_array)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train DQN to Solve 2x2x2 Rubiks Cube')
    parser.add_argument('-s', '--shuffle', help='Number of moves when shuffling cube', default='11')
    args = parser.parse_args()
    n_shuffle = int(args.shuffle)
    train_constant(n_shuffle)