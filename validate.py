# mega challenges: 
# write program that validates that a user has input a valid email address, 
# and doesn't let a person continue until a valid email address is 
# entered
# for example :" melissa@hackbrightacademy.com" is valid 
# and "melissa@hackbrightacademy" or" @hackbrightacademy.com" is not valid.

import re

validation = None
email = None

def validate(email):
	email_split = email.split("@")
	username = email_split[0]
	email_domain_suffix = email_split[1].split(".")
	domain = email_domain_suffix[0]
	suffix = email_domain_suffix[1]

	if username == "":
		print "Not a valid email."
		return False
	elif len(email_split) != 2:
		print "Not a valid email."
		return False
	# elif not re.match(r"[A-Za-z0-9.+_-@]", email):
	# 	return False
	elif suffix.lower() not in ["edu", "com", "net", "org", "gov", "mil", "int"]:
		print "Not a valid email."
		return False
	else:
		validation = True
		return validation

def main():
	while validation != True:
		email = raw_input("Please enter your email: ")
		print email, "is valid"

if __name__ == '__main__':
	main()