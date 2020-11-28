tasks = []

print("hello\n Wellcome on TodoApp !")

option_input = ''
while option_input != 'q':
	print("(q=quit , l=list, n=new, c=complete=, r=reset)\n")
	option_input = input('what do you want to do ? ').lower()

	if option_input=='q':
		print("thanks, bye")
	
	elif option_input=='l':
		print('Your open tasks are : ')
		for task in tasks :
			print('- ' + task)

	elif option_input=='n':
		tasks.append(input('write your new task : '))

	elif option_input=='c':
		pass

	elif option_input=='r':
		pass

	else:
		pass
