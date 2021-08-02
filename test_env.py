import gym
import fetch

# create environment
env = gym.make('FetchReachRandomRobot-v2')

# initial reset
done = False
env.render()
env.reset()

# act until done
while not done:
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    obs = env.render()
