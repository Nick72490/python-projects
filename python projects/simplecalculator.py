def calculator():
    while True:
        print("simple python calculator")
        try:
            a = int(input("number: "))
            x = int(input("number: "))
        except ValueError:
            print("can only use numbers")
            continue

        while True:
            print("1.+ plus")
            print("2.- minus")
            print("3./ divide")
            print("4.* times")
            print("type 'quit' to stop")
            f = input()

            if f == "quit":
                return  

            if f in ("+", "1"):
                result = a + x
                break
            elif f in ("-", "2"):
                result = a - x
                break
            elif f in ("/", "3"):
                result = a / x
                break
            elif f in ("*", "4"):
                result = a * x
                break
            else:
                print("can only use the given options")
                continue

        print("Result:", result)
calculator()
