# Project I: Personal Workout Log Tracker

## Overview

The Workout Log Tracker provides an interactive terminal interface for managing daily exercise sessions. The program tracks activities in real time using in-memory parallel lists to record workout modalities and their durations without using dictionaries.

### Features
* **Interactive Menu Navigation:** Persistent loop providing clear command options.
* **Input Validation:** Enforces non-empty workout names and positive numeric durations.
* **Session History:** Formats and prints all logged exercises chronologically.
* **Statistical Summary:** Computes total active minutes, workout frequency, average session length, and extreme values (longest and shortest workouts).

---

## File Structure

```
workout_tracker/
├── .github/
│   └── issue_tracking.csv   # Task tracking mapped to commit IDs
├── data.py                  # In-memory storage using parallel lists
├── tracker.py               # Functional logic for input, viewing, and summaries
├── main.py                  # Main entry point and user menu loop
└── README.md                # Project documentation and instructions 

## how to Run
1. Open the project in python or github codespaces.
2. Run main.py.
3. select an option from the menu

## Storage 
workout data is stored in memory and is cleared when the program end.