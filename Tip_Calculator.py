
print("welcome to the tip calculator")
totalBill = float(input("Enter the total bill amount R\n"))
tip = int(input("Enter the tip percentage:  (10%, 12%, 15%)\n"))
Num_people = int(input("Enter the number of people\n"))

total_tip = tip /100
total_Amount_paid = (totalBill * total_tip) + totalBill
Amount_Each = (total_Amount_paid / Num_people)

print(f"The amount that will be paid by each person is R{Amount_Each}")

