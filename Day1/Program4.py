cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
profit = selling_price - cost_price
print("Profit:",profit)
new_selling_price = 1.05 * profit + cost_price
print("Increased selling price after increase profit by 5% : ",new_selling_price)
