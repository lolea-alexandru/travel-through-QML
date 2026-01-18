# The following code is based on the example from Gymnasium
# Source: https://gymnasium.farama.org/introduction/basic_usage/#your-first-rl-program
# ================= IMPORTS ================= #
import gymnasium as gym

# ================= ENVIRONMENT INTIALIZATION ================= #
env = gym.make("CartPole-v1", render_mode="human")

observation, info = env.reset()

print(f"Starting observation: {observation}")

# Init state
episode_over = False
total_reward = 0

while not episode_over:
    action = env.action_space.sample() # Random sampling

    observation, reward, terminated, truncated, info = env.step(action)

    total_reward += reward
    # episode_over = terminated or truncated

print(f"Episode finished! Total reward: {total_reward}")
env.close()