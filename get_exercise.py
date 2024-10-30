import pandas as pd
import random

def generate_workout_plan(days):
    # Read the workout data from the CSV file
    workouts_df = pd.read_csv('workouts.csv')
    
    # Function to get random exercises for a given region and count
    def get_random_exercises(region, count):
        return workouts_df[workouts_df['bolge'] == region].sample(count)
    
    # Define workout plans based on the number of days
    workout_plan = {}

    if days == 1:
        workout_plan[1] = pd.concat([
            get_random_exercises("Gogus", 2),
            get_random_exercises("Omuz", 2),
            get_random_exercises("Biceps", 1),
            get_random_exercises("On Kol", 1),
            get_random_exercises("Arka Kol", 1),
            get_random_exercises("Sirt", 2),
            get_random_exercises("Bacak", 2)
        ])
    elif days == 2:
        workout_plan[1] = pd.concat([
            get_random_exercises("Gogus", 2),
            get_random_exercises("Omuz", 2),
            get_random_exercises("Biceps", 1),
            get_random_exercises("On Kol", 1),
            get_random_exercises("Arka Kol", 1),
            get_random_exercises("Sirt", 2)
        ])
        workout_plan[2] = get_random_exercises("Bacak", 5)
    
    elif days == 3:
        workout_plan[1] = pd.concat([
            get_random_exercises("Gogus", 3),
            get_random_exercises("Omuz", 3),
            get_random_exercises("Arka Kol", 2)
        ])
        workout_plan[2] = pd.concat([
            get_random_exercises("Sirt", 3),
            get_random_exercises("Biceps", 2),
            get_random_exercises("On Kol", 2)
        ])
        workout_plan[3] = get_random_exercises("Bacak", 5)

    elif days == 4:
        workout_plan[1] = pd.concat([
            get_random_exercises("Gogus", 3),
            get_random_exercises("Omuz", 3),
            get_random_exercises("Arka Kol", 2)
        ])
        workout_plan[2] = get_random_exercises("Bacak", 5)
        workout_plan[3] = pd.concat([
            get_random_exercises("Sirt", 3),
            get_random_exercises("Biceps", 2),
            get_random_exercises("On Kol", 2)
        ])
        workout_plan[4] = get_random_exercises("Bacak", 5)

    elif days == 5:
        workout_plan[1] = pd.concat([
            get_random_exercises("Gogus", 4),
            get_random_exercises("Arka Kol", 3)
        ])
        workout_plan[2] = get_random_exercises("Omuz", 3)
        workout_plan[3] = get_random_exercises("Bacak", 5)
        workout_plan[4] = pd.concat([
            get_random_exercises("Sirt", 4),
            get_random_exercises("Biceps", 2),
            get_random_exercises("On Kol", 2)
        ])
        workout_plan[5] = get_random_exercises("Bacak", 4)

    elif days == 6:
        workout_plan[1] = get_random_exercises("Gogus", 4)
        workout_plan[2] = get_random_exercises("Omuz", 3)
        workout_plan[3] = get_random_exercises("Bacak", 5)
        workout_plan[4] = get_random_exercises("Sirt", 4)
        workout_plan[5] = get_random_exercises("Bacak", 4)
        workout_plan[6] = pd.concat([
            get_random_exercises("Arka Kol", 3),
            get_random_exercises("Biceps", 3),
            get_random_exercises("On Kol", 3)
        ])

    elif days == 7:
        workout_plan[1] = get_random_exercises("Gogus", 4)
        workout_plan[2] = get_random_exercises("Omuz", 3)
        workout_plan[3] = get_random_exercises("Bacak", 5)
        workout_plan[4] = get_random_exercises("Sirt", 4)
        workout_plan[5] = "Dinlenme Günü"  # Rest day message instead of empty DataFrame
        workout_plan[6] = get_random_exercises("Bacak", 4)
        workout_plan[7] = pd.concat([
            get_random_exercises("Arka Kol", 3),
            get_random_exercises("Biceps", 3),
            get_random_exercises("On Kol", 3)
        ])
    
    return workout_plan

# Keep asking for valid input until the user enters a valid number of days
def get_valid_days_input():
    while True:
        try:
            days_input = int(input("Kaç gün spora gideceksiniz? (1-7): "))
            if days_input < 1 or days_input > 7:
                print("Hata: Geçerli bir gün sayısı giriniz (1-7).")
            else:
                return days_input
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz.")

# Main program
days_input = get_valid_days_input()
workout_plan = generate_workout_plan(days_input)

def save_workout_plan_to_excel(workout_plan, filename="workout_plan.xlsx"):
    with pd.ExcelWriter(filename) as writer:
        for day, plan in workout_plan.items():
            if isinstance(plan, pd.DataFrame):
                # Save each day's workout to a different sheet in the Excel file
                plan.to_excel(writer, sheet_name=f"Day {day}", index=False)
            else:
                # Create a DataFrame for rest day message
                pd.DataFrame([{"Rest Day": plan}]).to_excel(writer, sheet_name=f"Day {day}", index=False)

# Example usage:
# After generating the workout plan

# Display the workout plan for each day as a table
for day, plan in workout_plan.items():
    print(f"\nWorkout Plan for Day {day}:\n")
    if isinstance(plan, pd.DataFrame):
        print(plan.to_string(index=False))  # Display as a table without index
    else:
        print(plan)  # Print "Dinlenme Günü" or other string messages
        
save_workout_plan_to_excel(workout_plan, "workout_plan.xlsx")
