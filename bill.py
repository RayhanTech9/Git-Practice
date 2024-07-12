# Read the user's name
name = input("Enter your name: ")
# Read the number of units consumed
unit = int(input("Enter unit: "))

# Calculate the bill based on the unit consumption
if unit <= 100:
    bill = unit * 1.75
elif unit <= 300:
    bill = 100 * 1.75 + (unit - 100) * 2.25
else:
    bill = 100 * 1.75 + 200 * 2.25 + (unit - 300) * 3.50

# Ensure minimum charge of Tk. 100
if bill < 100:
    bill = 100

# Calculate additional surcharge if the bill is more than Tk. 1000
if bill > 1000:
    surcharge = bill * 0.15
else:
    surcharge = 0

# Calculate the net bill
netBill = bill + surcharge

# Print the results
print("Name:", name)
print("Bill =", bill)
print("Surcharge =", surcharge)
print("Net Bill =", netBill)































