number=input("Enter a mathematical expression: ")
brackets = ['(', ')', '[', ']', '{', '}']

for i in brackets:
    number = number.replace(i, '') # Replace brackets with empty string
  
print("Expression without brackets:", number)
