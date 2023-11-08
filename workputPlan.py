# def calculat_sets_program(lift):
#     print('WEEK 1 - For maximum bench of', lift)
#     print('Set 1:', str(lift * .65))
#     print('Set 2:', str(lift * .75))
#     print('Set 3:', str(lift * .85))

# def calculat_sets_WEEK_2(lift):
#     print('WEEK 2 - For maximum bench of', lift)
#     print('Set 1:', str(lift * .70))
#     print('Set 2:', str(lift * .80))
#     print('Set 3:', str(lift * .90))

# def calculat_sets_WEEK_3(lift):
#     print('WEEK 3 - For maximum bench of', lift)
#     print('Set 1:', str(lift * .75))
#     print('Set 2:', str(lift * .85))
#     print('Set 3:', str(lift * .95))

# def calculat_sets(lift):
#     calculat_sets_program(lift)
#     calculat_sets_WEEK_2(lift)
#     calculat_sets_WEEK_3(lift)

# calculat_sets(315)  
################################################################################################
# WEEK ONE

# def program(lift, max_squat, max_ohp, max_deadlift):
#     print("WEEK 1 bench set weights:")
#     print("Set 1: " + str(lift * .65))
#     print("Set 2: " + str(lift * .75))
#     print("Set 3: " + str(lift * .85))

#     print("WEEK 1 squat set weights:")
#     print("Set 1: " + str(max_squat * .65))
#     print("Set 2: " + str(max_squat * .75))
#     print("Set 3: " + str(max_squat * .85))

#     print("WEEK 1 OHP set weights:")
#     print("Set 1: " + str(max_ohp * .65))
#     print("Set 2: " + str(max_ohp * .75))
#     print("Set 3: " + str(max_ohp * .85))

#     print("WEEK 1 deadlift set weights:")
#     print("Set 1: " + str(max_deadlift * .65))
#     print("Set 2: " + str(max_deadlift * .75))
#     print("Set 3: " + str(max_deadlift * .85))

# program(315, 405, 225, 495)
from ssl import OP_CIPHER_SERVER_PREFERENCE


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

# def program_lifts():
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             print(set)

       

# current_lift = program_lifts()


# def program_sets():
#     for set in sets:
#         print(set)

# set_number = program_sets()
#######################################################################################
# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def program_lifts():
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
            

       

# current_lift = program_lifts(), WEEK_2_lifts(), WEEK_3_lifts("225")
###########################################################################################
# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def program_lifts(deadlift):
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             if set == sets[0]:
#                 print(set + str(float(deadlift) * .65))
#             # print(set)

# current_lift = program_lifts("225")

##########################################################################################

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def program_lifts(deadlift):
#     for lift in lifts:
#         print("WEEK 1: " + str(lift) + " set weights:")
#         for set in sets:
#             if set == sets[0]:
#                 print(set + str(float(deadlift) * .65))
#             elif set == sets[1]:
#                 print(set + str(float(deadlift) * .75))
#             else:
#                 print(set + str(float(deadlift) * .85))

# current_lift = program_lifts("225")
 ############################################################################################

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")


# def program_lifts(deadlift):
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

# current_lift = program_lifts("225")
##############################################################################

# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")
# # percentages = ((.65, .75, .85), (.70, .80, .90), (.76, .85, .95)) # consider loop for precentages ???
# # weeks = (1, 2, 3) # consider loop for weeks ???

# def program(bench, squat, OHP, deadlift):
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

# current_lift = program("315", "405", "225", "495")
###########################################################################################
# lifts = ("bench", "squat", "OHP", "deadlift")
# sets = ("Set 1: ", "Set 2: ", "Set 3: ")
# # percentages = ((.65, .75, .85), (.70, .80, .90), (.76, .85, .95)) # consider loop for precentages ???
# weeks = (1, 2, 3) # consider loop for weeks ???


# def program(bench, squat, OHP, deadlift):
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

# current_lift = program("315", "405", "225", "495")

##############################################################################################

lifts = ("bench", "squat", "OHP", "deadlift")
sets = (1, 2, 3)
percentages = ((.65, .75, .85), (.70, .80, .90), (.75, .85, .95)) # consider loop for precentages ???
weeks = (1, 2, 3) # consider loop for weeks ???
week_headers = ("WEEK 1", "WEEK 2", "WEEK 3")

data = {
  "WEEK 1": { 
    "bench": (.65, .75, .85),
    "squat": (.65, .75, .85),
    "OHP": (.65, .75, .85),
    "deadlift": (.65, .75, .85)
  },
  "WEEK 2": { 
    "bench": (.70, .80, .90),
    "squat": (.70, .80, .90),
    "OHP": (.70, .80, .90),
    "deadlift": (.70, .80, .90)
  },
  "WEEK 3": { 
    "bench": (.75, .85, .95),
    "squat": (.75, .85, .95),
    "OHP": (.75, .85, .95),
    "deadlift": (.75, .85, .95)
  },
}

def program(bench, squat, OHP, deadlift):
        for week_header in week_headers:
            for lift in lifts:
                print(week_header + ": " + str(lift) + " set weights:")
                for set in sets:
                    if lift == "bench":
                        max_weight = bench
                    elif lift == "squat":
                        max_weight = squat
                    elif lift == "OHP":
                        max_weight = OHP
                    else:
                        max_weight = deadlift

                    weight = str(float(max_weight) * data[week_header][lift][set - 1])
                    print("Set", str(set) + ":", str(weight))
            

current_lift = program("315", "405", "225", "495") 