# full_name = ("Alli","McKee")
# full_name_list = [full_name[0], full_name[1]]
# print full_name_list
# full_name_list = [full_name[1],full_name[0]]
# print full_name_list

# for num in range(1000,99,-100):
# 	print num

names = ['Steven', 'Michael', 'James']
first_middle_combos = []

for firstname in range(len(names)):
	for middlename in range(len(names)):
		combo_name = names[firstname] + " " + names[middlename]
		if names[firstname] == names[middlename]:
			pass
		elif combo_name in first_middle_combos:
			pass
			#combo in combo list, pass
		else:
			first_middle_combos.append(combo_name)
			#add that ish to the list
print first_middle_combos