# Foody
---
## _Put your diet on autopilot_
##### Stop worrying about what to eat, our personalised meal planner has got you covered!
------------------
#### Video Demo:  <https://www.youtube.com/watch?v=BCI0FRn1kdg>

### Table of Contents  
  * [Features](#features)
  * [Tech](#tech)
  * [Architecture](#architecture)
  * [Future Work](#future-work)


## Features

- **Personalised Meal Plans**: Enter your age, weight, height, gender, activity level, and weight goal to receive a personalised meal plan for the entire day.
- **Calorie and Nutrient Tracking**: Our meal planner calculates the calories and nutrient values (protein, carbs, and fat) of each meal in your plan, helping you track your intake.
- **User-Friendly Interface**: Our site provides an intuitive interface that makes it easy to input your information and navigate through the meal plan.
- **Change disliked meals**: Don't like a specific meal in your plan? We've got you covered with a simple reload button!

Foody combines powerful calculations and a user-friendly interface to deliver a comprehensive solution for planning and tracking your meals. Whether you are looking to achieve specific health goals or maintain a balanced diet, this application will help you create and manage personalised meal plans with ease.

## Tech

Foody is based on different programming languages:

- [Python]
- [SQL]
- [HTML]
- [CSS]
- [Javascript]

## Architecture
- **Static**: This folder contains the different images used for the project. It also contains the styling for each page (.css files) and the required JS scripts.
- **Templates**: This folder contains the different HTML templates for the project, combined together with JINJA: **_layout.html_** sets the ground for the frontend, leaving space through JINJA for page-specific css styling and JS scripting. **_index.html_** is the homepage that contains the table for user input. **_meal_plan.html_** displays the output table after python code executes the calculations.
- **app**: Through the usage of Flask, this python file is the base of the project’s web application.
- **calorie_calculator**: This python file contains the algorithm that calculates the user’s calorie intake based on the input in **_index.html_**. 
- **nutritional_values**: This python file takes contains the algorithm that calculates the user’s macronutrient intake (protein, carbohydrates, fat) based on the calorie intake calculated in **_calorie_calculator_**
- **meal_planner**: This python file first reads in the data from my modified version of **_MyFoodData Nutrition.csv_**, first selecting the columns of interest, then splitting it into days and meals. With this data it creates smaller, random samples of datasets for each meal in order to always create different meal plans that still respect calorie and macronutrient restrictions. This file also contains the main_meal and snack models which perform the necessary calculations in order to find the perfect combination of dishes within the given calories and macronutrients. 

## Future Work
- **plot**: This python file will contain the necessary code in order to plot the distribution of macronutrients within a given meal, in order to display it on **_meal_plan.html_**.
- **users.db**: This will serve as SQL database in order to add login feature.
- **Machine Learning**: Through machine learning the algorithm will take into account the user’s preferences.
- **Shopping list**: Through an API users will be able to order the required ingredients directly from our site.
- **Single Meal replacement**: Add the feature to reload a single meal and preserve the rest of the meal plan.