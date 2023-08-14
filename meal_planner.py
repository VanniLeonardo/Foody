import numpy as np
import pandas as pd
from pulp import *

import calorie_calculator
import nutritional_values

# import data
data = pd.read_csv("MyFoodData Nutrition.csv")

# select columns of interest
data = data[['name', 'calories', 'carbohydrate', 'total_fat', 'protein', 'meal']]

# split data into days
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
split_values_day = np.linspace(0, len(data), 8).astype(int)
split_values_day[-1] = split_values_day[-1]-1

# split data into meals
meals = ['Snack 1', 'Snack 2', 'Breakfast', 'Lunch', 'Dinner']
meal_split = {'Snack 1': 0.10, 'Snack 2': 0.10, 'Breakfast': 0.15, 'Lunch': 0.35, 'Dinner': 0.30}


def random_snack_dataset(data, day):
    # Select only the rows that contain the word 'Snacks' in the 'meal' column
    data = data[data['meal'].str.contains('Snacks', na=False)]
    # Shuffle the rows of the dataframe
    frac_data = data.sample(frac=1).reset_index(drop=True)
     # Split the dataset in 7 parts (7 days) and append each part to the list
    day_data = []
    for s in range(len(split_values_day)-1):
        day_data.append(
            frac_data.loc[split_values_day[s]:split_values_day[s+1]])
    return day_data
    

def random_main_meal_dataset(data, day):
    # Select only main meals from the dataset
    data = data[data['meal'].str.contains(
        'Main Dishes|Condiments|Side Dishes', na=False)]
    # Create a random sample of the dataset and reset the index
    frac_data = data.sample(frac=1).reset_index(drop=True)
    day_data = []
    # Split the dataset in 7 parts (7 days) and append each part to the list
    for s in range(len(split_values_day)-1):
        day_data.append(
            frac_data.loc[split_values_day[s]:split_values_day[s+1]])
    return day_data


def main_meal_model(day, weight, calories, data, meal, goal):
    calories = calories*meal_split[meal]
    data = random_main_meal_dataset(data, day)
    G = nutritional_values.extract_gram(
        nutritional_values.build_nutritional_values(weight, calories, goal))
    C = G['Carbohydrates Grams']
    F = G['Fat Grams']
    P = G['Protein Grams']
    day_data = data[day]
    day_data = day_data[day_data.calories != 0]
    food = day_data.name.tolist()
    x = {}
    for i in range(len(food)):
        x[food[i]] = LpVariable(
            f"x_{i}", lowBound=0, upBound=1.5, cat='Continuous')
    c = day_data.carbohydrate.tolist()
    f = day_data.total_fat.tolist()
    p = day_data.protein.tolist()
    div_meal = meal_split[meal]
    prob = LpProblem("Diet", LpMinimize)
    prob += lpSum([x[food[i]]*day_data.calories.tolist()[i]
                       for i in range(len(food))])
    prob += lpSum([x[food[i]]*c[i]
                       for i in range(len(x))]) >= C*div_meal
    prob += lpSum([x[food[i]]*f[i]
                       for i in range(len(x))]) >= F*div_meal
    prob += lpSum([x[food[i]]*p[i]
                       for i in range(len(x))]) >= P*div_meal
    prob.solve(PULP_CBC_CMD(msg=0))
    variables = []
    values = []
    for v in prob.variables():
        variable = v.name
        value = v.varValue
        variables.append(variable)
        values.append(value)
    values = np.array(values).round(2).astype(float)
    sol = pd.DataFrame(np.array([food, values]).T,
                       columns=['Food', 'Quantity'])
    sol['Quantity'] = sol.Quantity.astype(float) 
    sol.Quantity = round(sol.Quantity*10)*10
    sol = sol[sol['Quantity'] != 0.0]
    sol = sol.rename(columns={'Quantity': 'Quantity (g)'})
    return sol

def snack_model(day, kg, calories, data, meal, goal):
    calories = calories*meal_split[meal]
    data = random_snack_dataset(data, day)
    G = nutritional_values.extract_gram(
        nutritional_values.build_nutritional_values(kg, calories, goal))
    C = G['Carbohydrates Grams']
    F = G['Fat Grams']
    P = G['Protein Grams']
    day_data = data[day]
    day_data = day_data[day_data.calories != 0]
    food = day_data.name.tolist()
    x = {}
    for i in range(len(food)):
        x[food[i]] = LpVariable(
            f"x_{i}", lowBound=0, upBound=1.5, cat='Continuous')
    c = day_data.carbohydrate.tolist()
    f = day_data.total_fat.tolist()
    p = day_data.protein.tolist()
    div_meal = meal_split[meal]
    prob = LpProblem("Diet", LpMinimize)
    prob += lpSum([x[food[i]]*day_data.calories.tolist()[i]
                       for i in range(len(food))])
    prob += lpSum([x[food[i]]*c[i]
                       for i in range(len(x))]) >= C*div_meal
    prob += lpSum([x[food[i]]*f[i]
                       for i in range(len(x))]) >= F*div_meal
    prob += lpSum([x[food[i]]*p[i]
                       for i in range(len(x))]) >= P*div_meal
    prob.solve(PULP_CBC_CMD(msg=0))
    variables = []
    values = []
    for v in prob.variables():
        variable = v.name
        value = v.varValue
        variables.append(variable)
        values.append(value)
    values = np.array(values).round(2).astype(float)
    sol = pd.DataFrame(np.array([food, values]).T,
                       columns=['Food', 'Quantity'])
    sol['Quantity'] = sol.Quantity.astype(float)
    sol.Quantity = round(sol.Quantity*10)*10
    sol = sol[sol['Quantity'] != 0.0]
    sol = sol.rename(columns={'Quantity': 'Quantity (g)'})
    return sol