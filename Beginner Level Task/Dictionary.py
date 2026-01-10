print("================================================================")
print("1: List of friends\n")
friends = ["Zoya", "Ritesh", "Zia", "Lubna", "Hammad"]

friend_tuples = [(friend, len(friend)) for friend in friends]

print("List of friends with name lengths:")
for ft in friend_tuples:
    print(ft)

print("================================================================")

print("2: Trip Planning Track Expenses\n")

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

total_your = sum(your_expenses.values())
total_partner = sum(partner_expenses.values())

print("Total expenses:")
print(f"Your total expenses: {total_your}")
print(f"Partner's total expenses: {total_partner}")

if total_your > total_partner:
    print("You spent more money overall.")
elif total_your < total_partner:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount overall.")

max_diff = 0
max_category = ""
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print(f"\nCategory with the biggest difference: {max_category}")
print(f"Difference in spending: {max_diff}")
