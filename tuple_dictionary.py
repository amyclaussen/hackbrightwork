food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)

food_dictionary = {}

def convert_tuple_to_dictionary():
	for i in range(0,len(food_price_tuple),2):
		food_dictionary[food_price_tuple[i]] = food_price_tuple[i + 1] 
	print food_dictionary


convert_tuple_to_dictionary()

#for thing in food_price_tuple:
		# food_dictionary["thing index o"] = thing index 0 +1
		#add 2 to the index (really 1 because the range thing alread adds) so that we skip putting the price as the key
		#jeremy says range - which gives indices


		# for thing in ram