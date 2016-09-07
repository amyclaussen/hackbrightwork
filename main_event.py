from string import *

def make_key_map():
	key_map = {}
	alpha_list = list(ascii_lowercase)
	for letter in range(len(alpha_list)):
		key_map[alpha_list[letter]] = "test"
	print key_map	


def encrypt():
	pass

def decrypt():
	pass

def alli_snark():
	print "Tales from the crypt."

def main():
	make_key_map()

if __name__ == '__main__':
	main()