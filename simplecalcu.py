def calcu():
    print("SELECT OPERATION:")
    print("\n[1]Addition")
    print("\n[2]Subtraction")
    print("\n[3]Multiplication")
    print("\n[4]Division\n")

    user = int(input("Enter Choices: ")) 
    if user == 1:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        result = a+b
        print("Result is: ",result)

    elif user == 2:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number; "))
        result = a-b
        print("Result is: ",result)

    elif user == 3:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        result = a*b
        print("Result is: ",result)

    elif user == 4:
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        result = a/b
        print("Answer: ",result)
    else:
        print("invalid")
    
calcu()