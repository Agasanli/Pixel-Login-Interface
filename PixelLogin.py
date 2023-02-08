import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

windows = tk.Tk()
windows.geometry("350x400")
windows.title("Login")
windows.resizable(False,False)

photo = PhotoImage(file ="C:\\Users\\xxx\\xxxx\\backgr.gif") #LOCATIONU DEYISMEK LAZIMDIR
eticket = Label(windows, image=photo,bd=0)
eticket.place(x=0,y=0)
#ad def
def username_text(e):
   username.delete(0,"end")
   
#sifre def
def password_text(e):
   password.delete(0,"end")

#giris buton
def nothing():
   my_label.config(bg="Red",fg="White",text="Error",font="Monospace 15 bold")


   # my_label.config("Giris edildi")

#giris butonu
# login2 = tk.Button(text="Login",font="Arial 12 bold",bg="#00E5EE").pack(padx=80,pady=170)
login = PhotoImage(file="C:\\Users\\XXX\\XXX\\click.png") #LOCATIONU DEYISMEK LAZIMDIR
img_label = Label(image=login)

my_button = Button(windows,image=login,command=nothing)
my_button.pack(pady=150)

my_label = Label(windows,font="Arial 14 bold",text="")
my_label.place(x=155,y=270)

#istifadeci adi
username = tk.Entry(windows,bg="white",fg="#808080",width=20,bd=7,cursor="hand2",font="Arial 12 ")
username.insert(0,"Username")
username.place(x=90,y=50)
username.bind("<FocusIn>", username_text)

#sifre melumat
password = tk.Entry(windows,bg="white",fg="#808080",width=20,bd=7,cursor="hand2",font="Arial 12 ")
password.insert(0,"Password")
password.place(x=90,y=90)
password.bind("<FocusIn>", password_text)

windows.mainloop()