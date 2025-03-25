#NAME: Kyrin Ellis
#DATE: 02/13/2024
#FILE: shipkellis.py
#PURPOSE: Programs that reads if else statments
#Input
package1_weight = float(input("Enter the weight of package 1: "))
package2_weight = float(input("Enter the weight of package 2: "))
package3_weight = float(input("Enter the weight of package 3: "))
#Constants
discount_limit = 100
small_discount = 0.05
big_discount = 0.025
shipping_cost = 15.00
#Total weight
total_weight = package1_weight + package2_weight + package3_weight
#calc and IF Else statement
if total_weight < discount_limit:
    discount_percent = small_discount
else:
        discount_percent = big_discount
discount_amount = shipping_cost * discount_percent
total_shipping_cost = shipping_cost - discount_amount
#output
print("=========SHIPPING COST==========")

print("PACKAGE WEIGHT: {:.2f}".format(total_weight))
print("STANDARD Shipping Cost: ${:.2f}".format(shipping_cost))
print("DISCOUNT: {:.1%}".format(discount_percent))
print("DISCOUNT AMOUNT: ${:.2f}".format(discount_amount))
print("SHIPPING COST: ${:.2f}".format(total_shipping_cost))
