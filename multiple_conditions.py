country = input('What country do you live in? ')
#Nested if function

if country == 'Canada':

    province = input('What province/state do you live in? ')

    if province in ('Alberta','Nunavut','Yukon'):
        tax = 0.05 
    elif province == 'Ontario':
        tax = 0.13
    else: 
        tax = 0.15
    print(tax)
else:
    tax = 0.0
    