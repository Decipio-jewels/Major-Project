from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage


def register():
    try:
        username_value = Username.get()
        password_value = Password.get()
        age_value = int(Age.get())
        phone_value = int(Phone.get())
        dict['username'] = username_value
        dict['password'] = password_value
        dict['phone'] = phone_value
        dict['age'] = age_value
        f = open("dict.txt","w")
        for key, value in dict.items():
            f.write('%s:%s\n' % (key, value))
        f.close()
        messagebox.showinfo("Information", "Registration Completed")
    except ValueError:
        pass
    

def ExitFile():
    popup.destroy()
    
def NewFile():
    print ("New File!")

def About():
    print ("New File!")

def Profile():
    
    prowindow = Toplevel()
    prowindow.minsize(300,400)
    
    mainframe = ttk.Frame(prowindow, padding="3 30 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    prowindow.columnconfigure(0, weight=1)
    prowindow.rowconfigure(0, weight=1)
    
    prowindow.title('Profile')
    ttk.Label(prowindow, text='Welcome '+L_username.get(), font="none 20 bold").place(x=80, y = 10)
    ttk.Label(prowindow, text="Username").place(x=20, y=150)
    ttk.Label(prowindow, text=L_username.get()).place(x=100, y=150)
    ttk.Label(prowindow, text="Age").place(x=20, y=180)
    ttk.Label(prowindow, text=dict['age'] ).place(x=100, y=180)
    ttk.Label(prowindow, text="Phone").place(x=20, y=210)
    ttk.Label(prowindow, text=dict['phone'] ).place(x=100, y=210)
    
    mainloop()

def signin():
     try:
         file = open("dict.txt","r")
         for line in file:
             if ':' in line:
                 key,value = line.split(':', 1)
                 cvalue = len(value)-1
                 value = value[0:cvalue]
                 dict[key]=value
             else:
                 pass
         usern = dict.get('username')
         passn = dict.get('password')
         
         if(usern==L_username.get() and passn==L_password.get()):
             Profile()
         else:
             messagebox.showinfo("ERROR", "Incorrect Username or Password")
     except ValueError:
           pass
     file.close()
    
def OpenFile():
    mywin.filename =  filedialog.askopenfilename(initialdir = "/",
        title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)
    
def registerscreen():
    regwindow = Toplevel()
    regwindow.minsize(300,400)
    
    regwindow.title('Register Menu')

    mainframe = ttk.Frame(regwindow, padding="3 30 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    regwindow.columnconfigure(0, weight=1)
    regwindow.rowconfigure(0, weight=1)
    
    img = PhotoImage(file="register.png")
    ttk.Label(mainframe,image=img).place(x=100, y = 0)
    
    ttk.Label(mainframe, text="REGISTRATION").place(x=100, y = 110)
    
    ttk.Label(mainframe, text="Username").place(x=20, y=150)
    username_entry = ttk.Entry(mainframe, width=10, textvariable=Username)
    username_entry.place(x=100, y=150)
    
    ttk.Label(mainframe, text="Password").place(x=20, y=180)
    password_entry = ttk.Entry(mainframe, width=10, show="*", textvariable=Password)
    password_entry.place(x=100, y=180)

    ttk.Label(mainframe, text="Age").place(x=20, y=210)
    age_entry = ttk.Entry(mainframe, width=10, textvariable=Age)
    age_entry.place(x=100, y=210)

    ttk.Label(mainframe, text="Phone").place(x=20, y=240)
    phone_entry = ttk.Entry(mainframe, width=10, textvariable=Phone)
    phone_entry.place(x=100, y=240)

    ttk.Button(mainframe, text="Register", command=register).place(x=100, y=280)
   
    username_entry.focus()
    password_entry.focus()
    age_entry.focus()
    phone_entry.focus()
    
    mainloop()
    
    
def loginscreen():
    loginwindow = Toplevel()
    loginwindow.minsize(300,500)
    
    loginwindow.title('Login Menu')

    mainframe = ttk.Frame(loginwindow, padding="3 30 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    loginwindow.columnconfigure(0, weight=1)
    loginwindow.rowconfigure(0, weight=1)
    
    img = PhotoImage(file="Login.png")
    ttk.Label(mainframe,image=img).place(x=70, y = 0)
    
    ttk.Label(mainframe, text="LOGIN SCREEN").place(x=100, y = 200)

    
    ttk.Label(mainframe, text="Username").place(x=20, y=240)
    username_entry = ttk.Entry(mainframe, width=7, textvariable=L_username)
    username_entry.place(x=100, y=240)
    
    ttk.Label(mainframe, text="Password").place(x=20, y=280)
    password_entry = ttk.Entry(mainframe, width=7, show="*",textvariable=L_password)
    password_entry.place(x=100, y=280)

    ttk.Button(mainframe, text="Login", command=signin).place(x=100, y=350)
   
    username_entry.focus()
    password_entry.focus()

    mainloop()

    
    
   
    
    

mywin = Tk()
mywin.minsize(300,400)
mywin.resizable(False,False)
mywin.title('Delivery System')

Username = StringVar()
Password = StringVar()
Age = StringVar()
Phone = StringVar()
L_username = StringVar()
L_password = StringVar()
username_entry=StringVar()
password_entry=StringVar()


dict = { }

menu = Menu(mywin)
mywin.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Login", command=loginscreen)
filemenu.add_command(label="Register", command=registerscreen)
filemenu.add_command(label="Register", command=registerscreen)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=mywin.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

lblimage = PhotoImage(file="car.png")
Label(mywin, text="Welcome to Nats Systems", fg="black",
      font="none 20 bold"). grid(row=1, column =0, sticky=N)
Label(mywin, image=lblimage).grid(row=4, column = 0, padx=100, pady=20)

Button(mywin, text="Let's Begin ! ", width=10, command=loginscreen).grid(row=7,
        column=0, columnspan=2, padx=15, pady=15)


mainloop()
