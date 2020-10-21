import os
import main
import commands
import pickle

userInfo = {
	"usrName" = "you have not set a name yet"
}

speak("What should i call you \n")
usrName = takeCommand()

with open('info.pkl', 'wb') as a:
    pickle.dump(usrName, a)

print('saved data')


if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	main.wishMe() 
	main.usrname() 

	commands.cmds()
