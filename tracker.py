import data
def add_workout():
    workout = input("Enter workout type: ").strip()
    if workout == "":
        print("Workout type cannot be empty.")
        return
    duration_text = input("Enter duration (minutes): ")
    
