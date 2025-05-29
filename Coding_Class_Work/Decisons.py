first = int(input("What is the first number? "))
second = int(input("What is the second number? "))

if first > second:
    print("The first number is greater")

if first == second:
    print("The numbers are equal")

if second > first:
    print("The second number is greater")

print() 

user_animal = input("What is your favorite animal? ")

if user_animal.lower() == "elephant":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")