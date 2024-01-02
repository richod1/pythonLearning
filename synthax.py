name=str("Degraft frimpong")
print(type(name))

cars=tuple(("benz","toyata"))
print(cars[0])

tenses="""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

greeting="Hello World "
print(greeting.strip())

slogan="We are the so-called \"Vikings\" of the north"
print(slogan)
print(tenses)

print("magna" in tenses)

fruit=str("Banana")
print(len(fruit))
for x in fruit:
    print(x)

#basic calculator
def calculate():
    print("WELCOME TO BASIC CALCULATOR")
    print("Slect yout operation")
    print("1.Addition")
    print("2.Multiplication")
    print("3.Subtraction")
    print("4.Division")


    choice=input("Enter choice (1/2/3/4) :")

    #choice validation
    if choice in ('1','2','3','4'):
        num1=float(input('Enter your value :'))
        num2=float(input('Enter your second value :'))

        #perform conditional
        if choice == '1':
            result=num1+num2
            print("sum of input is ",result)
        elif choice =='2':
            result=num1*num2
            print("Multiplication of input is ",result)
        elif choice == '3':
            result =num1-num2
            print("Minus of input is ",result)
        elif choice == '4':
            result=num1/num2
            print("Division of input is ",result)
        else:
            print("Invalid operation")
    else:
        print("Invalid user input response")

#function call
calculate()