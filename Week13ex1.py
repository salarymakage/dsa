# Power Function
def power_recursive(a, n):
    if n == 0:
        return 1
    else:
        return a * power_recursive(a, n-1)

def power_non_recursive(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# Reverse Number Function
def reverse_recursive(n):
    n_str = str(n)
    if len(n_str) == 1:
        return n
    else:
        return int(n_str[-1]) * (10 ** (len(n_str) - 1)) + reverse_recursive(int(n_str[:-1]))

def reverse_non_recursive(n):
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n = n // 10
    return reversed_num


def excercies1():
    while True:
        print("1. Calculate power recursively")
        print("2. Calculate power non-recursively")
        print("3. Go back")
        choice = input("Enter your choice (or '3' to go back): ")

        if choice == '3':
            break
        if choice not in ('1', '2'):
            print("Invalid choice, please enter 1 or 2.")
            continue
        
        a = int(input("Enter the base number (a): "))
        n = int(input("Enter the exponent number (n): "))

        if choice == '1':
            print(f"Recursive result: {power_recursive(a, n)}")
            input("Press Enter key to continue...")
        elif choice == '2':
            print(f"Non-Recursive result: {power_non_recursive(a, n)}")
            input("Press Enter key to continue...")

def excersice2():
    while True:
        print("1. Reverse a number recursively")
        print("2. Reverse a number non-recursively")
        print("3. Go back")
        choice = input("Enter your choice (or '3' to go back): ")

        if choice == '3':
            break
        if choice not in ('1', '2'):
            print("Invalid choice, please enter 1 or 2.")
            continue
        
        num = int(input("Enter the number to reverse: "))

        if choice == '1':
            print(f"Reverse Recursive result: {reverse_recursive(num)}")
            input("Press Enter key to continue...")
        elif choice == '2':
            print(f"Reverse Non-Recursive result: {reverse_non_recursive(num)}")
            input("Press Enter key to continue...")

# Display function
def display():
    while True:
        print("Choose an exercise to perform:")
        print("1. Exercise 1 - Power Calculation")
        print("2. Exercise 2 - Reverse Number")
        print("3. Exit Program")
        option = input("Enter your option (or '3' to exit): ")

        if option == '3':
            print("Exiting the program.")
            break
        if option == '1':
            excercies1()
        elif option == '2':
            excersice2()
        else:
            print("Invalid option, please enter 1, 2, or 3.")

display()
