from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from calorie_calculator import user_info, calculate_activity, gain_or_lose
import meal_planner
import pandas as pd
import nutritional_values
import matplotlib.pyplot as plt

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meal_plan", methods=["GET", "POST"])
def meal_plan():
    if request.method == "POST":
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        weight = int(request.form.get("weight"))
        height = int(request.form.get("height"))
        activity_level = request.form.get("activity_level")
        goal = request.form.get("goal")
        calories = gain_or_lose(calculate_activity(
            user_info(age, gender, weight, height), activity_level), goal)
        grams = nutritional_values.extract_gram(
            nutritional_values.build_nutritional_values(weight, calories, goal))
        C = grams['Carbohydrates Grams']
        F = grams['Fat Grams']
        P = grams['Protein Grams']
        
        monday_breakfast = meal_planner.snack_model(0, weight, calories, meal_planner.data, 'Breakfast', goal)
        monday_breakfast_food = monday_breakfast["Food"].apply(str).astype(str).str.replace(
            '\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_breakfast_quantity = monday_breakfast["Quantity (g)"].apply(
            str).astype(str).str.replace('\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_snack1 = meal_planner.snack_model(0, weight, calories, meal_planner.data, 'Snack 1', goal)
        monday_snack1_food = monday_snack1["Food"].apply(str).astype(str).str.replace(
            '\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_snack1_quantity = monday_snack1["Quantity (g)"].apply(
            str).astype(str).str.replace('\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_lunch = meal_planner.main_meal_model(0, weight, calories, meal_planner.data, 'Lunch', goal)
        monday_lunch_food = monday_lunch["Food"].apply(str).astype(str).str.replace(
            '\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_lunch_quantity = monday_lunch["Quantity (g)"].apply(
            str).astype(str).str.replace('\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_snack2 = meal_planner.snack_model(0, weight, calories, meal_planner.data, 'Snack 2', goal)
        monday_snack2_food = monday_snack2["Food"].apply(str).astype(str).str.replace(
            '\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_snack2_quantity = monday_snack2["Quantity (g)"].apply(
            str).astype(str).str.replace('\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_dinner = meal_planner.main_meal_model(0, weight, calories, meal_planner.data, 'Dinner', goal)
        monday_dinner_food = monday_dinner["Food"].apply(str).astype(str).str.replace(
            '\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        monday_dinner_quantity = monday_dinner["Quantity (g)"].apply(
            str).astype(str).str.replace('\n', '<br>').to_frame().to_html(index=False, header=False, border=0)
        return render_template("meal_plan.html", protein=round(P), fat=round(F), carbohydrate=round(C), calories=calories, monday_breakfast_food=monday_breakfast_food,
                        monday_breakfast_quantity=monday_breakfast_quantity, monday_snack1_food=monday_snack1_food,
                        monday_snack1_quantity=monday_snack1_quantity, monday_lunch_food=monday_lunch_food, monday_lunch_quantity=monday_lunch_quantity, 
                        monday_snack2_food=monday_snack2_food, monday_snack2_quantity=monday_snack2_quantity, monday_dinner_food=monday_dinner_food,
                        monday_dinner_quantity=monday_dinner_quantity)
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)