# Wendler 5/3/1 Workout Program Calculator

This program calculates the Wendler 5/3/1 workout routine based on the user's one-rep maxes (1RMs) for the squat, bench press, deadlift, and overhead press exercises.

## Features

- Calculates 4-week training cycles.
- Customizes weights for each exercise based on 90% of the user's 1RM.
- Rounds the weights to the nearest 5lbs increment for practicality.
- Outputs the workout plan in a clear, readable format.

## Usage

To use this program, simply input your 1RM for the squat, bench press, deadlift, and overhead press. The program will output a four-week workout plan with the prescribed sets, reps, and weights.

### Input Format

The input should be a tuple containing the 1RM values for the following lifts in the given order:

1. Squat
2. Bench Press
3. Deadlift
4. Overhead Press

Example:
```python
my_1rms = (315, 225, 405, 135)  # Replace these values with your actual 1RMs
```

### Terminal Call

The program can be called from the terminal as follows:

Example:
```bash
python3 wendler_531_calculator.py 315 225 405 135
```
