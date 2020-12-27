from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkcalendar import Calendar
import os
import sqlite3
import re

###################DATABASE Functions

def create_signUP_table():
    con = sqlite3.connect("guidatabase.db")

    cur = con.cursor()
    cur.execute("""
    CREATE TABLE SignUpData(
        user_name text,
        user_id text,
        user_password text
    )""")
    con.commit()
    con.close()


def create_FormInfo_table():
    con = sqlite3.connect("guidatabase.db")

    cur = con.cursor()
    cur.execute("""
    CREATE TABLE FormInfo(
        user_name text,
        user_Gender text,
        user_age integer,
        user_dob text,
        user_contact integer,
        user_email text,
        user_course text
    )""")
    con.commit()
    con.close()


def Sign_Up_data(en1,en2,en3):
    con = sqlite3.connect("guidatabase.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO SignUpData VALUES (?,?,?)",(en1,en2,en3))
        #allready Created Table, data Added
    except sqlite3.OperationalError:
        #Not created!! Now Creating
        create_signUP_table()
        cur.execute("INSERT INTO SignUpData VALUES (?,?,?)",(en1,en2,en3))
    con.commit()
    con.close()


def Form_data(en1,en2,en3,en4,en5,en6,en7):
    con = sqlite3.connect("guidatabase.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO FormInfo VALUES (?,?,?,?,?,?,?)",(en1,en2,en3,en4,en5,en6,en7))
        #allready Created Table, data Added
    except sqlite3.OperationalError:
        #Not created!! Now Creating
        create_FormInfo_table()
        cur.execute("INSERT INTO FormInfo VALUES (?,?,?,?,?,?,?)",(en1,en2,en3,en4,en5,en6,en7))
    con.commit()
    con.close()

def get_pass(userid):
    con = sqlite3.connect("guidatabase.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM SignUpData WHERE user_id=?",(userid,))

    return cur.fetchone()[2]


#######################################################

    

####GUI
root=Tk()
root.geometry('1200x1000')
root.resizable(0,0)


# _ Main window ____________________________________________________ 
def Home():
    #creating Frame For Image
    f1 = Frame(root,width=1200,height=800,bg='yellow')
    root.title("Welcome Window")
    f1.place(x=0,y=0)
    # image Labeling
    l1=Label(f1,width=1200,height=800,bg='black')
    l1.place(x=0,y=0)

    #creating labels for entries
    #lable for intro lines
    lblIntro = Label(f1, text='Welcome to Login Page',width=40,height=2,bg="#ffd60c",font='arial 18 bold')
    lblIntro.place(x=350,y=40)
    
    # ____LABELS________________________

    #label for username
    lblUser = Label(f1, text='Username',width=10,bg="#ffea80",font='arial 18 bold')
    lblUser.place(x=350,y=150)

    #label for password
    lblPass = Label(f1, text='Password',width=10,bg="#ffea80",font='arial 18 bold')
    lblPass.place(x=350,y=200)

    #____Entries___________________________

    #Entry For user Name
    enUser = Entry(width=20,font='arial 18',bd=3)
    enUser.place(x=560,y=150)
    
    #Entry For password
    enPass = Entry(width=20,font='arial 18',bd=3,show="*")
    enPass.place(x=560,y=200)

    # _____Buttons_________________________________
    #login Button
    loginButton= Button(text="Login",width=10,font="arial 10 bold",command = lambda:login(enUser,enPass))
    loginButton.place(x=500,y=280)

    #SignUp Button
    signupButton= Button(text="Sign Up",width=10,font="arial 10 bold",command=signUpWindow)
    signupButton.place(x=700,y=280)
    
    f1.mainloop()

  
def formFrame():
    ####################################################################ISSUE______________________
    varGen = StringVar()

    # ______FRAME___________
    f2=Frame(root,width=1200,height=1200,bg="yellow")
    f2.place(x=0,y=0)
    root.title("Registration")

    
    # ______Putting image on label_______________       
    
    lbImg=Label(f2,width=1200,height=800,bg='black')
    lbImg.place(x=0,y=0)
    #____Welcome Message Label___________
    lbIntr=Label(f2,width=50,text='Welcome to Registration Page',font=('italic',20,'bold'),bg="#66fcf1")
    lbIntr.place(x=200,y=20)

    # ____LABELS________________________
    lbName=Label(f2,width=10,text='Name',font=('italic',20,'bold'),bg="#66fcf1")
    lbName.place(x=250,y=90)

    lbGen=Label(f2,width=10,text='Gender',font=('italic',20,'bold'),bg="#66fcf1")
    lbGen.place(x=250,y=160)
        
    lbAge=Label(f2,width=10,text='Age',font=('italic',20,'bold'),bg="#66fcf1")
    lbAge.place(x=250,y=230)
        
    lbDob=Label(f2,width=11,justify=LEFT,text='Date Of Birth',font=('italic',20,'bold'),bg="#66fcf1")
    lbDob.place(x=250,y=300)

    
    lbCont=Label(f2,width=13,justify=LEFT,text='Contact Number',font=('italic',20,'bold'),bg="#66fcf1")
    lbCont.place(x=250,y=370)
        
    lbEmail=Label(f2,width=10,text='Email',font=('italic',20,'bold'),bg="#66fcf1")
    lbEmail.place(x=250,y=440)
        
    lbCourse=Label(f2,width=10,text='Course',font=('italic',20,'bold'),bg="#66fcf1")
    lbCourse.place(x=250,y=510)

    # ______Entries__________________________________________________________        
    enName=Entry(width=30,font='arial 18',bd=3)
    enName.place(x=500,y=90)
    ##REDIO Buttons
    genRadioMale = Radiobutton(root, text="Male",font=('italic',15), variable = varGen,value='Male')
    genRadioMale.place(x=500,y=160)

    genRadioFemale = Radiobutton(root, text="Female",font=('italic',15), variable = varGen,value='Female')
    genRadioFemale.place(x=620,y=160)

    genRadioOther = Radiobutton(root, text="Others",font=('italic',15),variable = varGen, value='Others')
    genRadioOther.place(x=750,y=160)
    ######################
    
    enAge=Entry(width=30,font='arial 18',bd=3)
    enAge.place(x=500,y=230)
    
    ########################################################
    logoDOB = Button(f2,text="📅",width=3,font=('20,bold'),command= lambda:dob(enDob))
    logoDOB.place(x=500,y=300)
    ########################################################
    
    enDob=Entry(text = "DOB",width=26,font='arial 18',bd=3)
    enDob.place(x=550,y=300)
    
    enCno=Entry(width=30,font='arial 18',bd=3)
    enCno.place(x=500,y=370)
    
    enEmail=Entry(width=30,font='arial 18',bd=3)
    enEmail.place(x=500,y=440)
    
    
    #option menu for COURSES____________
    option = [
            'Select Course',
            'PYTHON',
            'DS',
            'ML',
            'Tkinter'
    ]
    var=StringVar(f2)
    var.set(option[0])
    enCourse=OptionMenu(f2,var,*option)
    enCourse.config(width='20')
    enCourse.place(x=500,y=510)

    
    # __Button______________________________________________________________________________
    #Submit Button
    
    submitButton= Button(text="Submit",width=16,font="arial 13 bold",command = lambda:submitForm(enName,varGen,enAge,enDob,enCno,enEmail,var,enDob))
    submitButton.place(x=300,y=600)

    #Reset Button
    resetButton= Button(text="Reset",width=16,font="arial 13 bold",command=formFrame)
    resetButton.place(x=500,y=600)

    #Back Button
    backButton= Button(text="Logout",width=16,font="arial 13 bold",command=Home)
    backButton.place(x=700,y=600)    
    f2.mainloop()

# ___login function________________________
def login(e1,e2):
        username = e1.get()
        password = e2.get()
        if "" in (username,password):
            tkinter.messagebox.showerror('Error Message','Wrong Id or Password')
        else:
            try:
                dbPass = get_pass(username)

    
                if password == dbPass:
                    tkinter.messagebox.showinfo('Successful','Login Successfully')
                    formFrame()
                else:
                    tkinter.messagebox.showerror('Error Message','Wrong Id or Password')
            except TypeError:
                tkinter.messagebox.showerror('Error Message','Wrong Id or Password')




def signUpWindow():
    f1=Frame(root,width=1200,height=1200,bg="black")
    f1.place(x=0,y=0)
    root.title("SignUp")

    
    # ______Putting image on label_______________       
    
    lbImg=Label(f1,width=1200,height=800,bg='black')
    lbImg.place(x=0,y=0)

    #_____Intro Label____________   
    lbIntro = Label(f1, text='Sign Up',width=50,height=1,bg="#ffea80",font='arial 18 bold')
    lbIntro.place(x=250,y=80)

    # ____Labels_________________________________________
    #Label for Name
    lblName = Label(f1, text='Name',width=10,bg="#ffea80",font='arial 18 bold')
    lblName.place(x=350,y=150)

    #label for username
    lblUser = Label(f1, text='Username',width=10,bg="#ffea80",font='arial 18 bold')
    lblUser.place(x=350,y=200)
    
    #label for password
    lblPass = Label(f1, text='Password',width=10,bg="#ffea80",font='arial 18 bold')
    lblPass.place(x=350,y=250)

    #____Entries___________________________
    #Entry For Name
    enName = Entry(width=20,font='arial 18',bd=3)
    enName.place(x=560,y=150)

    #UserName
    enUname = Entry(width=20,font='arial 18',bd=3)
    enUname.place(x=560,y=200)
    
    #Entry For password
    enPass = Entry(width=20,font='arial 18',bd=3,show="*")
    enPass.place(x=560,y=250)

    # __Button______________________________________________________________________________
    #Submit Button
    signUpButton= Button(text="Sign Up",width=16,font="arial 13 bold",command = lambda: signUp(enName,enUname,enPass))
    signUpButton.place(x=300,y=350)

    #Reset Button
    resetButton= Button(text="Reset",width=16,font="arial 13 bold",command=signUpWindow)
    resetButton.place(x=500,y=350)

    #Back Button
    backButton= Button(text="Back",width=16,font="arial 13 bold",command=Home)
    backButton.place(x=700,y=350)  

    f1.mainloop()
    
def signUp(e1,e2,e3):
   
    # name = e1.get()
    # userName = e2.get()
    # passWord = e3.get()
    name = e1.get()
    userName = e2.get()
    passWord = e3.get()
    if "" in (userName,passWord,name):
        tkinter.messagebox.showerror('Error Message','Something is missing')

    else:
        #############Sending Data to DATABASE##########################
        Sign_Up_data(name,userName,passWord)
        tkinter.messagebox.showinfo('Done','Signed in Successfully. You can Login Now!')
        Home()


def submitForm(e1,e2,e3,e4,e5,e6,e7,lb):	
    name=e1.get()
    gender = e2.get()
    age=e3.get()
    try:
        age = int(age)
    except ValueError:
        tkinter.messagebox.showerror('Error','Age is Invalid')
        return
    dob=e4.get()
    Cno=e5.get()
    Email=e6.get()
    course = e7.get()    
    if re.search('@',Email)==None:
        tkinter.messagebox.showerror('Error','Email is Not Valid')
    else:

        #___Contact Number to int______
        try:
            Cno = int(Cno)
            if len(str(Cno))==10:
                # if name=="" or age=="" or dob=="" or  Cno =="" or Email=="" or course =="Select Course":
                if "" in (name,gender,age,dob,Cno,Email,course) or course =="Select Course":
                    tkinter.messagebox.showerror('Error Message','Something is missing')
                else:
                    #############Sending Data to DATABASE##########################
                    Form_data(name,gender,age,dob,Cno,Email,course)
                    tkinter.messagebox.showinfo('Done','Form Submitted Successfully')
            else:
                tkinter.messagebox.showerror('Error','Contact Number is Invalid')

        except ValueError:
            tkinter.messagebox.showerror('Error','Contact Number is Invalid')
            return
        

    
        
        

##DOB Exp
def dob(e):
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError:
        import Tkinter as tk
        import ttk

    def print_sel():
        text = cal.get_date()
        e.delete(0,END)
        e.insert(0,text)
        top.destroy()
        

    top = tk.Toplevel(root)

    cal = Calendar(top,font="Arial 14", selectmode='day', year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="Ok", command=print_sel).pack()
    


Home()
