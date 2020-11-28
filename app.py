tasks = []

print("hello\n Wellcome on TodoApp !")

option_input = ''
while option_input != 'q':
	print("(q=quit , l=list, n=new, c=complete, r=reset)\n")
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
		to_delete = input('which task do you want to delete ? ')

		if to_delete in tasks:
			tasks.remove(to_delete)
		else:
			print("task unknown, back to main menu.")

	elif option_input=='r':
		pass

	else:
		pass
