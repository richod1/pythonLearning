#python basic calculator
def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!= 0:
        return x/y
    else:
        return "Error Divided by zero"
    
def calculator():
    print("Choose Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice=input("Enter Operation 1/2/3/4 :")

    if choice in ("1","2","3","4"):
        num1=float(input("Enter first Value :"))
        num2=float(input("Enter Second Value :"))

        if choice=='1':
            print(num1,"+",num2, "=" ,addition(num1,num2))
        elif choice=='2':
            print(num1,"-",num2, "=" ,subtraction(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1, "/",num2, "=",divide(num1,num2))
        else:
            print("Invalid input please input a valid choice (1/2/3/4)")

if __name__ == "__main__":
    calculator()
