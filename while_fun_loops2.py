def sum_nums(num):
	sum_of_all = 0
	for i in range(num):
		sum_of_all = sum_of_all + i
		i += 1
	return sum_of_all

def sum_nums2(num):
	sum_of_all = 0
	if num < 0:
		for i in range(0,num,-1):
			sum_of_all = sum_of_all + i
			i -= 1
	else:
		for i in range(num):
			sum_of_all = sum_of_all + i
			i += 1
	return sum_of_all

def main():
	input_number = int(raw_input("Number to run sum_num: "))
	print sum_nums2(input_number)

if __name__ == "__main__":
	main()