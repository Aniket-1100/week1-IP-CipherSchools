num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
print(f"average of three numbers : {(int(num1)+int(num2)+int(num3))/3}")

num1,num2,num3 = input("enter three numbers comma seperated: ").split(",")
print(f"average of three numbers : {(int(num1)+int(num2)+int(num3))/3}")