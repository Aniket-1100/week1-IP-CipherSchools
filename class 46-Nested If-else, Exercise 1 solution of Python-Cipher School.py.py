winning_number = 27
a = int(input("guess any two digit number: "))
if a == winning_number:
    print("YOU WIN")

else:
    if a > winning_number:
        print("TOO HIGH")
    else:
        print("TOO LOW")