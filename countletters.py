lettercount_dict = {}

def count_letters():
	myname = raw_input("What is your name?").lower()
	for i in myname:

		#lettershowsup = count how many times i appears

		lettercount_dict[i] = "dunnoyet" #change this to lettershowsup
	print lettercount_dict
	

count_letters()