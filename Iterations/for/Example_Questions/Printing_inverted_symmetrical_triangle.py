__author__ = "Laurine"

# Question

# Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
# of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
# contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
# spaces. For example, for n = 4 the triangle should appear as follows:

rows = 5

for i in range(rows, 1):
    print(" *" *i-1)
