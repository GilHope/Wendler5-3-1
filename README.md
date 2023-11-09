### Wendler 5/3/1 Program Calculator

This repository contains a Python script for calculating weekly workout plans based on the Wendler 5/3/1 program. The Wendler 5/3/1 program is a popular strength training regimen designed by Jim Wendler for weightlifters looking to gain strength systematically. This script helps users to generate a four-week workout schedule with specified weights and reps according to their one-rep max (1RM) for squat, bench press, deadlift, and overhead press.

## Features

- Calculation of training maxes (90% of 1RM)
- Weekly workout plans:
  - Week 1: Sets of 5 reps at 65%, 75%, and 85% of training max
  - Week 2: Sets of 3 reps at 70%, 80%, and 90% of training max
  - Week 3: Sets of 5, 3, and 1 rep at 75%, 85%, and 95% of training max
  - Week 4: Deload week with sets of 5 reps at 40%, 50%, and 60% of training max
- Weights rounded to the nearest 5 lbs to match common gym equipment increments

To use this script, you will need Python 3 installed on your system. Clone the repository, navigate to the project directory, and run the script with your 1RM values.

```bash
git clone [repository-url]
cd [local-repository-name]
python3 wendler_func.py