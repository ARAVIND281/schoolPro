choice = "y"
while choice == "y" or choice =="Y":
    a=int(input("Enter 1st no "))
    b=int(input("Enter 2nd no "))
    op=input("Enter the operator (+,-,*,/) ")
    if(op=="+"):
        c=a+b
        print("Sum = ",c)
    elif(op=="*"):
        c=a*b
        print("Product = ",c)
    elif(op=="-"):
        if(a>b):
            c=a-b
        else:
            c=b-a
            print("Difference = ",c)
    elif(op=="/"):
        if b!= 0:
            c=a/b
            print("Division = ",c)
        else:
            print("Division not possible")
    else:
        print("Invalid operator")
        print ()
    choice=input("Do you want to continue y/n")
