for i in range(int(input("Enter a number: "))):
         print(chr(65 + i) * (i + 1))

#output
# Enter a number: 5
# A
# BB
# CCC
# DDDD
# EEEEE

#######################################

for i in range(1,int(input("Enter a number: "))+1):
        print("*"*i)

# Output
# Enter a number: 4
# *
# **
# ***
# ****

#######################################

n=int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line after each row
    print()

# Output
# Enter the number of rows: 5
#     *
#    ***
#   *****
#  *******
# *********

#######################################
n=int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print(chr(64+i), end="")
    # Move to the next line after each row
    print()

# Output
# Enter the number of rows: 5
#     A
#    BBB
#   CCCCC
#  DDDDDDD
# EEEEEEEEE

#######################################


