__author__ = "Laurine"

# Question
# Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
# should consist of n rows, where n is a given positive integer, and consecutive rows should
# contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:

# Specify the number of rows
rows = 5


for i in range(1, rows+1):
    # for every row, print an arterisk and a space multiplied by the row number
    print("* " *i)