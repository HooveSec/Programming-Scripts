customer_basket_cost = 34
customer_basket_weight = 44

if customer_basket_cost >=100:
  customer_total_basket_cost = customer_basket_cost
  print("Customer total cost: " + str(customer_total_basket_cost))
else:
  customer_total_basket_cost = customer_basket_cost + (customer_basket_weight*1.2)
  print("Customer total cost: " + str(customer_total_basket_cost))
