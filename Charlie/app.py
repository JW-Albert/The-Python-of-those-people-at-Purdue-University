from subfun import SB 

def main():
    print("Hello from main in app.py")
    print(__name__)
    print("=====")
    SB()

print("app.py is being run directly")

if __name__ == "__main__":
    main()