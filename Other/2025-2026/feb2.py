# guest_name = input("Enter the guest's name: ")

# with open("guests.txt", "a") as file:
#     file.write(guest_name + "\n")

# print(f"Guest '{guest_name}' has been added to the guest list.")

# guest_name = input("Enter the guest's name: ")

# with open("guests.txt", "a") as file:
#     while True:
#         file.write(guest_name + "\n")
#         more = input("Would you like to add another guest? (y/n): ").strip().lower()
#         if more == 'y':
#             guest_name = input("Enter the guest's name: ")
#         else:
#             break

# print("Guest list updated.")


# reason = input("Enter the reason for why do you like programming: ")

# with open("reasons.txt", "a") as file:
#     while True:
#         file.write(reason + "\n")
#         more = input("Would you like to add another reason? (y/n): ").strip().lower()
#         if more == 'y':
#             reason = input("Enter the reason for why do you like programming: ")
#         else:
#             break

# print("Reasons list updated.")

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

try:
    num_sum = float(number1) + float(number2)
    while True:
        print("Would you like to add more numbers?")
        more = input("(y/n): ").strip().lower()
        if more == 'y':
            number1 = input("Enter the next number: ")
            number2 = input("Enter the next number: ")
            num_sum += float(number1) + float(number2)
        else:
            break
    print(f"The total sum is: {num_sum}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
num_sum = int(number1) + int(number2)


