'''
14.03.2024, Thu
Hokyeong Grace Lee
'''

print("\nHi! :DDDDDD \n\n"
      "Here is a mini calculator for simple calculations.\n")
print("*** Step 1: Enter two integers of your choice."
      " Mind the order of the numbers.\n")

# Get user input as a string
userInput = input("\t Please enter two numbers separated by comma and a space "
                  "(e.g. 5, 6): ")

# Split the string into two
numbers = userInput.split(", ")

# Checking if the input is indeed two numbers
if len(numbers) != 2:
    print("Invalid Input! Try again.")
else:
    try:
        num1 = int(numbers[0])
        num2 = int(numbers[1])

        # print("You entered:", num1, ",", num2, ".")
        print(f"\n\t You entered {num1} and {num2}\n")
    except ValueError:
        print("Invalid Input! Try again.")

print("\n*** Step 2: Choose which arithmetic operation"
      " you would like to perform.\n")
print("\t 1. Addition")
print("\t 2. Subtraction")
print("\t 3. Multiplication")
print("\t 4. Division")
print("\t 5. Modulus")
print("\t 6. Exponentiation\n")

# Get user choice
choice = input("Now, enter your choice of operation (1 - 6): ")

# Process user choice
if choice == '1':
    print("\n\tYou chose ADDITION,")
    print(f"\tand the result is {num1 + num2}")
    print("\nNow you may exit this program. Thank you.\n")
elif choice == '2':
    print("\n\tYou chose SUBTRACTION,")
    print(f"\tand the result is {num1 - num2}")
    print("\nNow you may exit this program. Thank you.\n")
elif choice == '3':
    print("\n\tYou chose MULTIPLICATION,")
    print(f"\tand the result is {num1 * num2}")
    print("\nNow you may exit this program. Thank you.\n")
elif choice == '4':
    print("\n\tYou chose DIVISION,")
    print(f"\tand the result is {num1 / num2}")
    print("\nNow you may exit this program. Thank you.\n")
elif choice == '5':
    print("\n\tYou chose MODULUS,")
    print(f"\tand the result is {num1 % num2}")
    print("\nNow you may exit this program. Thank you.\n")
elif choice == '6':
    print("\n\tYou chose EXPONENTIATION,")
    print(f"\tand the result is {num1 ** num2}")
    print("\nNow you may exit this program. Thank you.\n")
else:
    print("\nInvalid choice. Please enter a valid option.")
