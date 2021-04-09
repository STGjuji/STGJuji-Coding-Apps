
Answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

	answer = input("You reach a crossroad, would you like to go left or right?").lower().strip()
	if answer == "left":
		answer = input("You encounter a monster, would u like to run or attack.")

		if answer == "attack":
			print("That was not the greatest idea, you lost!")
		else:
			print("Good choice, you made it away safly.")





	elif answer == "right":
		print("You ran into a bear trap, and bled out.")






	else:
	 print("Invalid choice, you lost!")


else:
	print("That's to bad!")