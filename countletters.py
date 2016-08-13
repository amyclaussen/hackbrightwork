lettercount_dict = {}

def count_letters():
	myname = raw_input("What is your name?").lower()
	for i in myname:
		lettercount_dict[i] = myname.count(i)
	print lettercount_dict
	

count_letters()