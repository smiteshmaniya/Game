from tkinter import *
import random

def sel():
   msg.delete(1.0,END)
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   s=var.get()
   r = random.randint(1,3)
   if r==s:
       msg.insert(INSERT,"The is tie.")
   elif (s==1 and r==2):
        msg.insert(INSERT,"Computer choose paper.\nYou loss the game")
   elif s==1 and r==3:
        msg.insert(INSERT,"Computer choose scissors.\nYou win the game")
   elif s==2 and r==1:
        msg.insert(INSERT,"Computer choose stone.\nYou win the game.")
   elif s==2 and r==3:
        msg.insert(INSERT,"Computer choose scissors.\nYou loss the game.")
   elif s==3 and r==1:
        msg.insert(INSERT,"Computer choose stone.\nYou loss the game.")
   elif s==3 and r==2:
        msg.insert(INSERT,"Computer choose paper.\nYou win the game.")
   else:
       print("")

root = Tk()
root.geometry("400x250")
f = Frame(root,bg="yellow")
Label(f,text="The game is star",font=40,bg="yellow", fg="red").pack()
f.pack()
var = IntVar()
R1 = Radiobutton(root, text="Stone", font=16, variable=var, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Paper", font=16, variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Scissors", font=16,variable=var, value=3, command=sel)
R3.pack( anchor = W)

msg = Text(root,width=30,height=2,font= 16)
msg.pack()

label = Label(root)
label.pack()
root.mainloop()
