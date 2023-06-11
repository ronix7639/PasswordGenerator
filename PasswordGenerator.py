#Password Generator
from tkinter import *
import string
import random
import pyperclip
def generator():
    s1=string.ascii_lowercase
    #print(s1)
    s2=string.ascii_uppercase
    #print(s2)
    s3=string.digits
    #print(s3)
    s4=string.punctuation
    #print(s4)

    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print(s)

    password_length=int(lengthbox.get())
    if choice.get()==1:
        passwordfield.insert(0,random.sample(s1+s2,password_length))
    elif choice.get()==2:
        passwordfield.insert(0,random.sample(s1+s2+s3,password_length))
    elif choice.get()==3:
        passwordfield.insert(0,random.sample(s,password_length))


    # password=random.sample(s,password_length)
    # passwordfield.insert(0,password)
    
def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)


root=Tk()
root.title('Password Generator')
root.config(bg="grey30")
choice=IntVar()
Font=('Times New Roman',16,'bold')
passwordLabel=Label(root,text='Password Generator',font=('Times New Roman',25,'bold'),bg='gray30',fg="black")
passwordLabel.grid(pady=10)
weakradiobutton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradiobutton.grid(pady=7)

mediumradiobutton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradiobutton.grid(pady=7)

strongradiobutton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradiobutton.grid(pady=7)

passwordlengthLabel=Label(root,text='Password Length',font=Font,bg='gray30',fg="white")
passwordlengthLabel.grid(pady=10)

lengthbox=Spinbox(root,from_=5,to_=20,width=7,font=Font)
lengthbox.grid(pady=7)


generatebutton =Button(root,text='Generate Password',font=Font,command=generator)
generatebutton.grid(pady=7)

passwordfield=Entry(root,width=25,bd=3,font=Font)
passwordfield.grid(pady=7)

copybutton=Button(root,text='Copy password',font=Font,command=copy)
copybutton.grid()

root.mainloop()

