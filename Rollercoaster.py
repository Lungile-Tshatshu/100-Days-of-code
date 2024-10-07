Height = int(input("Enter height in cm: \n"))
price = 0
if Height > 120:
    print("you can ride")
    age = int(input("Please enter your age \n"))
    if age < 12:
        price = 10
        print("you will be charged as a minor")
    elif age <= 18:
        price = 20
        print("you will be charged as a Teen")
    else:
        price = 30
        print("you will be charged as an adult")

    Wants_a_picture = input("Would you like a picture? (y/n): ")
    if Wants_a_picture == "Y":
        price += 3

    print(f"your price is {price}")

else:
    print("your height must be greater than 120 to ride")