def build_nutritional_values(kg, calories, goal):
    if goal == 'lose':
       protein_calories = 35/100 * calories
       carb_calories = 40/100 * calories
       fat_calories = 25/100 * calories
    elif goal == 'maintain':
       protein_calories = 30/100 * calories
       carb_calories = 40/100 * calories
       fat_calories = 30/100 * calories
    elif goal == 'gain':
       protein_calories = 35/100 * calories
       carb_calories = 45/100 * calories
       fat_calories = 20/100 * calories 
    # Create a dictionary with the results
    res = {'Protein Calories': protein_calories,
           'Carbohydrates Calories': carb_calories, 'Fat Calories': fat_calories}
    return res

def extract_gram(table):
    # Calculate protein grams
    protein_grams = table['Protein Calories']/4.
    # Calculate carbohydrates grams
    carbs_grams = table['Carbohydrates Calories']/4.
    # Calculate fat grams
    fat_grams = table['Fat Calories']/9.
    # Create a dictionary with the results
    res = {'Protein Grams': protein_grams,
           'Carbohydrates Grams': carbs_grams, 'Fat Grams': fat_grams}
    return res
