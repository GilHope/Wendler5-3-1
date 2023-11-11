# Wendler 5/3/1 Workout Program Calculator

This program calculates the Wendler 5/3/1 workout routine based on the user's one-rep maxes (1RMs) for the squat, bench press, deadlift, and overhead press exercises.

## Features

- Calculates 4-week training cycles.
- Customizes weights for each exercise based on 90% of the user's 1RM.
- Rounds the weights to the nearest 5lbs increment for practicality.
- Outputs the workout plan in a clear, readable format.

## Prerequisites

This program is written in Python 3. If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).


## Usage

To use this program, simply input your 1RM for the squat, bench press, deadlift, and overhead press. The program will output a four-week workout plan with the prescribed sets, reps, and weights.

**_This current README reflects the updates featured in 'wendler_func_3'._**

### Input Format

The input should be a tuple containing the 1RM values for the following lifts in the given order:

1. Squat
2. Bench Press
3. Deadlift
4. Overhead Press

Example:
```python
default_1rms = (315, 225, 405, 135)  # Replace these default values with your actual 1RMs
```
Now try calling it inside your terminal, run:

Example:
```bash
python3 wendler_func_3.py  
```

### Terminal Call

The program can be called from the terminal as follows:

Example:
```bash
python3 wendler_func_3.py 315 225 405 135  # Replace these arguments with your actual 1RMs
```
