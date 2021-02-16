__author__ = "Laurine"

# Question

# Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
# of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
# contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
# spaces. For example, for n = 4 the triangle should appear as follows:

rows = 7

# introducing the step parameter to define the decrement
for i in range(rows, 0, -2):
    for j in range(0, rows, -2):
        print("*", end=" ")
    # for every row, print an arterisk and a space multiplied by the row number
    print(" *" *i)



