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
