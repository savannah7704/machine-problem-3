'''
Name: Savannah Stumpf
Date: 5/3/2026
Course Name: Artificial Intelligence
Semester: Spring 2026
Assignment Name: Machine Problem 3
'''

import numpy
import pandas
import constraint
from constraint import *

# I'm doing the implementation where every hour is filled with an activity

# variables:
work1 = "Work1"
work2 = "Work2"
work3 = "Work3"
work4 = "Work4"
lunch = "Lunch"
exercise = "Exercise"
shopping = "Shopping"
meeting = "Meeting"
reading = "Reading"
cleaning = "Cleaning"
activities = [work1, work2, work3, work4, lunch, exercise, shopping, meeting, reading, cleaning]
# 10 hours to fill:
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

problem = Problem()
problem.addVariables(activities, hours)

# making sure each activity is during a different hour:
problem.addConstraint(AllDifferentConstraint())

# making sure lunch is always at 11am or 12pm:
problem.addConstraint(SomeInSetConstraint({3, 4}), [lunch])

# making sure the meeting is always before 5pm:
problem.addConstraint(SomeInSetConstraint({1, 2, 3, 4, 5, 6, 7, 8}), [meeting])

# making sure the work hours are consecutive:
def consecutive_contraint(w1, w2, w3, w4):
    # w2 always after w1 and w3 always after w2 while w4 is anytime after w3
    return (w2 == w1 + 1 and w3 == w2 + 1 and w4 > w3)

problem.addConstraint(consecutive_contraint, [work1, work2, work3, work4])

# making sure lunch is always before exercise:
def prerequisite_constraint(l, e):
    return (l < e)
    
problem.addConstraint(prerequisite_constraint, [lunch, exercise])

hours_map = {1: "9am", 2: "10am", 3: "11am", 4: "12pm", 5: "1pm", 6: "2pm", 7: "3pm", 8: "4pm", 9: "5pm", 10: "6pm"}

solutions = problem.getSolutions()

print("CLASS: Artificial Intelligence, Lewis University\n")
print("NAME: Savannah Stumpf\n")
print("SEMESTER: Spring 2026\n")

print("Number of schedules is", len(solutions), "\n")
print("First Possible Schedule\n")
    
first_schedule = solutions[0]
first = pandas.Series(first_schedule)
first = first.sort_values()
first = first.map(hours_map)
print(first)

print("")
print("Last Possible Schedule\n")

last_schedule = solutions[-1]
last = pandas.Series(last_schedule)
last = last.sort_values()
last = last.map(hours_map)
print(last)