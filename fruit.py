# fruits = ["apples", "oranges", "bananas"]

# for i in fruits 
# 	print i

# for i in range(len(fruits)):
# 	print fruits[i]



#     #################################
# count = 0

# while count<len(fruits):
# 	print fruits[count] 
# 	count += 1


# 	###############################



def sum_nums(num):
	sum_of_all = 0
	for i in range(num):
		sum_of_all += i
	return sum_of_all	

	#sum(ourlist[i])

print sum_nums(12)