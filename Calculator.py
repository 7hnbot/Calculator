def Calculator(n) :
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    if n==1 :
        print("Sum:",a+b)
    elif n==2 :
        print("Difference:",a-b)
    elif n==3 :
        print("Multiplication:",a*b)
    elif n==4 :
        if b!=0 :
            print("Division:",a/b)
        else :
            print("Error! Division by zero.")
while(True) :
    print("\nEnter 1 to add\nEnter 2 to sub\nEnter 3 to multiply\nEnter 4 to divide\nEnter 0 to quit\n")
    try :
        n=int(input("Enter your choice: "))
        if n in [1,2,3,4] :
            Calculator(n)
        elif n==0 :
            print("Thanks for using it....!!")
            quit()
        else :
            print("Enter valid input.")
    except :
        print("Error! Enter numeric inputs")

