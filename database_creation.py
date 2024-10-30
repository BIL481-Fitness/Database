import random


workouts = [
    # Gogus (Chest) exercises
    {"bolge": "Gogus", "hareket_adi": "Bench Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Gogus", "hareket_adi": "Incline Bench Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Gogus", "hareket_adi": "Chest Fly", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "Gogus", "hareket_adi": "Push-Up", "set_sayisi": 3, "tekrar_sayisi": "15-20", "ekipman": "Bodyweight"},
    {"bolge": "Gogus", "hareket_adi": "Cable Crossover", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Cable"},
    {"bolge": "Gogus", "hareket_adi": "Dumbbell Bench Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Dumbbell"},
    {"bolge": "Gogus", "hareket_adi": "Pec Deck Machine", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Machine"},
    {"bolge": "Gogus", "hareket_adi": "Decline Bench Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Gogus", "hareket_adi": "Dips", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Bodyweight"},
    {"bolge": "Gogus", "hareket_adi": "Landmine Press", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},

    # Omuz (Shoulders) exercises
    {"bolge": "Omuz", "hareket_adi": "Overhead Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Omuz", "hareket_adi": "Lateral Raise", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "Omuz", "hareket_adi": "Front Raise", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "Omuz", "hareket_adi": "Arnold Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Dumbbell"},
    {"bolge": "Omuz", "hareket_adi": "Machine Shoulder Press", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Machine"},
    {"bolge": "Omuz", "hareket_adi": "Cable Face Pull", "set_sayisi": 4, "tekrar_sayisi": "15-20", "ekipman": "Cable"},
    {"bolge": "Omuz", "hareket_adi": "Reverse Fly", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "Omuz", "hareket_adi": "Seated Dumbbell Press", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Dumbbell"},
    {"bolge": "Omuz", "hareket_adi": "Upright Row", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Barbell"},
    {"bolge": "Omuz", "hareket_adi": "Dumbbell Shrug", "set_sayisi": 4, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},

    # Biceps exercises
    {"bolge": "Biceps", "hareket_adi": "Barbell Curl", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Biceps", "hareket_adi": "Dumbbell Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "Biceps", "hareket_adi": "Concentration Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "Biceps", "hareket_adi": "Hammer Curl", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Dumbbell"},
    {"bolge": "Biceps", "hareket_adi": "Preacher Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Barbell or Dumbbell"},
    {"bolge": "Biceps", "hareket_adi": "Cable Curl", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Cable"},
    {"bolge": "Biceps", "hareket_adi": "Incline Dumbbell Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "Biceps", "hareket_adi": "Zottman Curl", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Dumbbell"},
    {"bolge": "Biceps", "hareket_adi": "Reverse Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Barbell"},
    {"bolge": "Biceps", "hareket_adi": "Spider Curl", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Barbell or Dumbbell"},

    # On Kol (Forearms) exercises
    {"bolge": "On Kol", "hareket_adi": "Wrist Curl", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "On Kol", "hareket_adi": "Reverse Wrist Curl", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "On Kol", "hareket_adi": "Farmer's Walk", "set_sayisi": 3, "tekrar_sayisi": "15-20", "ekipman": "Dumbbell"},
    {"bolge": "On Kol", "hareket_adi": "Reverse Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Barbell"},
    {"bolge": "On Kol", "hareket_adi": "Zottman Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "On Kol", "hareket_adi": "Hammer Curl", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Dumbbell"},
    {"bolge": "On Kol", "hareket_adi": "Preacher Curl", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "On Kol", "hareket_adi": "Plate Pinch", "set_sayisi": 3, "tekrar_sayisi": "15-20", "ekipman": "Plate"},
    {"bolge": "On Kol", "hareket_adi": "Cable Curl", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Cable"},
    {"bolge": "On Kol", "hareket_adi": "Reverse Barbell Curl", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Barbell"},

    # Arka Kol (Triceps) exercises
    {"bolge": "Arka Kol", "hareket_adi": "Tricep Pushdown", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Cable"},
    {"bolge": "Arka Kol", "hareket_adi": "Skull Crushers", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Arka Kol", "hareket_adi": "Dips", "set_sayisi": 3, "tekrar_sayisi": "15-20", "ekipman": "Bodyweight"},
    {"bolge": "Arka Kol", "hareket_adi": "Close Grip Bench Press", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Arka Kol", "hareket_adi": "Overhead Tricep Extension", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "Arka Kol", "hareket_adi": "Tricep Kickback", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "Arka Kol", "hareket_adi": "Rope Tricep Extension", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Cable"},
    {"bolge": "Arka Kol", "hareket_adi": "Tricep Dips (Bench)", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Bodyweight"},
    {"bolge": "Arka Kol", "hareket_adi": "One-Arm Overhead Extension", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "Arka Kol", "hareket_adi": "Cable Overhead Tricep Extension", "set_sayisi": 4, "tekrar_sayisi": "10-12", "ekipman": "Cable"},

    # Sirt (Back) exercises
    {"bolge": "Sirt", "hareket_adi": "Pull-Up", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Bodyweight"},
    {"bolge": "Sirt", "hareket_adi": "Lat Pulldown", "set_sayisi": 4, "tekrar_sayisi": "10-12", "ekipman": "Cable"},
    {"bolge": "Sirt", "hareket_adi": "Barbell Row", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Sirt", "hareket_adi": "Deadlift", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Sirt", "hareket_adi": "T-Bar Row", "set_sayisi": 4, "tekrar_sayisi": "10-12", "ekipman": "Barbell"},
    {"bolge": "Sirt", "hareket_adi": "Seated Row", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Cable"},
    {"bolge": "Sirt", "hareket_adi": "Dumbbell Row", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"},
    {"bolge": "Sirt", "hareket_adi": "Face Pull", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Cable"},
    {"bolge": "Sirt", "hareket_adi": "Hyperextension", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Bodyweight"},
    {"bolge": "Sirt", "hareket_adi": "Chin-Up", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Bodyweight"},

    # Bacak (Legs) exercises
    {"bolge": "Bacak", "hareket_adi": "Squat", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Bacak", "hareket_adi": "Leg Press", "set_sayisi": 4, "tekrar_sayisi": "10-12", "ekipman": "Machine"},
    {"bolge": "Bacak", "hareket_adi": "Lunges", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Bodyweight or Dumbbell"},
    {"bolge": "Bacak", "hareket_adi": "Romanian Deadlift", "set_sayisi": 3, "tekrar_sayisi": "8-10", "ekipman": "Barbell"},
    {"bolge": "Bacak", "hareket_adi": "Leg Curl", "set_sayisi": 4, "tekrar_sayisi": "12-15", "ekipman": "Machine"},
    {"bolge": "Bacak", "hareket_adi": "Leg Extension", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Machine"},
    {"bolge": "Bacak", "hareket_adi": "Bulgarian Split Squat", "set_sayisi": 3, "tekrar_sayisi": "10-12", "ekipman": "Dumbbell"},
    {"bolge": "Bacak", "hareket_adi": "Calf Raise", "set_sayisi": 4, "tekrar_sayisi": "15-20", "ekipman": "Machine or Dumbbell"},
    {"bolge": "Bacak", "hareket_adi": "Hack Squat", "set_sayisi": 4, "tekrar_sayisi": "8-10", "ekipman": "Machine"},
    {"bolge": "Bacak", "hareket_adi": "Step-Up", "set_sayisi": 3, "tekrar_sayisi": "12-15", "ekipman": "Dumbbell"}

]


import pandas as pd





# Read the CSV file
csv_file = 'workouts.csv'  # Replace with your actual CSV file path if necessary
df = pd.read_csv(csv_file)

# Display the DataFrame as a table
print(df)