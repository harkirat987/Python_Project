print("enter first number")
n1 = int(input())
print("enter your second number")
n2= int(input())
print("Enter your Operator: +,*,/,-")
Operator = input()

if n1 == 45 and n2 == 3 and operator == "*":
    print(5555)
elif n1== 56 and n2 == 9 and operator == "+":
    print(345)
elif n1 == 59 and n2 == 6 and operator == "/":
    print(332)
elif Operator == "*":
    print(int(n1) * int(n2))
elif Operator == "+":
    print(int(n1) + int(n2))
elif Operator == "+":
    print(int(n1) - int(n2))
elif Operator =="/":
    print(int(n1) / int(n2))
else:
    print("Invalid Input")