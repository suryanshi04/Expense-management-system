from tkinter import *
from tkinter import ttk
import sqlite3  as db #for connectivity of database
from tkcalendar import DateEntry
import os
def init(): #fun for storing data
    connectionObjn = db.connect("expenseTracker.db") #connection of database
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists expenses (
        date string,
        name string,
        title string,
        expense number
        )
    '''
    curr.execute(query)
    connectionObjn.commit()
def submitexpense(): #submit button
    values=[dateEntry.get(),Name.get(),Title.get(),Expense.get()] #values in dictionary on click
    print(values)
    Etable.insert('','end',values=values)
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?)
    '''
    curr.execute(query,(dateEntry.get(),Name.get(),Title.get(),Expense.get()))
    connectionObjn.commit()
def viewexpense():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
     select * from expenses
    '''
    total='''
    select sum(expense) from expenses
    '''
    curr.execute(query)
    rows=curr.fetchall()
    curr.execute(total)
    amount=curr.fetchall()[0]
    print(rows)
    print(amount)
    
    l=Label(root,text="Date\t  Name\t  Title\t  Expense",font=('arial',15,'bold'),bg="dark cyan",fg="light cyan")
    l.grid(row=6,column=0,padx=7,pady=7)
    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t'
        st+='\n'
    print(st)
    l=Label(root,text=st,font=('arial',12))
    l.grid(row=7,column=0,padx=7,pady=7)
###################################################################################################################################
# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 ################################################
   
# Create an object of tkinter ImageTk
    Label(register_screen, text="Please enter details below", bg="light blue").pack()
    Label(register_screen).pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="light cyan", command = register_user).pack()

# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login",bg="light cyan").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify,bg="light green").pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x350")
    main_screen.title("Account Login")
    main_screen['background']='light cyan'
    Label(text="GET STARTED!", bg="light blue", width="300", height="2", font=("Times new roman", 15)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",bg="light green",command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30",bg="light green",command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
####################################################################################################################################
init()
root=Tk()
root.title("Expense management system")
root.geometry('800x600')
root['background']='light cyan'
#date
dateLabel=Label(root,text="Date",font=('arial',15,'bold'),bg="dark cyan",fg="light cyan",width=12)
dateLabel.grid(row=0,column=0,padx=7,pady=7)
dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'))
dateEntry.grid(row=0,column=1,padx=7,pady=7)
#name
Name=StringVar()
nameLabel=Label(root, text="Name",font=('arial',15,'bold'),bg="dark cyan",fg="light cyan",width=12)
nameLabel.grid(row=1,column=0,padx=7,pady=7)
NameEntry=Entry(root,textvariable=Name,font=('arial',15,'bold'))
NameEntry.grid(row=1,column=1,padx=7,pady=7)
#title
Title=StringVar()
titleLabel=Label(root, text="Title",font=('arial',15,'bold'),bg="dark cyan",fg="light cyan",width=12)
titleLabel.grid(row=2,column=0,padx=7,pady=7)
titleEntry=Entry(root,textvariable=Title,font=('arial',15,'bold'))
titleEntry.grid(row=2,column=1,padx=7,pady=7)
#expense
Expense=IntVar()
expenseLabel=Label(root,text="Expense",font=('arial',15,'bold'),bg="dark cyan",fg="light cyan",width=12)
expenseLabel.grid(row=3,column=0,padx=7,pady=7)
expenseEntry=Entry(root,textvariable=Expense,font=('arial',15,'bold'))
expenseEntry.grid(row=3,column=1,padx=7,pady=7)
#submit button
submitbtn=Button(root,command=submitexpense,text="Submit",font=('arial',15,'bold'),bg="dark green",fg="light green",width=12 )
submitbtn.grid(row=4,column=0,padx=13,pady=13)
viewtn=Button(root,command=viewexpense,text="View expenses",font=('arial',15,'bold'),bg="dark green",fg="light green",width=12 )
viewtn.grid(row=4,column=1,padx=13,pady=13)
# all saved expenses--------------
Elist=['Date','Name','Title','Expense']
Etable=ttk.Treeview(root,column=Elist,show='headings',height=7)
for c in Elist:
    Etable.heading(c,text=c.title())
Etable.grid(row=5,column=0,padx=7,pady=7,columnspan=3)
mainloop()