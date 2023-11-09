# The Wendler 5/3/1 workout program standard percentages and reps
# Week 1: 3 sets of 5 reps at 65%, 75%, and 85% of 1RM
# Week 2: 3 sets of 3 reps at 70%, 80%, and 90% of 1RM
# Week 3: 3 sets of 5, 3, and 1 rep at 75%, 85%, and 95% of 1RM
# Week 4: Deload week, 3 sets of 5 reps at 40%, 50%, and 60% of 1RM

# We will write a function that calculates the workout plan for each week given a 1RM.

def calculate_wendler_531(orms):
    """
    Calculate the Wendler 5/3/1 workout program based on the given 1RMs.

    :param orms: A tuple containing the 1RM for squat, bench, deadlift, overhead press
    :return: A dictionary with the workout plan for each week
    """
    workout_plan = {}
    training_maxes = {lift: max * 0.9 for lift, max in zip(["Squat", "Bench", "Deadlift", "OHP"], orms)}

    # Define the rep schemes and percentages for each week
    rep_schemes = {
        "WEEK 1:": [(5, 0.65), (5, 0.75), (5, 0.85)],
        "WEEK 2:": [(3, 0.70), (3, 0.80), (3, 0.90)],
        "WEEK 3:": [(5, 0.75), (3, 0.85), (1, 0.95)],
        "WEEK 4:": [(5, 0.40), (5, 0.50), (5, 0.60)]
    }

    # Calculate the weights for each set
    for week, reps_and_percs in rep_schemes.items():
        workout_plan[week] = {}
        for lift, training_max in training_maxes.items():
            workout_plan[week][lift] = [("{} Reps".format(reps), "{}lbs".format(round(training_max * perc / 5) * 5)) for reps, perc in reps_and_percs]

    return workout_plan

# For now, we'll just define the function. It will be called later with the user's 1RM inputs to generate the workout plan.
# We round the weights to the nearest 5 as is common in many gyms where weights are available in 5-pound increments.


#################################################################################################
#################################################################################################

# Test Call #

if __name__ == "__main__":
    # Example 1RM inputs
    my_1rms = (315, 225, 405, 135)  # Replace with your 1RM for squat, bench, deadlift, overhead press
    workout_plan = calculate_wendler_531(my_1rms)
    print(workout_plan)

# ^^^Uncomment the above ' Test Call ' scrip, open terminal and run this command to test: ' python3 wendler_func.py '

#################################################################################################
#################################################################################################