# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
hot_dog = float(input("Enter number of hot dogs:"))
h = hot_dog*3.5

chili_dog = float(input("Enter number of Chili dogs: "))
c = chili_dog*4.5

cheese = float(input("Enter number of cheese toppings: "))
ch = cheese*.5

peppers = float(input("Enter number of pepper toppings: "))
p = peppers*.75

grilled_onions = float(input("Enter number of grilled onion toppings: "))
o = grilled_onions*1

t = h+c+ch+p+o
print('Your total is $,',t + t*.07)
