def fizz_buzz():
	for i in range(1,101):
		if (i % 15 == 0):
			print "FizzBuzz"
		else:
			if i % 3 == 0:
				print "Fizz"
			elif i % 5 == 0:
				print "Buzz"
			else:
				print i


def main():
	fizz_buzz()

if __name__ == '__main__':
    main()