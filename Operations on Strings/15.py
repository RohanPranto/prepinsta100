string = input("Enter a string: ")

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
