actual_cost=float(input("Please enter the product cost price"))
selling_price=float(input("Please enter the product sale price"))
if selling_price>actual_cost:
  amount=selling_price-actual_cost
  print("you made profit",amount)
else:
  print("you made no profit")