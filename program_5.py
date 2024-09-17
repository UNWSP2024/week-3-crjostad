# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
hot_dog = 3.5

chili_dog = 4.5

cheese = .5

peppers = .75

grilled_onions = 1

Subtotal = float(input("Enter Hot dog choice: "))

print("Your total comes to $", Subtotal + Subtotal*.07)
