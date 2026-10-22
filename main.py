import tracker

print("=== workout tracker ===")
print("1. Add a workout")
print("2. View all workouts")
print("3. View summary report")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    tracker.add_workout()
elif choice == "2":
    tracker.view_all_workouts()
elif choice == "3":
    tracker.view_summary_report()
elif choice == "4":
    print("Goodbye!")
else:
    print("Invalid choice. Please try again.")