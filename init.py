import main
import os

if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	main.wishMe() 
	main.usrname() 

	main.commands.cmds()