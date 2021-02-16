__author__ = "Laurine"

# Question: Print a symmetrical triangle of rows 7 with the top most part containing a single star while the bottom
# most part has 7 stars


# Function to demonstrate printing pattern triangle

n = 7
# number of spaces
k = n - 1

# outer loop to handle number of rows
for i in range(0, n):
    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, k):
        print(end=" ")

    print("\r")
    # decrementing k after each loop
    k = k - 1

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")


        # ending line after each row
print()

