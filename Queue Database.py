queue = []
while True:
	begin = input("""
What would you like to do? Enter the number from the corresponding options :
		1. Add Customer
		2. Remove Customer
		3. Show Customer List
		           """)
		
	if begin == "1":
			customer_name = input("\nPlease state the customer's full name. For main menu, enter \"!\":\n")
			if customer_name =="!":
				continue
			customer_number = input("\nPlease enter the customer's contact number. For main menu, enter \"!\": \n")
			if customer_number == "!":
				continue
			queue.append((customer_name, customer_number))
			continue


	if begin == "2":
		while True:
			position = 0
			for x in queue:
				position +=1
				print(str(position) + "." + str(x))	
			try:
				y = int(input("\nPlease select which customer you would like to remove from the list by inputting the corresponding number. (For main menu, enter \"0\":\n"))
				if y == 0:
					break
			except:
				print("\nIncorrect input. Please enter a numeric value\n")
				continue
			if y > position or y < 1:
				print("\nIncorrect input. Please enter a number specified on the list\n")
				continue
			else:
				print("\n" + str(queue[(y-1)]) + " will be removed from the list\n")
				queue.remove(queue[y-1])
				break
		continue

	if begin == "3":
		position = 0
		for x in queue:
			position +=1
			print(str(position) +"." + str(x))
			continue