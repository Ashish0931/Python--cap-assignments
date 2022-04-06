selector = input("enter the action you want to perform: (+,-,*,/)")
num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
condition=True
while(condition==True):

    if selector=="+":
        print(num1+num2)
        condition=False
    elif (selector=="-"):
        print(num1-num2)
        condition=False
    elif(selector=="*"):
        print(num1*num2)
        condition=False
    elif(selector=="/"):
        print("num1/num2")
        condition=False
    else:
        print("wrong value entered! try again! ")
        condition=True