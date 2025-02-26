import random
import string

def generater():
    letters = string.ascii_lowercase
    firatLetter = random.choice(letters)
    secondLetter = random.choice(letters)
    digit = str(random.randint(0, 9))

    pair = [firatLetter, secondLetter, digit]
    password = ""
    for i in range(0, 3):
        randomChoice = random.choice(pair)
        password += randomChoice
        pair.remove(randomChoice)
    
    return password

print("Password:", generater())
