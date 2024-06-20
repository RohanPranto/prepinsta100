##Remove All Characters Other Than Alphabets

name=input("Enter a string: ")
alphabets="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
for i in name:
    if i not in alphabets:
        print(i, end="")
