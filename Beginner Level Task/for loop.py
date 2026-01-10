print("1: Rolling Six sided die multiple times\n")
import random

rolls = 20
count_six = 0
count_one = 0
two_sixes_in_row = 0
previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    if roll == 6:
        count_six += 1
        if previous_roll == 6:
            two_sixes_in_row += 1
    if roll == 1:
        count_one += 1

    previous_roll = roll

print("\nStatistics:")
print(f"Number of times rolled a 6: {count_six}")
print(f"Number of times rolled a 1: {count_one}")
print(f"Number of times two 6s appeared in a row: {two_sixes_in_row}")

print("================================================================\n")

print("2: Jumping Jacks Workout\n")

total_jumping_jacks = 100
set_size = 10
completed = 0

for i in range(0, total_jumping_jacks, set_size):
    completed += set_size
    print(f"\nYou performed {set_size} jumping jacks. Total completed: {completed}")

    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed
            print(f"{remaining} jumping jacks remaining.")
    else:
        remaining = total_jumping_jacks - completed
        print(f"{remaining} jumping jacks remaining.")

else:
    print("\nCongratulations! You completed the workout.")

