def user_info(age, gender, weight, height):
    if gender == 'male':
        c1 = 5
        hm = 6.25 * height
        wm = 10 * weight
        am = 5 * age
    elif gender == 'female':
        c1 = -161
        hm = 6.25 * height
        wm = 10 * weight
        am = 5 * age

    bmr_result = c1 + hm + wm - am
    return (int(bmr_result))



def calculate_activity(bmr_result, activity_level): # This function takes the bmr result as a parameter and returns the activity level of the user.
    if activity_level == 'sedentary': 
        activity_level = 1.2 * bmr_result 
    elif activity_level == 'light':
        activity_level = 1.375 * bmr_result 
    elif activity_level == 'moderate': 
        activity_level = 1.55 * bmr_result 
    elif activity_level == 'very':
        activity_level = 1.725 * bmr_result
    elif activity_level == 'extra':
        activity_level = 1.9 * bmr_result
    return (int(activity_level)) 



def gain_or_lose(activity_level, goal): # This function calculates the number of calories required to lose / maintain / gain weight based on a user's activity level.
    global calories
    if goal == 'lose':
        calories = activity_level - 300
    elif goal == 'maintain':
        calories = activity_level
    elif goal == 'gain':
        calories = activity_level + 300
    return (int(calories)) # This function returns the number of calories the user should be consuming.
