import numpy as np

# Example dataset of Indian dishes with calorie information
dishes = {
    "Dal Tadka": 150,
    "Paneer Butter Masala": 300,
    "Roti": 120,
    "Biryani": 400,
    "Sambar": 180,
    "Vegetable Curry": 250,
    "Rice": 200,
    "Cucumber Salad": 50
}

# User preferences and dietary restrictions
daily_calories = 2000
preferred_dishes = ["Dal Tadka", "Roti", "Paneer Butter Masala", "Cucumber Salad"]
dietary_restrictions = ["No Biryani"]  # Example of a restriction

# AI-powered meal planning function
def generate_detailed_meal_plan(calories, preferences, dishes, restrictions, meals_per_day=3):
    plan = {f"Meal {i+1}": [] for i in range(meals_per_day)}  # Dictionary to store meals
    remaining_calories = calories
    calories_per_meal = calories // meals_per_day  # Divide daily calories across meals

    # Filter dishes based on dietary restrictions
    available_dishes = {dish: cal for dish, cal in dishes.items() if all(restriction not in dish for restriction in restrictions)}

    for meal in plan.keys():
        meal_calories = 0
        for dish in preferences:
            if dish in available_dishes and meal_calories + available_dishes[dish] <= calories_per_meal:
                plan[meal].append(dish)
                meal_calories += available_dishes[dish]
                remaining_calories -= available_dishes[dish]

        # Fill remaining calories for the meal with available non-preferred dishes
        for dish, cal in available_dishes.items():
            if dish not in plan[meal] and meal_calories + cal <= calories_per_meal:
                plan[meal].append(dish)
                meal_calories += cal
                remaining_calories -= cal

    # If calories remain, distribute them among meals
    if remaining_calories > 0:
        for meal in plan.keys():
            for dish, cal in available_dishes.items():
                if dish not in plan[meal] and remaining_calories >= cal:
                    plan[meal].append(dish)
                    remaining_calories -= cal
                    break  # Avoid overloading the meal

    return plan, calories - remaining_calories

# Generate a meal plan
meal_plan, total_calories_used = generate_detailed_meal_plan(
    daily_calories, preferred_dishes, dishes, dietary_restrictions
)

# Display the generated meal plan
print("Generated Meal Plan:")
for meal, items in meal_plan.items():
    print(f"{meal}: {', '.join(items)}")
print(f"Total Calories Consumed: {total_calories_used}")
print(f"Remaining Calories: {daily_calories - total_calories_used}")
