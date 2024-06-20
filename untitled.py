name= input("Enter your name: ")
vowels="aeiouAEIOU"

for i in name:
    if i not in vowels:
        print(i, end="")
