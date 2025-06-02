# Fitness Data Generation and Agent Simulation

This project contains two Python scripts for generating synthetic fitness data and simulating a reinforcement learning-based fitness training agent.

## Files

### 1. Data_generation (2) (1).py
- **Purpose**: Generates synthetic fitness data for multiple users over a specified period.
- **Functionality**:
  - Creates user profiles with demographic data (age, sex, weight, fitness level, resting heart rate, and fitness goals).
  - Simulates daily workout sessions, including exercise repetitions, errors, and heart rate data based on user fitness levels.
  - Estimates daily calorie expenditure and updates fitness levels based on training frequency.
  - Saves data in JSON format for each user (`user_<id>_data.json`).
- **Key Features**:
  - Uses predefined heart rate ranges for different fitness levels and age groups.
  - Supports exercise parameters for various fitness categories (beginner, intermediate, athlete).
  - Generates heart rate data using a normal distribution based on MET values and user profiles.
  - Simulates a month of data with configurable start and end dates.

### 2. Fitness_agent (2) (1).ipynb
- **Purpose**: Implements a reinforcement learning agent to optimize workout plans.
- **Functionality**:
  - Defines a `FitnessAgent` class using Q-learning to select actions that adjust workout duration and difficulty.
  - Includes a `TrainingEnvironment` class to simulate workout sessions with performance-based rewards.
  - Runs simulations to train the agent over multiple episodes and visualizes total rewards using Matplotlib.
- **Key Features**:
  - Supports three difficulty levels (easy, intermediate, difficult) with corresponding exercise parameters.
  - Uses a Q-table for decision-making and an epsilon-greedy strategy for exploration.
  - Tracks performance metrics like total rewards and epsilon decay over episodes.

## Usage
1. **Data Generation**:
   - Run `Data_generation (2) (1).py` to generate synthetic fitness data.
   - Modify `start_date`, `end_date`, and `num_users` to customize the simulation period and number of users.
   - Output: JSON files (`user_<id>_data.json`) containing user profiles and daily records.

2. **Fitness Agent Simulation**:
   - Open and run `Fitness_agent (2) (1).ipynb` in a Jupyter Notebook environment.
   - Ensure required libraries (`numpy`, `matplotlib`, `random`, `collections`) are installed.
   - The script simulates 20 episodes and plots the total rewards per training session.

## Requirements
- Python 3.x
- Libraries: `numpy`, `pandas`, `matplotlib`, `random`, `json`, `os`, `datetime`, `collections`

## Notes
- Ensure the output directory is writable for JSON file generation.
- The fitness agent assumes a simplified state space and action set; adjust parameters like `num_states` or `num_actions` for more complex scenarios.
- The data generation script overwrites existing user data for the specified month unless the file is checked for prior existence.
