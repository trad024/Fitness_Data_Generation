#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json
import datetime
from random import randint, choice
import numpy as np
import pandas as pd
import random
import datetime
import os
import datetime
import random


# In[9]:

#Resting heart rate data for men
male_data = {
    'Athlète': [(18, 25, (49, 55)), (26, 35, (49, 54)), (36, 45, (50, 56)), (46, 55, (50, 57)), (56, 65, (51, 56)), (65, 100, (50, 55))],
    'Excellente': [(18, 25, (56, 61)), (26, 35, (55, 61)), (36, 45, (57, 62)), (46, 55, (58, 63)), (56, 65, (57, 61)), (65, 100, (56, 61))],
    'Bonne': [(18, 25, (62, 65)), (26, 35, (62, 65)), (36, 45, (63, 66)), (46, 55, (64, 67)), (56, 65, (62, 67)), (65, 100, (62, 65))],
    'Au-dessus de la moyenne': [(18, 25, (66, 69)), (26, 35, (66, 70)), (36, 45, (67, 70)), (46, 55, (68, 71)), (56, 65, (68, 71)), (65, 100, (66, 69))],
    'Moyenne': [(18, 25, (70, 73)), (26, 35, (71, 74)), (36, 45, (71, 75)), (46, 55, (72, 76)), (56, 65, (72, 75)), (65, 100, (70, 73))],
    'En dessous de la moyenne': [(18, 25, (74, 81)), (26, 35, (75, 81)), (36, 45, (76, 82)), (46, 55, (77, 83)), (56, 65, (76, 81)), (65, 100, (74, 79))],
    'Mauvaise': [(18, 25, (82, 100)), (26, 35, (82, 100)), (36, 45, (83, 100)), (46, 55, (84, 100)), (56, 65, (82, 100)), (65, 100, (80, 100))]
}

#Resting heart rate data for women
female_data = {
    'Athlète': [(18, 25, (56, 60)), (26, 35, (54, 59)), (36, 45, (54, 59)), (46, 55, (54, 60)), (56, 65, (54, 59)), (65, 100, (54, 59))],
    'Excellente': [(18, 25, (61, 65)), (26, 35, (60, 64)), (36, 45, (60, 64)), (46, 55, (61, 65)), (56, 65, (60, 64)), (65, 100, (60, 64))],
    'Bonne': [(18, 25, (66, 69)), (26, 35, (65, 68)), (36, 45, (65, 69)), (46, 55, (66, 69)), (56, 65, (65, 68)), (65, 100, (65, 68))],
    'Au-dessus de la moyenne': [(18, 25, (70, 73)), (26, 35, (69, 72)), (36, 45, (70, 73)), (46, 55, (70, 73)), (56, 65, (69, 73)), (65, 100, (69, 72))],
    'Moyenne': [(18, 25, (74, 78)), (26, 35, (73, 76)), (36, 45, (74, 78)), (46, 55, (74, 77)), (56, 65, (74, 77)), (65, 100, (73, 76))],
    'En dessous de la moyenne': [(18, 25, (79, 84)), (26, 35, (77, 82)), (36, 45, (79, 84)), (46, 55, (78, 83)), (56, 65, (78, 83)), (65, 100, (77, 84))],
    'Mauvaise': [(18, 25, (85, 100)), (26, 35, (83, 100)), (36, 45, (85, 100)), (46, 55, (84, 100)), (56, 65, (84, 100)), (65, 100, (84, 100))]
}
def get_resting_heart_rate(age, sex, fitness_level):
    data = male_data if sex == 'male' else female_data
    for age_range in data[fitness_level]:
        if age_range[0] <= age <= age_range[1]:
            return random.randint(*age_range[2])  # Retourne une valeur aléatoire dans la plage définie
    raise ValueError("Age or fitness level out of range")


def generate_individual_demographic_data(user_id):
    age = random.randint(18, 75)  # Génération d'un âge aléatoire entre 18 et 100 ans
    sex = random.choice(['male', 'female'])  # Sélection aléatoire du sexe
    weight = random.randint(50, 120)  # Génération d'un poids aléatoire entre 50 et 120 kg
    fitness_level = random.choice([
        'Athlète', 'Excellente', 'Bonne', 'Au-dessus de la moyenne', 
        'Moyenne', 'En dessous de la moyenne', 'Mauvaise'
    ])  # Sélection aléatoire du niveau de forme physique
    resting_heart_rate = get_resting_heart_rate(age, sex, fitness_level)
    goal = random.choice(['strength', 'weight loss', 'soft'])
    individual = {
        'user_id': user_id,
        'goal': goal,
        'age': age,
        'sex': sex,
        'weight': weight,
        'fitness_level': fitness_level,
        'resting_heart_rate': resting_heart_rate
    }
    return individual
exercise_params = {
    'Squat': {'debutant': (6, 16), 'intermediaire': (16, 28), 'sportif': (28, 50)},
    'Push-up': {'debutant': (2, 14), 'intermediaire': (14, 24), 'sportif': (24, 50)},
    'Jumping Jack': {'debutant': (10, 30), 'intermediaire': (30, 50), 'sportif': (50, 60)},
    'Situps': {'debutant': (3, 8), 'intermediaire': (8, 14), 'sportif': (14, 28)},
    'V-up': {'debutant': (2, 10), 'intermediaire': (10, 26), 'sportif': (28, 52)},
    'Mountain Climber': {'debutant': (6, 16), 'intermediaire': (16, 28), 'sportif': (28, 56)},
    'Superman': {'debutant': (2, 10), 'intermediaire': (10, 28), 'sportif': (30, 52)},
    'High Knees': {'debutant': (20, 40), 'intermediaire': (40, 60), 'sportif': (60, 80)},
    'Box Jump': {'debutant': (5, 15), 'intermediaire': (15, 25), 'sportif': (25, 35)},
    'Tuck Jump': {'debutant': (5, 15), 'intermediaire': (15, 25), 'sportif': (25, 35)},
    'Skipping Rope': {'debutant': (30, 60), 'intermediaire': (60, 90), 'sportif': (90, 120)},  #60 secondes
    'Burpees': {'debutant': (5, 15), 'intermediaire': (15, 25), 'sportif': (25, 40)},
    'Plank': {'debutant': (15, 30), 'intermediaire': (30, 45), 'sportif': (45, 60)},  # 60secondes
    'Leg Raises': {'debutant': (5, 15), 'intermediaire': (15, 25), 'sportif': (25, 35)},
    'Lunges': {'debutant': (6, 16), 'intermediaire': (16, 26), 'sportif': (26, 40)},
    'Pull-ups': {'debutant': (1, 5), 'intermediaire': (5, 10), 'sportif': (10, 20)},
    'Bicycle Crunches': {'debutant': (10, 20), 'intermediaire': (20, 30), 'sportif': (30, 50)},
    'Side Plank': {'debutant': (10, 20), 'intermediaire': (20, 35), 'sportif': (35, 50)}  # 60secondes
}

met_values = {
    'Squat': 3.5,
    'Push-up': 8.0,
    'Jumping Jack': 6.0,
    'Situps': 7.0,
    'V-up': 4.5,
    'Mountain Climber': 5.0,
    'Superman': 3.8,
    'High Knees': 6.5,
    'Box Jump': 8.0,
    'Tuck Jump': 7.8,
    'Skipping Rope': 10.0,
    'Burpees': 8.0,
    'Plank': 3.0,
    'Leg Raises': 4.0,
    'Lunges': 5.5,
    'Pull-ups': 8.0,
    'Bicycle Crunches': 4.0,
    'Side Plank': 3.5
}


def map_fitness_level(fitness_level):
    if fitness_level in ['Mauvaise', 'En dessous de la moyenne']:
        return 'debutant'
    elif fitness_level in ['Moyenne', 'Au-dessus de la moyenne', 'Bonne']:
        return 'intermediaire'
    elif fitness_level in ['Excellente', 'Athlète']:
        return 'sportif'
def simulate_training_session(user_profile, date=datetime.date.today()):
    exercises = list(exercise_params.keys())
    random.shuffle(exercises) 
    num_exercises = random.randint(8, 12)# Mélange aléatoire pour varier les séances
    exercises = exercises[:num_exercises] 
    fitness_category = map_fitness_level(user_profile['fitness_level'])
    weight = user_profile['weight']  # Assurez-vous que 'weight' fait partie du dict user_profile
    training_data = []

    for exercise in exercises:
        reps_range = exercise_params[exercise][fitness_category]
        repetitions = random.randint(reps_range[0], reps_range[1])
        major_errors = random.randint(0, max(1, repetitions // 10))
        minor_errors = random.randint(0, max(1, repetitions // 5))

        met_value = met_values[exercise] 
        duration_minute = 1 # Durée en minutes pour certains exercices
        exercise_data = {
            "date": date.isoformat(),
            "duration": duration_minute ,  # Durée en minutes
            "exerciseId": exercise,
            "majErrors": major_errors,
            "minErrors": minor_errors,
            "reps": repetitions,
            "calories": random.randint(30, 70)
        }
        training_data.append(exercise_data)

    return training_data
def calculate_target_heart_rate(met_value, user_profile):
    age = user_profile['age']
    resting_hr = user_profile['resting_heart_rate']
    max_hr = 220 - age
    hr_reserve = max_hr - resting_hr
    intensity = met_value / 10  # Lien entre MET et intensité de l'exercice
    target_hr = (hr_reserve * intensity) + resting_hr
    return target_hr


def simulate_workout_heart_rate(training_data, user_profile):
    heart_rates = []
    time_samples = []
    current_time = 0

    for exercise_data in training_data:
        exercise = exercise_data['exerciseId']
        met_value = met_values[exercise]
        target_hr = calculate_target_heart_rate(met_value, user_profile)
        duration = int(exercise_data['duration'])  # Assurez-vous que 'duration' est un entier
        variability = 2  # Variabilité dans la fréquence cardiaque

        # Générer des données de fréquence cardiaque normales avec la durée arrondie à l'entier le plus proche
        hr_data = np.random.normal(loc=target_hr, scale=variability, size=duration)
        heart_rates.extend(hr_data)
        time_samples.extend(np.arange(current_time, current_time + duration))
        current_time += duration

    heart_rate_df = pd.DataFrame({
        'time': time_samples,
        'heart_rate': heart_rates
    })

    return heart_rate_df.to_dict(orient='records')
def estimate_daily_calories():
    activities = {
        'faible': range(100, 400),
        'modérée': range(400, 700),
        'élevée': range(700, 1200),
        'très élevée': range(1200, 2000)
    }
    chosen_activity = random.choice(list(activities.keys()))
    calories = random.choice(activities[chosen_activity])+2000
    print(f"Activity Level: {chosen_activity}, Estimated Calories: {calories}")
    return calories


# In[10]:


def training_probability(fitness_level):
    probabilities = {
        'Athlète': 0.9,
        'Excellente': 0.8,
        'Bonne': 0.7,
        'Au-dessus de la moyenne': 0.6,
        'Moyenne': 0.5,
        'En dessous de la moyenne': 0.4,
        'Mauvaise': 0.3
    }
    return probabilities.get(fitness_level, 0.5)


# In[11]:


def update_fitness_level(user_profile, monthly_performance):
    # Supposons que 'monthly_performance' contient des détails comme le nombre de jours entraînés
    required_sessions = {
        'Athlète': 26, 'Excellente': 23, 'Bonne': 20,
        'Au-dessus de la moyenne': 18, 'Moyenne': 15,
        'En dessous de la moyenne': 12, 'Mauvaise': 10
    }
    next_level = {
        'Mauvaise': 'En dessous de la moyenne', 'En dessous de la moyenne': 'Moyenne',
        'Moyenne': 'Au-dessus de la moyenne', 'Au-dessus de la moyenne': 'Bonne',
        'Bonne': 'Excellente', 'Excellente': 'Athlète'
    }
    if monthly_performance['training_days'] >= required_sessions.get(user_profile['fitness_level'], 10):
        user_profile['fitness_level'] = next_level.get(user_profile['fitness_level'], user_profile['fitness_level'])


# In[12]:


def generate_data_for_month(start_date, end_date, num_users):
    users_data = {}

    for user_id in range(1, num_users + 1):
        user_profile = generate_individual_demographic_data(user_id)
        user_data = {
            'Profile': user_profile,
            'Daily_records': []
        }

        current_date = start_date
        monthly_performance = {'training_days': 0}

        while current_date <= end_date:
            daily_record = {
                'date': current_date.isoformat(),
                'estimated_calories': estimate_daily_calories()
            }

            if random.random() < training_probability(user_profile['fitness_level']):
                training_data = simulate_training_session(user_profile, current_date)
                heart_rate_data = simulate_workout_heart_rate(training_data, user_profile)
                daily_record['training_data'] = training_data
                daily_record['heart_rate_data'] = heart_rate_data
                monthly_performance['training_days'] += 1

            user_data['Daily_records'].append(daily_record)
            current_date += datetime.timedelta(days=1)

        # Update fitness level at the end of the month
        update_fitness_level(user_profile, monthly_performance)
        user_data['Profile'] = user_profile  # Update the profile in the main data structure

        # Save all monthly data for this user in one file
        with open(f'user_{user_id}_data.json', 'w') as f:
            json.dump(user_data, f, indent=4)

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 1, 31)
num_users = 5  # Number of users to simulate
generate_data_for_month(start_date, end_date, num_users)


# In[13]:


def generate_data_for_month(start_date, end_date, num_users):
    for user_id in range(1, num_users + 1):
        file_path = f'user_{user_id}_data.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                user_data = json.load(f)
            user_profile = user_data['Profile']  # Assurez-vous de récupérer le profil existant
        else:
            user_profile = generate_individual_demographic_data(user_id)
            user_data = {
                'Profile': user_profile,
                'Daily_records': []
            }
        
        current_date = start_date
        while current_date <= end_date:
            daily_record = {
                'date': current_date.isoformat(),
                'estimated_calories': estimate_daily_calories()
            }

            if random.random() < training_probability(user_profile['fitness_level']):
                training_data = simulate_training_session(user_profile, current_date)
                heart_rate_data = simulate_workout_heart_rate(training_data, user_profile)
                daily_record['training_data'] = training_data
                daily_record['heart_rate_data'] = heart_rate_data

            user_data['Daily_records'].append(daily_record)
            current_date += datetime.timedelta(days=1)

        # Save all data back to the same file
        with open(file_path, 'w') as f:
            json.dump(user_data, f, indent=4)

# Update your start and end dates for the new month
start_date = datetime.date(2024, 2, 1)
end_date = datetime.date(2024, 2, 28)
num_users = 5
generate_data_for_month(start_date, end_date, num_users)


# In[ ]:




