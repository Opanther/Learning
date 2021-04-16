from datetime import datetime

# Create a function to execute the print time and show task completion
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    # cleaner code 
    # print(datetime.datetime.now())
    print()



# print timestamps to see how long sections of code take to run 

first_name = 'Susan'
print_time('printed first name')
# print('task completed')
# print(datetime.datetime.now())
# print()

for x in range(0,10):
    print(x)
print_time('completed for loop ')
# I can now use the finction created to call the line of code below
# print('task completed')
# print(datetime.datetime.now())
# print()