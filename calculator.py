num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: "))
while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        print("result=",num1+num2)
    elif choice==2:
        print("result=",num1-num2)
    elif choice==3:
        print("result=",num1*num2)
    elif choice==4:
        if num2!=0:
            print("result=",num1/num2)
        else:
            print("division by zero is not allowed")
    elif choice==5:
        print("----exiting program----")
        break
    else:
        print("----invalid choice----")
