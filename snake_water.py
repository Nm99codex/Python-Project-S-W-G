import random

# ***GAME FUCTION**
def swg_game(comp_turn, p, n, round_num, comp_win, player_win):
	while(round_num<=n):
		p= input("Player's Turn: ")
		
		if(p!='s' and p!='w' and p!='g'):
			print("Invalid entry")
			continue

		print(f"--Round {round_num}")

		if (comp_turn == p):
			print(f"Match tie in Round - {round_num}")
		
		elif(comp_turn == 's'):
			if(p == 'w'):
				print(f"Computer win in Round - {round_num}")
				comp_win+=1
			elif(p == 'g'):
				print(f"Player win in Round - {round_num}")
				player_win+=1

		elif(comp_turn == 'w'):
			if(p == 'g'):
				print(f"Computer win in Round - {round_num}")
				comp_win+=1
			elif(p == 's'):
				print(f"Player win in Round - {round_num}")
				player_win+=1

		elif(comp_turn == 'g'):
			if(p == 's'):
				print(f"Computer win in Round - {round_num}")
				comp_win+=1
			elif(p == 'w'):
				print(f"Player win in Round - {round_num}")
				player_win+=1

		round_num+=1

	print("FINAL RESULT : ") 

	points = player_win-comp_win

	if(comp_win<player_win):
		print(f"**CONGRATULATIONS !!! YOU WIN by {points} point(s)**")
	
	elif(comp_win>player_win):
		print(f"~~YOU LOSE by {0 - points} point(s)~~")
	
	else:
		print("--MATCH TIE--")

	# Making a high score file
	with open ("hi_score.txt", "r") as f:  #reading hiscore from file
		h = int(f.read())   # h -> high score 

	with open ("hi_score.txt", "w") as f:
		if(points>h):
			print("You scored new HI SCORE")
			f.write(str(points))

# **************************************************
# MAIN FUNCTION
# **************************************************

print("SNAKE - WATER - GUN")
n = int(input("Enter number of rounds : "))  #Number of rounds

randNo = random.randint(1,3)   #Choose any number from 1 to 3
if(randNo==1):
	comp_turn = 's'
if(randNo==2):
	comp_turn = 'w'
if(randNo==3):
	comp_turn = 'g'

p =None

# 
rn = 1;   #Round number
cw = 0;   #Count of computer wins
pw = 0;   #Count of player wins

a = swg_game(comp_turn,p,n,rn,cw,pw)   #Calling function swg_gun