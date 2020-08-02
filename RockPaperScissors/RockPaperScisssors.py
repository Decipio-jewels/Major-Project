from tkinter import *
import random
import tkinter.messagebox as tm
import sys

# making the window
root = Tk()

# setting the icon of the window
root.iconbitmap("rock2.ico")
# setting the title of the window
root.title('Rock Paper Scissors')
# making the window fixed (not resizable)
root.resizable(width=False, height=False)

click = True

# all the images

# rock, paper, scissors hands
rHandPhoto = PhotoImage(file='rHand.png')
pHandPhoto = PhotoImage(file='pHand.png')
sHandPhoto = PhotoImage(file='sHand.png')

# rock, paper scissor images
rockPhoto = PhotoImage(file="rock.png")
paperPhoto = PhotoImage(file='paper.png')
scissorsPhoto = PhotoImage(file='scissors.png')

# winning, losing, tie images
winPhoto = PhotoImage(file="win.png")
losePhoto = PhotoImage(file="loose.png")
tiePhoto = PhotoImage(file="tie.png")


# making buttons variable
rHandButton = ''
pHandButton = ''
sHandButton = ''

wins = 0
draws = 0
loses = 0

def play():
	global rHandButton, pHandButton, sHandButton

	rHandButton = Button(root, image=rHandPhoto, command=lambda:youPick('rock'))
	pHandButton = Button(root, image=pHandPhoto, command=lambda:youPick('paper'))
	sHandButton = Button(root, image=sHandPhoto, command=lambda:youPick('scissors'))

	# winText = Text(root, )

	rHandButton.grid(row=0, column=0)
	pHandButton.grid(row=0, column=1)
	sHandButton.grid(row=0, column=2)

def computerPick():
	choice = random.choice(['rock', 'paper', 'scissors'])
	return choice



def youPick(yourChoice):

	global click
	global wins, draws, loses

	compPick = computerPick()

	if click == True:

		if yourChoice == 'rock':
			rHandButton.configure(image=rockPhoto)
			if (compPick == 'rock'):
				pHandButton.configure(image=rockPhoto)
				sHandButton.configure(image=tiePhoto)
				click = False
			elif (compPick == 'paper'):
				pHandButton.configure(image=paperPhoto)
				sHandButton.configure(image=losePhoto)
				click = False
			else:
				pHandButton.configure(image=scissorsPhoto)
				sHandButton.configure(image=winPhoto)
				click = False

		elif yourChoice == 'paper':
			pHandButton.configure(image=paperPhoto)
			if (compPick == 'rock'):
				rHandButton.configure(image=rockPhoto)
				sHandButton.configure(image=winPhoto)
				click = False
			elif (compPick == 'paper'):
				rHandButton.configure(image=paperPhoto)
				sHandButton.configure(image=tiePhoto)
				click = False
			else:
				rHandButton.configure(image=scissorsPhoto)
				sHandButton.configure(image=losePhoto)
				click = False			

		elif yourChoice == 'scissors':
			sHandButton.configure(image=scissorsPhoto)
			if (compPick == 'rock'):
				pHandButton.configure(image=rockPhoto)
				rHandButton.configure(image=losePhoto)
				click = False
			elif (compPick == 'paper'):
				pHandButton.configure(image=rockPhoto)
				rHandButton.configure(image=losePhoto)
				click = False
			else:
				pHandButton.configure(image=rockPhoto)
				rHandButton.configure(image=losePhoto)
				click = False	

	else:

		if yourChoice == 'rock' or yourChoice == 'paper' or yourChoice == 'scissors':
			rHandButton.configure(image=rHandPhoto)
			pHandButton.configure(image=pHandPhoto)
			sHandButton.configure(image=sHandPhoto)
			click = True


loginCounts = 0

def startLogin():

	label_username = Label(root, text="Username")
	label_password = Label(root, text="Password")

	entry_username = Entry(root)
	entry_password = Entry(root, show="*")

	label_username.grid(row=0, sticky=E)
	label_password.grid(row=1, sticky=E)
	entry_username.grid(row=0, column=1)
	entry_password.grid(row=1, column=1)



	logbtn = Button(root, text="Login", command=lambda:_login_btn_clicked(entry_username, entry_password))
	logbtn.grid(columnspan=2)

	# pack()

def _login_btn_clicked(entry_username, entry_password):
	global loginCounts
	username = entry_username.get()
	password = entry_password.get()

	# print(username, password)

	if username == "john" and password == "password":
		tm.showinfo("Login info", "Welcome John")
		# clearing the screen
		for ele in root.winfo_children():
			ele.destroy()
		play()
	else:
		tm.showerror("Login error", "Incorrect username")
		loginCounts += 1
		if (loginCounts >= 3):
			tm.showerror("Login error", "Too many unsuccessful attempts, closing!")
			sys.exit(0)


# play()
startLogin()


root.mainloop()