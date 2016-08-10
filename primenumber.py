def checkprime(num):
	for i in range(2,num):
		if num % i == 0:
			print num, "is not prime."
			break
	else:
		print num, "is prime."

def main():
	checkprime_num = int(raw_input("Which number would you like to check if it is prime? "))
	checkprime(checkprime_num)

if __name__ == '__main__':
	main()