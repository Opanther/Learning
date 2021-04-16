#type conversion using float 
# nested statement example 
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))
# Using Boolean variables
if gpa >= .85 and  lowest_grade >= .70:
    honour_roll = True 
else: 
    honour_roll = False 


if honour_roll: 
    print('You made honour roll')