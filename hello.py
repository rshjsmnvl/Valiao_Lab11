first = float (input("first item ="))
second = float (input("second item ="))
third = float (input("third item ="))
total = first+second+third
print(total)
if total > 100:
    discount = total * 0.10
    new_total = total - discount
    print("You are qualified for a discount")
    print("New total", (new_total))
else:
    print("Payment failed!")
loyalty_points = total//10
print("Loyalty Points Earned:", loyalty_points)
payment = float (input("Enter payment ="))
if payment > total:
    change = total - payment
    print("Your change is", change)
else:
    print("Payment failed!")