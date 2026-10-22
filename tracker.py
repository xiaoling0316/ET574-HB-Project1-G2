import data
def add_workout():
    workout = input("Enter workout type: ").strip()
    if workout == "":
        print("Workout type cannot be empty.")
        return
    duration_text = input("Enter duration (minutes): ")
    if not duration_text.isdigit():
        print("Please enter a valid number for duration.")
        return
    duration = int(duration_text)
    if duration <= 0:
        print("Duration must be greater than 0.")
        return
