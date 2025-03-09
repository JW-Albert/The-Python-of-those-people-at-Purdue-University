import os

x = 1
try:
    while True:
        x *= 10
        print("{} * 10 = {}".format(x//10, x))
except OverflowError:
    os.system("cls")
    print("============================================")
    print("OverflowError: {} is too large".format(x))