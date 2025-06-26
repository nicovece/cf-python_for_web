first_term = int(input("Enter the first term: "))
second_term = int(input("Enter the second term: "))
operation = input("Enter the operation: ")

if operation == "+":
    print(f"The sum of {first_term} and {second_term} is {first_term + second_term}")
elif operation == "-":
    print(f"The difference of {first_term} and {second_term} is {first_term - second_term}")
else:
    print("Unknown operation")