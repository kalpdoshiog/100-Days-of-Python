print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
    # print("You have selected Small Pizza")
    if pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    # print("You have selected Medium Pizza")
    if pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
else:
    bill = 25
    # print("You have selected Large Pizza")
    if pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}.")

