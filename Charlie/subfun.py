def main():
    print("Hello from main in sunfun.py")
    print(__name__)


def SB():
    print("Hello from subfun in SB.py")
    print(__name__)

print("subfun.py is being run directly")

if __name__ == "__main__":
    main()