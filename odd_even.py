# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
number = input("Enter a number: ")
try:
    number = int(number)
except ValueError as e:
        print("That's not a number")
else:
    if number % 2 == 0:
        print(number, "is ane even number")
    else:
        print(number, "is an odd number")