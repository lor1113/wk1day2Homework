# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

print([x for x in numbers if (x%2==0)])

# 2. Print the difference between the largest and smallest value:

print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
two = False
for number in numbers:
    if number == 2:
        if two:
            print(True)
        else:
            two = True
    else:
        two = False



# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

sum1 = 0
sum2 = 0
six = False

for number in numbers:
    if number == 6:
        sum2 = 6
        six = True
    elif number == 7 and six:
        sum2 = 0
        six = False
    elif six:
        sum2 += number
    else:
        sum1 += number

sum1 += sum2
print(sum1)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total = 0
thirteen = False

for number in numbers:
    if number == 13:
        thirteen = True
    elif thirteen:
        thirteen = False
    else:
        total += number

print(total)




