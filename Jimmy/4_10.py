import random ,os

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2

    os.system("clear")
    user_answer = input(f"{num1} x {num2} = ")

    if not user_answer.isdigit() or int(user_answer) != correct_answer:
        print("Incorrect! Game Over!")
        break

    print("Correct!")
    if input("Countinued？（yes/no）：").lower() != "yes":
        break
