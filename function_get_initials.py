# This function will return the first initial of a name
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


# Ask for someones name and return the initials
first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name,False)

middle_name = input('Enter your middle name:')
middle_name_initial = get_initial(middle_name,True)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name,False)

print('Your initials are: ' + first_name_initial  + middle_name_initial + last_name_initial)

# One can use name notation to call function
#1 it makes the code easier to read 
#2 the function parameters can be called in any order