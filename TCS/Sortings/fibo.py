#find python fibonacci series for given range

number = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
count = 0

if number <= 0:
    print("Please enter a positive integer")
elif number == 1:
    print("Fibonacci series upto",number,":")
    print(n1)
else:
    print("Fibonacci series:")
    while count < number:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

        