grade = input('please enter the mark:')
grade = int(grade)
if grade >= 90:
	print('HD')
elif grade <90 and grade >=80:
	print('D')
elif grade <80 and grade >= 75:
	print('C')
elif grade <75 and grade >=50:
	print('Pass')
else:
	print('Fail')