import random
from hangman_stages import stages
from hangman_words import word_list
import os

print("\n***********************welcome to the game of hangman***********************")
print('''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/             by-payakan''')


random_choose = random.choice(word_list)


display=[]
for n in random_choose:
	display += '_'
print(display)

lives = 6

end_of_game = False
while not end_of_game:
	geuss = input("\n There are a missing above, you have to find the word by letters,\n Enter the latter what ever you geuss :  ")

	for x in range(0,len(random_choose)):
		if geuss == random_choose[x]:
			display[x] = geuss
	print(display)
	
	if '_' not in display:
		end_of_game = True
		print("you win!")
	
	if geuss not in random_choose:
		lives -= 1
		print(stages[lives])
		print("your friend running out of life")
		print(f"only {lives} life you have")
	if lives == 0:
		end_of_game = True
		print("\nYOU LOSE!")
	


