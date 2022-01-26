# Q_learning_snow_game

## Gym
Gym is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API. Since its release, Gym's API has become the field standard for doing this.

Gym currently has two pieces of documentation: the documentation website and the FAQ.

## Installation
To install the base Gym library, use pip install gym.

This does not include dependencies for all families of environments (there's a massive number, and some can be problematic to install on certain systems). You can install these dependencies for one family like pip install gym[atari] or use pip install gym[all] to install all dependencies.

## API
The Gym API's API models environments as simple Python env classes. Creating environment instances and interacting with them is very simple- here's an example using the "CartPole-v1" environment:

import gym 

env = gym.make('CartPole-v1')


        
