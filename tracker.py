"""
tracker.py - Core operations for logging, viewing, and calculating workout metrics.
"""

import data

def add_workout():
    workout = input("Enter workout type: ").strip()
    if workout == "":
        print("Workout type cannot be empty.")
        return 
    
    if workout.isdigit():
        print("Workout type cannot be a number.")
        return
    
    duration_text = input("Enter duration (minutes): ")
    if not duration_text.isdigit():
        print("Please enter a valid number for duration.")
        return
    
    duration = int(duration_text)
    if duration <= 0:
        print("Duration must be greater than 0.")
        return
    
    data.workout_types.append(workout)
    data.workout_durations.append(duration)

    print("Workout recorded successfully!")

def view_all_workouts():
    if len(data.workout_types) == 0:
        print("No workouts found in tracker.")
        return

    print("---Workout Tracker---")

    for i in range(len(data.workout_types)):
        print(f"{i+1}. Type: {data.workout_types[i]} | Duration: {data.workout_durations[i]}")

    print("---------------------\n")

def summary_report():
    if len(data.workout_types) == 0:
        print("No workouts to summarize")
        return

    total_count = len(data.workout_durations)
    total_time = sum(data.workout_durations)
    avg_duration = total_time / total_count
    max_time = max(data.workout_durations)
    min_time = min(data.workout_durations)

    print("---Workout Summary---")
    print(f"Total Time Spent: {total_time}")
    print(f"Number of workouts: {total_count}")
    print(f"Average Duration: {avg_duration}")
    print(f"Longest Duration: {max_time}")
    print(f"Shortest Duration: {min_time}")
    print("---------------------\n")