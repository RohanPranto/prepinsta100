string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string: ", reversed_string)


# another approach
# def reverse_string(string):
#     stack = []
#     reversed_string = ""
#     for char in string:
#         stack.append(char)
#     while stack:
#         reversed_string += stack.pop()
#     return reversed_string
# print(reverse_string(string)) 
