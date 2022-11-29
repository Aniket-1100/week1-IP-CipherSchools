name,char = input("enter comma seperated name and character: " ).split(",")
print(f"length of your name and is {len(name)}")
print(f"character count: {name.lower().count(char.lower())}")