print("Welcome to Pizza Delivery!")
size = input("Whats six=ze pizza do you want? S, M, L:\n")
pepperoni = input("Do you want pepperoni on your pizza Y/N \n")
extra_cheese = input("Do you want extra cheese on your pizza Y/N \n")
price = 0

if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
        price +=  1

elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1

else:
    price = 25
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
        price += 1

print(f"your final price is {price}")
