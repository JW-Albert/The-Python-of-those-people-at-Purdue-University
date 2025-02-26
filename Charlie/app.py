import subfun

def main():
    print("Hello from main in app.py")
    print(__name__)
    print("=====")
    subfun.main()

print("app.py is being run directly")

if __name__ == "__main__":
    main()