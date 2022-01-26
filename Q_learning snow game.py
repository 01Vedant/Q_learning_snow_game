import numpy as np
import gym 
import random 
import time
from IPython.display import clear_output

env = gym.make("FrozenLake-v1") # Create an environment
print(env.action_space)

action_space_size = env.action_space.n     # Number of Coloumns are equivalent to the action space environment
state_space_size = env.observation_space.n # Number of rows equivalent to the state space environment

q_table = np.zeros((state_space_size,action_space_size)) # Build the Q table and fill it with zeros
print(q_table)

num_episodes = 1000           # Total episodes
max_steps_per_episodes = 100  # Max steps per episodes
learning_rate = 0.1           # Learning rate
discount_rate = 0.99          # Discount rate
exploration_rate = 1          # Exploration rate
max_exploration_rate = 1      # Max exploration rate
min_exploration_rate = 0.01   # Min exploration rate
exploration_decay_rate = 0.001# Exploration rate decay

rewards_all_episodes = []     #Holds all the rewards from each episode

#Q learning algorithm
for episode in range(num_episodes): # This for loop contains everything that happens within a single episode
 state = env.reset()                # Resets the state of the environment to the starting state
 done = False                       # It keeps track whether or not the episode is finished
 rewards_current_episode = 0
 for step in range(max_steps_per_episodes): # This for loop contains everything that heppens in a single time step within each episode
      exploration_rate_threshold = random.uniform(0,1) # Exploration rate threshold is assigned a random number between zero and one
      if exploration_rate_threshold>exploration_rate:
          action = np.argmax(q_table[state, :])        # Chooses the action with the highest Q-value
      else:
          action=env.action_space.sample()             # Chooses random action
     
      new_state, reward, done, info = env.step(action) # pass the action using step object
   
  #Updated Q table for Q(s,a)
      q_table[state,action] = q_table[state,action] * (1-learning_rate) + learning_rate * (reward+discount_rate*np.max(q_table[new_state,:]))   # Update the q value for the state action pair

      state = new_state    # Set the current state to the new state
      rewards_current_episode+= reward # Update the reward
      if done == True:    # if last action ended the episode then break from the loop
          break
      
        
#Exploration rate decay
exploration_rate= min_exploration_rate + (max_exploration_rate-min_exploration_rate) * np.exp(-exploration_decay_rate*episode)  # Update the exploration rate

rewards_all_episodes.append(rewards_current_episode)     # Append the rewards


 # Calculate and print the average reward per thousand episodes
rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes),num_episodes/1000) 
count = 1000
print("Average reward per thousand episodes")
for r in rewards_per_thousand_episodes: 
    print(count,":",str(sum(r/100)))
    count+=1000
    
#updated Q table
print("\n\n*******Q-table*******\n")
print(q_table)


for episode in range(3):
  state = env.reset()
  done = False
  print("***** episode ", episode+1, "******\n\n\n\n")
  time.sleep(1)

  for step in range(max_steps_per_episodes):
    clear_output(wait = True)
    env.render()
    time.sleep(0.3)

    action = np.argmax(q_table[state,:])
    new_state, reward, done, info=env.step(action)

    if done:
      clear_output(wait = True)
      env.render()
      if reward == 1:
        print("You reached the goal")
        time.sleep(3)
      else:
          print("You fell through a hole")
          time.sleep(3)
          clear_output(wait=True) 
          break

    state = new_state

env.close()     
        
      
