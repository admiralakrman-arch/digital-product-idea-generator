import random

ideas = {
    "fitness": [
        "30-Day Home Workout Plan",
        "Healthy Meal Prep Guide",
        "Beginner Yoga eBook",
        "Fat Loss Tracker Spreadsheet",
        "Home Workout Video Course"
    ],
    "cooking": [
        "Air Fryer Recipe eBook",
        "Mediterranean Diet Guide",
        "Quick 15-Minute Meals eBook",
        "Healthy Dessert Recipe Book",
        "Weekly Meal Planner Template"
    ],
    "money": [
        "Passive Income Guide",
        "Budget Planner Spreadsheet",
        "Side Hustle Ideas eBook",
        "Investing for Beginners Course",
        "Freelancing Starter Kit"
    ]
}

print("Digital Product Idea Generator")

niche = input("Enter a niche: ").lower()

if niche in ideas:
    print("\nTop Digital Product Ideas:\n")
    for i in random.sample(ideas[niche], len(ideas[niche])):
        print("-", i)
else:
    print("Niche not found. Try: fitness, cooking, money")
