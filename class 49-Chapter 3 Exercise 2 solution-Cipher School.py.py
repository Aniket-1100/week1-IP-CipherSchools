name,age = input("Enter comma seperated name and age: ").split(",")
if name[0]=='A' or name[0]=='a' and int(age)>10:
    print("you can watch coco movie")
else:
    pirnt("sorry,you cannot watch coco movie")