def checkprime(num):
	for i in range(2,num):
		if num % i == 0:
			print num, "is not prime."
			break
	else:
		print num, "is prime."

def main():
	checkprime_num = 0
	while True:
		checkprime_num = raw_input("Which number would you like to check if it is prime? Type q to quit. ")
		if checkprime_num == "q":
			break
		else:
			try:
				checkprime(int(checkprime_num))
			except:
				print "Please enter a valid integer."

if __name__ == '__main__':
	main()