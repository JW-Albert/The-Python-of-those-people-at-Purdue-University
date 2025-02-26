Salary = 10

isRunning = True
year = 0
while isRunning:
    year += 1
    print("=================================")
    print("The {:02d}th year".format(year))

    print("Employee salary is: ", Salary)
    print("Choose an option:")
    print("1. Raise salary")
    print("2. Cut salary")
    print("3. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        Salary *= 1.03
    
    elif option == 2:
        Salary *= 0.97
    
    elif option == 3:
        isRunning = False

    else:
        print("Invalid option")

print("=================================")
print("Employee salary is: ", Salary)