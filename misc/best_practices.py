
# F-srtings!!!!!
f'#{i+1}: {item.title():<10s} = {round(count)}'

# inline conditional statements
int(red_str[0]) if red_str[0] else 0

# Unpacking a tuple. 
Ex:
f = (1,2,3,4)
one, two, three, four = f
# This is easier than:
one = f[0]
# this is catch all unpacking
oldest, second_oldest, *others = car_ages_descending


# Using unpacking to swap variables. 
# a = 1
# b = 0
# We want a = 0 and b = 1

b, a = a, b  # Swap

# Using a temp variable to swap variables


temp = a # temp, a = 1
a = b # a, b = 0
b = temp # b = 1

# Walrus operator
# not sure i get :=
