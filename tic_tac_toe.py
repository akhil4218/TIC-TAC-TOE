import tkinter as tk
import sys
from tkinter import messagebox
root=tk.Tk()
root.title("GAME")
num=0
click=True
def checker(buttons):
    global click
    global num
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click=False
        num+=1
        f()

    elif buttons["text"]==" " and click==False:
        buttons["text"]="O"
        click=True
        num+=1
        f()
    
    elif buttons["text"]=="X" or buttons["text"]=="O" and click==True or click==False:
        tk.messagebox.showinfo("SEE","dont press on exist block")
        
    if num==9:
        tk.messagebox.showinfo("Title","!!!!!Draw!!!!!!")
        result=tk.messagebox.askyesno("Title","Are you willing to play twice?")
        if result==True:
            reset()
        else:
            root.destroy()
            sys.exit()
def f():
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
        button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
        button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
        button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
        button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
        button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
        button7["text"]=="X" and button5["text"]=="X" and button3["text"]=="X" or
        button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" ):
        tk.messagebox.showinfo("CONGRACTS","Player has won")
        result=tk.messagebox.askyesno("Title","Are you willing to play twice?")
        if result==True:
            reset()
        else:
            print("Hope to see you next time")
            root.destroy()
            sys.exit()
        
    if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
        button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
        button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
        button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
        button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
        button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
        button7["text"]=="O" and button5["text"]=="O" and button3["text"]=="O" or
        button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" ):
        tk.messagebox.showinfo("Congratulations","Player2 has won")
        result=tk.messagebox.askyesno("Title","Are you willing to play twice?")
        if result==True:
            reset()
        else:
            root.destroy()
            sys.exit()

def reset():
    global num
    num=0
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "

button=tk.StringVar()

button1=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button1))
button1.grid(row=1,column=0)


button2=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button2))
button2.grid(row=1,column=1)

button3=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button3))
button3.grid(row=1,column=2)
    

button4=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button4))
button4.grid(row=2,column=0)


button5=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button5))
button5.grid(row=2,column=1)

button6=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button6))
button6.grid(row=2,column=2)

button7=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button7))
button7.grid(row=3,column=0)


button8=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button8))
button8.grid(row=3,column=1)

button9=tk.Button(root,text=" ",height=4,width=8,bg="black",fg="red",activebackground="brown",command=lambda:checker(button9))
button9.grid(row=3,column=2)

root.resizable(width=False , height=False)
root.mainloop()
