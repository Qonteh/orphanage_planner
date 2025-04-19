import csv
import random
from datetime import datetime, timedelta

# Constants
num_rows = 50000  # 🚀 MASSIVE data for AI power boost
start_year = 1995
end_year = 2023

food_items = ["Rice", "Beans", "Maize Flour", "Vegetables", "Fruits", "Meat", "Fish", "Milk", "Eggs", "Bread"]
emergencies = ["None", "Power Outage", "Water Shortage", "Fire", "Sickness", "Flood", "Robbery", "Staff Strike"]
medical_conditions = ["None", "Malaria", "Fever", "Diarrhea", "Flu", "Injury", "Infection", "Covid-19"]
utility_types = ["Electricity", "Water", "Gas", "Internet", "Phone", "Security", "Sanitation"]

def random_date():
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).strftime("%Y-%m-%d")

with open('mega_ai_orphanage_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow([
        "Date", "Num_Children", "Food_Remaining", "Daily_Need", "Food_Used",
        "Donation_Amount", "Expense_Total", "Budget_Left", "Food_Shortage",
        "Suggested_Purchase", "Quantity_To_Buy", "Estimated_Cost", "Emergency_Event",
        "Medical_Treatment", "Medical_Cost", "Utility_Type", "Utility_Cost", "Staff_On_Duty", "Notes",
        "Food_Per_Child", "Donation_Per_Child", "Budget_Per_Child",
        "Cost_Per_Child", "Food_Shortage_Per_Child", "Remaining_Days_Covered",
        "Emergency_Flag", "Medical_Flag", "High_Utility_Cost", "Season", "Holiday_Flag"
    ])

    for _ in range(num_rows):
        date = random_date()
        month = int(date.split("-")[1])
        season = (
            "Rainy" if month in [3, 4, 5, 10, 11] else
            "Dry" if month in [6, 7, 8, 9] else
            "Cold"
        )
        holiday_flag = 1 if month in [12, 1, 4] else 0

        num_children = random.randint(20, 100)
        daily_need = num_children
        food_remaining = random.randint(10, 120)
        food_used = random.randint(5, min(60, food_remaining))
        donation_amount = random.randint(0, 200000)
        expense_total = random.randint(15000, 150000)
        budget_left = donation_amount - expense_total
        food_shortage = max(0, daily_need - food_remaining)
        suggested_item = random.choice(food_items) if food_shortage > 0 else "None"
        quantity_to_buy = food_shortage if food_shortage > 0 else 0
        estimated_cost = quantity_to_buy * random.randint(1200, 2500)
        emergency = random.choices(emergencies, weights=[65, 10, 6, 5, 8, 3, 2, 1])[0]
        medical = random.choices(medical_conditions, weights=[60, 10, 10, 5, 5, 4, 3, 3])[0]
        medical_cost = random.randint(0, 40000) if medical != "None" else 0
        utility = random.choice(utility_types)
        utility_cost = random.randint(8000, 60000)
        staff_on_duty = random.randint(3, 12)
        notes = "Stable" if budget_left >= 0 and food_shortage == 0 else "Check food/donations"

        # Feature Engineering
        food_per_child = round(food_used / num_children, 2)
        donation_per_child = round(donation_amount / num_children, 2)
        budget_per_child = round(budget_left / num_children, 2)
        cost_per_child = round((expense_total + medical_cost + utility_cost) / num_children, 2)
        food_shortage_per_child = round(food_shortage / num_children, 2)
        remaining_days_covered = round(food_remaining / daily_need, 2)
        emergency_flag = 0 if emergency == "None" else 1
        medical_flag = 0 if medical == "None" else 1
        high_utility_cost = 1 if utility_cost > 30000 else 0

        writer.writerow([
            date, num_children, food_remaining, daily_need, food_used,
            donation_amount, expense_total, budget_left, food_shortage,
            suggested_item, quantity_to_buy, estimated_cost, emergency,
            medical, medical_cost, utility, utility_cost, staff_on_duty, notes,
            food_per_child, donation_per_child, budget_per_child,
            cost_per_child, food_shortage_per_child, remaining_days_covered,
            emergency_flag, medical_flag, high_utility_cost, season, holiday_flag
        ])

print("🚀 Done generating 50,000 rows of ULTRA AI POWER data 💪💡📊 Ready to feed your model and hit that 0.8+ accuracy! 🔥")
