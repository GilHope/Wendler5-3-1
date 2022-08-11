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

###########################################################################################

print("#############################################################")
#######################################################################################
# set_number = range(3)
# lifts = ("bench", "squat", "OHP", "deadlift")

# def WEEK_header():
#     print("WEEK 1: bench set weights:")
#     for lift in lifts:
#         count_1 = 0
#         while count_1 <= 3:
#             count_1 += 1
#     for set in set_number:
#         count_2 = 1
#         while count_2 <= 3:
#             count_2 += 1
#     print("Set " + str(count_2) + ": " +)
    

# WEEK_header()



# def WEEK_header():
#     print("WEEK 1: bench set weights:")
#     for set in set_number:
#         count = 1
#         while count <= 3:
#             count += 1
#     print("Set " + str(count) + ": " +)

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")

# def WEEK_1_lifts():
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             print(set)

       

# current_lift = WEEK_1_lifts()


# def WEEK_1_sets():
#     for set in sets:
#         print(set)

# set_number = WEEK_1_sets()
#######################################################################################
# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def WEEK_1_lifts():
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             print(set)

# def WEEK_2_lifts():
#     for lift in lifts:
#         print("WEEK 2: " + str(lift) + " set weights:")
#         for set in sets:
#             print(set)

# def WEEK_3_lifts(deadlift):
#     for lift in lifts:
#         print("WEEK 3: " + str(lift) + " set weights:")
#         for set in sets:
#             print(set + str(float(deadlift) * .65))       
            

       

# current_lift = WEEK_1_lifts(), WEEK_2_lifts(), WEEK_3_lifts("225")
###########################################################################################
# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def WEEK_1_lifts(deadlift):
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             if set == sets[0]:
#                 print(set + str(float(deadlift) * .65))
#             # print(set)

# current_lift = WEEK_1_lifts("225")

##########################################################################################

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def WEEK_1_lifts(deadlift):
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             if set == sets[0]:
#                 print(set + str(float(deadlift) * .65))
#             elif set == sets[1]:
#                 print(set + str(float(deadlift) * .75))
#             else:
#                 print(set + str(float(deadlift) * .85))

# current_lift = WEEK_1_lifts("225")
 ############################################################################################

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def WEEK_1_lifts(deadlift):
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             if lift == lifts[3]:
#                 if set == sets[0]:
#                     print(set + str(float(deadlift) * .65))
#                 elif set == sets[1]:
#                     print(set + str(float(deadlift) * .75))
#                 else:
#                     print(set + str(float(deadlift) * .85))

# current_lift = WEEK_1_lifts("225")
##############################################################################

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")
# # percentages = ((.65, .75, .85), (.70, .80, .90), (.76, .85, .95)) # consider loop for precentages ???
# # weeks = (1, 2, 3) # consider loop for weeks ???

# def WEEK_1(bench, squat, OHP, deadlift):
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             # BENCH SETS
#             if lift == lifts[0]:
#                 if set == sets[0]:
#                     print(set + str(float(bench) * .65))
#                 elif set == sets[1]:
#                     print(set + str(float(bench) * .75))
#                 else:
#                     print(set + str(float(bench) * .85))
#             # SQUAT SETS
#             elif lift == lifts[1]:
#                 if set == sets[0]:
#                     print(set + str(float(squat) * .65))
#                 elif set == sets[1]:
#                     print(set + str(float(squat) * .75))
#                 else:
#                     print(set + str(float(squat) * .85))
#             # OHP SETS
#             elif lift == lifts[2]:
#                 if set == sets[0]:
#                     print(set + str(float(OHP) * .65))
#                 elif set == sets[1]:
#                     print(set + str(float(OHP) * .75))
#                 else:
#                     print(set + str(float(OHP) * .85))
#             # DEADLIFT SETS
#             else:
#                 if set == sets[0]:
#                     print(set + str(float(deadlift) * .65))
#                 elif set == sets[1]:
#                     print(set + str(float(deadlift) * .75))
#                 else:
#                     print(set + str(float(deadlift) * .85))

# current_lift = WEEK_1("315", "405", "225", "495")
###########################################################################################
# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")
# # percentages = ((.65, .75, .85), (.70, .80, .90), (.76, .85, .95)) # consider loop for precentages ???
# weeks = (1, 2, 3) # consider loop for weeks ???


# def WEEK_1(bench, squat, OHP, deadlift):
#     for week in weeks:
#         if week == weeks[0]:
#             for lift in lifts:
#                 print("WEEK 1: " + str(lift) + " set weights:")
#                 for set in sets:
#                     # BENCH SETS
#                     if lift == lifts[0]:
#                         if set == sets[0]:
#                             print(set + str(float(bench) * .65))
#                         elif set == sets[1]:
#                             print(set + str(float(bench) * .75))
#                         else:
#                             print(set + str(float(bench) * .85))
#                     # SQUAT SETS
#                     elif lift == lifts[1]:
#                         if set == sets[0]:
#                             print(set + str(float(squat) * .65))
#                         elif set == sets[1]:
#                             print(set + str(float(squat) * .75))
#                         else:
#                             print(set + str(float(squat) * .85))
#                     # OHP SETS
#                     elif lift == lifts[2]:
#                         if set == sets[0]:
#                             print(set + str(float(OHP) * .65))
#                         elif set == sets[1]:
#                             print(set + str(float(OHP) * .75))
#                         else:
#                             print(set + str(float(OHP) * .85))
#                     # DEADLIFT SETS
#                     else:
#                         if set == sets[0]:
#                             print(set + str(float(deadlift) * .65))
#                         elif set == sets[1]:
#                             print(set + str(float(deadlift) * .75))
#                         else:
#                             print(set + str(float(deadlift) * .85))
#         elif week == weeks[1]:
#             for lift in lifts:
#                 print("WEEK 2: " + str(lift) + " set weights:")
#                 for set in sets:
#                     # BENCH SETS
#                     if lift == lifts[0]:
#                         if set == sets[0]:
#                             print(set + str(float(bench) * .70))
#                         elif set == sets[1]:
#                             print(set + str(float(bench) * .80))
#                         else:
#                             print(set + str(float(bench) * .90))
#                     # SQUAT SETS
#                     elif lift == lifts[1]:
#                         if set == sets[0]:
#                             print(set + str(float(squat) * .70))
#                         elif set == sets[1]:
#                             print(set + str(float(squat) * .80))
#                         else:
#                             print(set + str(float(squat) * .90))
#                     # OHP SETS
#                     elif lift == lifts[2]:
#                         if set == sets[0]:
#                             print(set + str(float(OHP) * .70))
#                         elif set == sets[1]:
#                             print(set + str(float(OHP) * .80))
#                         else:
#                             print(set + str(float(OHP) * .90))
#                     # DEADLIFT SETS
#                     else:
#                         if set == sets[0]:
#                             print(set + str(float(deadlift) * .70))
#                         elif set == sets[1]:
#                             print(set + str(float(deadlift) * .80))
#                         else:
#                             print(set + str(float(deadlift) * .90))

# current_lift = WEEK_1("315", "405", "225", "495")

##############################################################################################

lifts = ("bench", "squat", "OHP", "deadlift")
sets = ("Set 1: ", "Set 2: ", "Set 3: ")
percentages = ((.65, .75, .85), (.70, .80, .90), (.76, .85, .95)) # consider loop for precentages ???
weeks = (1, 2, 3) # consider loop for weeks ???
week_headers = ("WEEK 1: ", "WEEK 2: ", "WEEK 3: ")


def WEEK_1(bench, squat):
        for week_header in week_headers:
            for lift in lifts:
                print(week_header + str(lift) + " set weights:")
                for set in sets:
                    print(set)
                
                    

current_lift = WEEK_1("315", "405")
