'''
Below is a list of menu items and prices. Write a function that takes this list and returns a dictionary with the name of the food as the key and the price as the value. Make sure the price is a float, not a string!
 
menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50",
       "food:fries,price:4.00","food:shake, price:5.00"]
'''

menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50","food:fries,price:4.00","food:shake, price:5.00"]

food_list = {}

def food_dict():
	for i in menu_list:
		categories = i.split(",")
		food = categories[0].strip().split(":")
		price = categories[1].strip().split(":")
		food_list[food[1]]= float(price[1])
	print food_list


food_dict()
