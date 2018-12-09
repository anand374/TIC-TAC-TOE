import numpy as np
import random

#GLOBAL VARIABLE

user = 1
comp = -1

grid = np.array([[0,0,0],[0,0,0],[0,0,0]])
num_grid = np.array([[0,1,2],[3,4,5],[6,7,8]])
pat11 = np.array([[1,1,1],[0,0,0],[0,0,0]])
pat12 = np.array([[0,0,0],[1,1,1],[0,0,0]])
pat13 = np.array([[0,0,0],[0,0,0],[1,1,1]])
pat21 = np.array([[1,0,0],[1,0,0],[1,0,0]])
pat22 = np.array([[0,1,0],[0,1,0],[0,1,0]])
pat23 = np.array([[0,0,1],[0,0,1],[0,0,1]])
pat31 = np.array([[1,0,0],[0,1,0],[0,0,1]])
pat32 = np.array([[0,0,1],[0,1,0],[1,0,0]])


def print_grid():
	for row in grid:
		for col in row:
			if col==0:
				print "   |",
			elif col==1:
				print " X |",
			elif col==-1:
				print " O |",
		print "\n--------------"


def print_num_grid():
	for row in num_grid:
		for col in row:
			print "",col,"|",
		print "\n--------------"


def mult(grid1,grid2):
	ans = 0
	for x in range(3):
		for y in range(3):
			ans += grid1[x][y] * grid2[x][y]

	if abs(ans)==3:
		return True
	else:
		return False


def check_hidden():
	'''
		Steps
			1. Check for won - check which player matches the pattern
			2. If not won and no cells 0, means draw!
	'''

	#Check for won
	if mult(grid,pat11):
		return True
	elif mult(grid,pat12):
		return True
	elif mult(grid,pat13):
		return True
	elif mult(grid,pat21):
		return True
	elif mult(grid,pat22):
		return True
	elif mult(grid,pat23):
		return True
	elif mult(grid,pat31):
		return True
	elif mult(grid,pat32):
		return True

	#check for draw
	for row in grid:
		for col in row:
			if col==0:
				return False

	return True

def check():
	'''
		Steps
			1. Check for won - check which player matches the pattern
			2. If not won and no cells 0, means draw!
	'''

	#Check for won
	if mult(grid,pat11):
		if(grid[0][0]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat12):
		if(grid[1][0]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat13):
		if(grid[2][0]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat21):
		if(grid[0][0]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat22):
		if(grid[0][1]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat23):
		if(grid[0][2]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat31):
		if(grid[0][0]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True
	elif mult(grid,pat32):
		if(grid[2][0]==user):
			print "User has WON! Congo!"
		else:
			print "Computer has won!"
		return True

	#check for draw
	for row in grid:
		for col in row:
			if col==0:
				return False

	print "The game is DRAW!"
	return True


def comp_play():
	'''
		Steps:
			1. Check for empty boxes
			2. For each empty box, trial and error put in comp symbol and check for win
			3. If win then win, else put in some random box and return

	'''
	loc = []
	for x in range(3):
		for y in range(3):
			if grid[x][y]==0:
				loc.append((x,y))

	if loc==[]:
		print "Something is wrong, the game is DRAW it seems!"
		return
	
	for coord in loc:
		grid[coord[0]][coord[1]] = comp
		won = check_hidden()
		if won:
			return
		grid[coord[0]][coord[1]] = 0

	#Program reached here means can't win in this turn!

	#Check if user is going to win in the next turn!
	for coord in loc:
		grid[coord[0]][coord[1]] = user
		won = check_hidden()
		if won:
			grid[coord[0]][coord[1]] = comp
			return
		grid[coord[0]][coord[1]] = 0

	#Randomly play the turn then

	size = len(loc)
	ind = int(random.random()*10) % size
	grid[loc[ind][0]][loc[ind][1]] = comp


def grid_in(num):
	n = int(num)

	i = n/3
	j = n%3
	if grid[i][j]!=0:
		empty = False
		while(not empty):
			print_num_grid()
			var = raw_input("The box is already full. Enter new loc: ")
			n = int(var)
			i = n/3
			j = n%3
			empty = (grid[i][j]==0)
	grid[i][j] = user

def reset():
	global grid
	grid = np.array([[0,0,0],[0,0,0],[0,0,0]])

def main():
	'''
		Steps:
			1. Print grid
			2. Ask human player input
			3. update print grid
			4. computer player plays
			5. update print grid
			6. ask human player input

		Recurse after each player input- 
			Check if that player has won


	'''
	print "Welcome to ~~~~~~~~~~~~~~~~~Abhishek's Artificial Intelligence TIC TAC TOE!~~~~~~~~~~~ \n ~~~~~~~~~~ Hope you like it \n-- Remember, YOU are -X- and Comp is -O- . GOOD LUCK!"
	won = False
	while(not won):
		print "Current GRID: "
		print_grid()
		print " "
		print_num_grid()
		var = raw_input("Your turn to play! Please enter box number: ")
		grid_in(var)
		print "Grid after enter:"
		print_grid()
		print "Checking......"
		won = check()
		if won:
			var = raw_input("Wanna play another game? Enter Y/N")
			if var=="Y" or var=="y":
				reset()
				won = False
				print "Remember, YOU are -X- and Comp is -O- . GOOD LUCK!"
				continue
			else:
				print "Okey Dokey! Better Luck next Time you Amateur Pup! Ciao.. Peace."
				break

		print "Computer's Turn: "
		comp_play()
		won = check()
		if won:
			print "Winning GRID: "
			print_grid()
			var = raw_input("Wanna play another game? Enter Y/N")
			if var=="Y" or var=="y":
				reset()
				won = False
				continue
			else:
				print "Okey Dokey! Better Luck next Time you Amateur Pup! Ciao.. Peace."
				break


if __name__ == '__main__':
    main()