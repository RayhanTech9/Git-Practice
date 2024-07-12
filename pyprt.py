# name = input("Enter your Name : ")
# unit = int(input("Enter Unit"));

# if unit <= 100:
#     bill = unit * 1.75
# elif unit <= 300:
#     bill = unit * 1.75 + (unit-100)*2.25
# else:
#     bill = unit * 1.75+200*2.25+(unit-300)*3.50

# if bill <=100:
#     bill = 100;


# elif bill > 1000:
#     surcharges = bill*0.15
# else:
#     surcharges = 0;

# netBill = bill + surcharges;
# print("Output is -----------------------------")
# print("Bill =",bill)
# print("SurCharges =",surcharges)
# print("Net Bill =",netBill)

# pattern = int(input("Enter your Number : "))

# n = 1
# for i in range(0,pattern):
#     for j in range(0, i+1):
#         print(n,end=" ")
#         n = n+1
#     print()

# rows = int(input("Enter your rows Number : "))
# b = 0
# reverse for loop from 5 to 0
# for i in range(rows, 0, -1):
#     b = b+1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r')




rows = int(input("Enter your Rows Number : "))

for y in range(0,4+1):
    for z in range(1,y+1):
        print(z,end=" ")
    print()


for i in range(rows,9, -1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()




