print ("------------SIMPLE CALCULATOR-------------")

num1=float(input("Enter First number for calculation:"))
num2=float(input("Enter second number for calculation:"))
def show_menu():
    
    print("******Choose an operation which you want to perform:******")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Modulus(%)")
    print("6.Floor(//)")
    print("7.Exit")

while True:
    show_menu()
    
    choice=input("\tEnter your choice(1-4):")

    if choice=='1':
        result = num1+num2
        print("Result:",result)

    elif choice=='2':
        result = num1-num2
        print("Result:",result)

    elif choice=='3':
        result = num1*num2
        print("Result:" ,result)

    elif choice=='4':
        if num2 != 0:
            result = num1 /num2
            print("Result:",result)

        else:
            print("Error: Division by zero is not allowed")

    elif choice=='5':
        result =num1 % num2
        print("Result:",result)

    elif choice=='6':
        result=num1 // num2
        print("Result:",result)

    elif choice=='7':
        print("Exit.....see you soon..")
        break
    

    else:
        print("******Invalid choice******")
        
    
    
