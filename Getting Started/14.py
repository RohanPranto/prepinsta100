# find out armstrong number or not

num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

if num == sum_of_powers:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
