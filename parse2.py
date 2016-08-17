# my_name = "Noelis"

# my_name_list = list(my_name)

# print my_name_list

# string_o_numbers = "1,2,3,4,5"

# list_o_numbers = string_o_numbers.split(",")

# print list_o_numbers

# dr_seuss = "One fish two fish red fish blue fish".replace(' fish', '').split(" ")

# print dr_seuss

# def calc_bill():
	# receipt = "item:apples,quantity:4,price:1.50\n"
	# receipt_split = receipt.split(",")
	# print int(receipt_split[1])

	# price = "item:apples,quantity:4,price:1.50\n".split(',')[-1].split(":")[-1]
	# quantity = "item:apples,quantity:4,price:1.50\n".split(',')[-2].split(":")[-1]

	# total = float(price) * float(quantity)

	# print total

# calc_bill()

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]
sub_total = 0

for i in items:
	items_categories = i.split(",")
	qty_category = items_categories[1].strip().split(":")
	price_category = items_categories[2].strip().split(":")

	sub_total += float(price_category[1]) * int(qty_category[1])

print sub_total



	# for i in items_categories[1:3]:
	# 	items_items = i.split(":")
	# 	total_list.append(float(items_items[-1].strip()))

# print total_list
