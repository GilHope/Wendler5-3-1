import sys

def calculate_wendler_531(orms):
    """
    Calculate the Wendler 5/3/1 workout program based on the given 1RMs.

    :param orms: A tuple containing the 1RM for squat, bench, deadlift, overhead press
    :return: A dictionary with the workout plan for each week
    """
    workout_plan = {}
    # Adjust the keys to match the naming convention you want, all uppercase
    training_maxes = {lift: max * 0.9 for lift, max in zip(["SQUAT", "BENCH", "DEADLIFT", "OHP"], orms)}

    # Define the rep schemes and percentages for each week
    rep_schemes = {
        "WEEK 1": [(5, 0.65), (5, 0.75), (5, 0.85)],
        "WEEK 2": [(3, 0.70), (3, 0.80), (3, 0.90)],
        "WEEK 3": [(5, 0.75), (3, 0.85), (1, 0.95)],
        "WEEK 4": [(5, 0.40), (5, 0.50), (5, 0.60)]
    }

    # Calculate the weights for each set
    for week, reps_and_percs in rep_schemes.items():
        formatted_week = f'{week}:'  # Add colon here to match your desired output
        workout_plan[formatted_week] = {}
        for lift, training_max in training_maxes.items():
            # Format the output with "reps" and "lbs" as specified
            workout_plan[formatted_week][lift] = [
                (f'{reps} reps', f'{round(training_max * perc / 5) * 5}lbs') for reps, perc in reps_and_percs
            ]

    return workout_plan


#######################################################################################################
#######################################################################################################


## Test Call ##

if __name__ == "__main__":
    # Example 1RM inputs
    my_1rms = (315, 225, 405, 135)  # Replace with your 1RM for squat, bench, deadlift, overhead press
    workout_plan = calculate_wendler_531(my_1rms)

    for week in workout_plan:
        print(f"{week}")
        for lift in workout_plan[week]:
            
            formatted_lift = lift.upper()
            print(f"{formatted_lift}: ")

            formatted_sets = ', '.join(f"({reps}, {weight})" for reps, weight in workout_plan[week][lift])
            print(formatted_sets)
        print()


#######################################################################################################
#######################################################################################################
