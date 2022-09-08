from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.geometry("900x600")
root.title("Classes")

elements=["label","button","dropdown"]
box=ttk.Combobox(root,state="readonly",values=elements)
box.pack(padx=20,pady=10)

class CreateElements:
    def __init__(self):
        print("This is the CreateElements Classs")
    
    def createLabel(self):
        label=Label(root,text="A new label is been created using class")
        label.pack()
     
        
    def createButton(self):
        btn=Button(root,text="button",command= self.message)
        btn.pack(padx=20,pady=10)
        
    def createDropdown(self):
        elements=[1,2,3]
        box1=ttk.Combobox(root,state="readonly",values=elements)
        box1.pack(padx=20,pady=10)
    
    def choose(self):
        global box
        var=box.get()
        if(var=="label"):
            self.createLabel()
        elif(var=="button"):
            self.createButton()
        else:
            self.createDropdown()
        
    def message(self):
        messagebox.showinfo("showinfo"," You clicked the button created using class")

obj=CreateElements()

btn1=Button(root,text="Click to create label,Button Or Dropdown Element",command=obj.choose)
btn1.pack(padx=20,pady=10)

root.mainloop()
          