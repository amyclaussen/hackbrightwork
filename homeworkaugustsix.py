
# Write a program that will ask the user for a message and the number of times
#  they want that message displayed. Then output the message that number of times.

def write_message():
    message = raw_input("Write any message: ")
    num_repeat = int(raw_input("How many times would you like to repeat message: "))
    for i in range(num_repeat):
        print message,

# Write a Python program to find those numbers which are divisible by 7 and 
# multiple of 5, between 1500 and 2700 (both included).

def divisible():
    for i in range(1500,2701,5):
        if i % (5 * 7) == 0:
            print i

# Given: Two positive integers a and b (a<b<15000). [you could probably change 
# the number here]
# Return: The sum of all odd integers from a through b, inclusively.
# [python skills: Loops, operators & conditionals]


def sum_of_int():
    summation = 0
    index = 0
    a = raw_input("What do you want the starting number to be? (Must be positive integer and less than 15,000.) ")
    if a.isdigit() and 0 < a < 15000:
        b = raw_input("What do you want the ending number to be? (Must be more that the starting number and less than or equal to 15,000.) ")
        if b.isdigit() and a < b < 15001:
                for i in range(a,b + 1):
                    if i % 2 == 1:
                        summation += i
                    index += 1
    else:
        print "Please reenter a valid number."
    return summation

#entering anything other than an int breaks it

# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with 
# space in between), inclusively.

# g9aB0iza5rvlugFxAQnzxYjzjUVzRjajEJ7P25FcwWHt4VYbOoSgGo5I8H94zOsBP0tAkq3dBurhinusxonARhdcy44zOjdOMyJdz8rqtOmZeimLY9rHkEvdauricalYh6x65Jy3ZFTS3F303GdMZr7YVgwN9o4Ouo.
# 72 79 119 125

# Solution should return: 
# Burhinus daurica

def slice_indices(starting_string,num_a,num_b,num_c,num_d):
        slice_a = starting_string[num_a:num_b+1]
        slice_b = starting_string[num_c:num_d+1]
        return slice_a + " " + slice_b

# mega challenges: 
# write program that validates that a user has input a valid email address, 
# and doesn't let a person continue until a valid email address is 
# entered
# for example :" melissa@hackbrightacademy.com" is valid 
# and "melissa@hackbrightacademy" or" @hackbrightacademy.com" is not valid.

def validate_email():
    pass

def menu():
    while True:
        print ""
        print "Select a Menu Option:"
        print "     1 - Write Message Program"
        print "     2 - Divisible Program"
        print "     3 - Sum of Odd Integers Program"
        print "     4 - Slice Indices Program"     
        print "     5 - Quit"
        choice = raw_input("-->  ")
        if choice not in ["1","2","3","4","5"]:
            print "'" + str(choice) + "' was not a menu item."
        else:
            return int(choice)

def main():
    choice = None
    while choice != 5:
        choice = menu()
        if choice == 1:
            write_message()
        elif choice == 2:
            divisible()
        elif choice == 3:
            print sum_of_int()
        elif choice == 4:
            print slice_indices("g9aB0iza5rvlugFxAQnzxYjzjUVzRjajEJ7P25FcwWHt4VYbOoSgGo5I8H94zOsBP0tAkq3dBurhinusxonARhdcy44zOjdOMyJdz8rqtOmZeimLY9rHkEvdauricalYh6x65Jy3ZFTS3F303GdMZr7YVgwN9o4Ouo",72,79,119,125)
        else:
            print "Goodbye."

if __name__ == '__main__':
    main()