def hello(user_name):
    print(f'Hello {user_name}, here are your weights')

hello("Gilchan")

# Workout 1
# Set 1 = ((max) * .65)
# Set 2 = ((max) * .75)
# Set 3 = ((max) * .85)

working_max = 315

# set_1 = (working_max * .65)
# set_2 = (working_max * .75)
# set_3 = (working_max * .85)

# print("For set 1 I want to lift " + str(set_1) + " for five reps")
# print("For set 2 I want to lift " + str(set_2) + " for five reps")
# print("For set 3 I want to lift " + str(set_3) + " for five reps")

######################################################################



# def week_1(working_max):
#     print("For set 1 in week 1 I want to lift " + str(set_1) + " for five reps")
#     print("For set 2 in week 1 I want to lift " + str(set_2) + " for five reps")
#     print("For set 3 in week 1 I want to lift " + str(set_3) + " for five reps")

print()




max_bench = 315
max_squat = 405
max_ohp = 225
max_deadlift = 495


# WEEK ONE
def week_1(max_bench, max_squat, max_ohp, max_deadlifts):
    print("These are your Week 1 set bench weights:")
    print("Set 1: " + str(max_bench * .65))
    print("Set 2: " + str(max_bench * .75))
    print("Set 3: " + str(max_bench * .85))

    print("These are your Week 1 set squat weights:")
    print("Set 1: " + str(max_squat * .65))
    print("Set 2: " + str(max_squat * .75))
    print("Set 3: " + str(max_squat * .85))

    print("These are your Week 1 set OHP weights:")
    print("Set 1: " + str(max_ohp * .65))
    print("Set 2: " + str(max_ohp * .75))
    print("Set 3: " + str(max_ohp * .85))

    print("These are your Week 1 set deadlift weights:")
    print("Set 1: " + str(max_deadlift * .65))
    print("Set 2: " + str(max_deadlift * .75))
    print("Set 3: " + str(max_deadlift * .85))

week_1(max_bench, max_squat, max_ohp, max_deadlift)














# # WEEK TWO
# def week_2(max_bench):
#     print("These are your Week 2 set weights:")
#     print("Set 1: " + str(max_bench * .7))
#     print("Set 2: " + str(max_bench * .8))
#     print("Set 3: " + str(max_bench * .9))

# week_2(max_bench)

# # WEEK THREE
# def week_3(max_bench):
#     print("These are your Week 3 set weights:")
#     print("Set 1: " + str(max_bench * .75))
#     print("Set 2: " + str(max_bench * .85))
#     print("Set 3: " + str(max_bench * .95))

# week_3(max_bench)