def convert_score_to_letter(score):
	if score >= 90:
		return "A"
	elif 80 <= score < 90:
		return "B"
	elif 70 <= score < 80:
		return "C"
	elif 60 <= score < 70:
		return "B"
	else:
		return "F"

def process_file_to_list():
	with open ("class_grades.txt") as grade_file:
		grade_list = grade_file.readlines()
		grade_list_ints = []
		for i in range(1,len(grade_list)):
			grade_list_ints.append(int(grade_list[i].strip()))
		return grade_list_ints

def main():
	grade_list = process_file_to_list()
	for grade in grade_list:
		letter_grade = convert_score_to_letter(grade)
		print str(grade) + " is a " + str(letter_grade)

if __name__ == '__main__':
   main()