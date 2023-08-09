from tkinter import ttk
from tkinter import * 

import sqlite3

class Product:

    db_name = 'database.db'

    def __init__(self, PryWind):
    
        # Primary Window Attributes

        self.windOne = PryWind
        self.windOne.title('Contacts')
        self.windOne.geometry('800x600')
        self.windOne.resizable(False, False)
        self.windOne.configure(bg='#1F1F1F')

        #Canvas
        self.SelTxt = Canvas(self.windOne, width=780, height=75, bg='#1F1F1F', relief='groove',highlightthickness='0')
        self.SelTxt.create_text(390, 25, text='Select one method to save the contacts', fill='white', font=('Arial 15 bold'))
        self.SelTxt.place(relx=0.5, rely=0.1, anchor=CENTER)

        #Buttons
        self.LocalCtc = Button(self.windOne, text='Save Contacts Locally', command=self.SryWfunc)
        self.LocalCtc.configure(width=25, height=2, bg='#1F1F1F', fg='white', highlightthickness='0', font=('Arial 15 bold'))
        self.LocalCtc.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    #Secondary Window

    #Function: Secondary window creation
    def SryWfunc(self):
        self.windOne.destroy()

        #Secondary Window Attributes
        
        SryWind = Tk()
        self.windTwo = SryWind
        self.windTwo.title('Local Contacts')
        self.windTwo.geometry("804x588+300+300")
        self.windTwo.resizable(False, False)
        self.windTwo.configure(bg='#1F1F1F')

        #Variables
        self.my_ctclist = {
            'name' : '',
            'email' : '',
            'phone' : 0
        }
        self.name = ''
        self.email = ''
        self.phone = 0

        #Label Add Contact
        self.LblCtc = Label(self.windTwo, height=23, width=50)
        self.LblCtc.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblCtc.place(x=550, y=52, anchor=N)

        self.CName = Entry(self.LblCtc)
        self.CEmail = Entry(self.LblCtc)        
        self.CPhone = Entry(self.LblCtc)


        #Labels Buttons Navigation
        self.LblBtnF = Label(self.windTwo, height=2, width=29)
        self.LblBtnF.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblBtnF.place(x=149, y=52, anchor=S)

        self.LblBtnS = Label(self.windTwo, height=2, width=50)
        self.LblBtnS.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblBtnS.place(x=550, y=52, anchor=S)

        #Add Contacts
        self.AddCW = Button(self.LblBtnF, text='+', command=self.AddCF)
        self.AddCW.configure(height=1, width=1, font=('Arial',5))
        self.AddCW.place(x=50, y=22, anchor=E)

        #Select Contacts
        self.SelCW = Button(self.LblBtnF, text='+')
        self.SelCW.configure(height=1, width=1, font=('Arial',5))
        self.SelCW.place(x=260, y=22, anchor=E)

        #Settings
        self.SngsW = Button(self.LblBtnF, text='+')
        self.SngsW.configure(height=1, width=1, font=('Arial',5))
        self.SngsW.place(x=210, y=22, anchor=E)

        #Cancel Button
        self.ClB = Button(self.LblBtnS, text='Cancel', command=self.ClF)
        self.ClB.configure(height=1, width=5, font=('Arial',10))

        #Done Button
        self.DoB = Button(self.LblBtnS, text='Done', state='disabled', command=self.DoF)
        self.DoB.configure(height=1, width=5, font=('Arial',10))

        self.EdB = Button(self.LblBtnS, text='Edit')
        self.EdB.configure(height=1, width=5, font=('Arial',10))


        #Label Search Widgets
        self.LblSrc = Label(self.windTwo, height=23, width=29)
        self.LblSrc.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblSrc.place(x=149, y=52, anchor=N)

        #Search Bar
        self.SrcCW = Entry(self.LblSrc)
        self.SrcCW.configure(width=15, font=('Arial',20), bg='#323232', fg='white')
        self.SrcCW.place(x=145, y=47, anchor=S)

        #List of Contacts
        self.LstCW = Listbox(self.LblSrc)
        self.LstCW.configure(height=18, width=15, bg='#1F1F1F', font=('Arial', 20), fg='white')
        self.LstCW.place(x=145, y=50, anchor=N)

        self.EvnTk()

    #Functions 

    #Function to call the events
    def EvnTk(self):
        #Entry event
        self.SrcCW.bind('<KeyRelease>', self.CheckF)

        #Listbox event
        self.LstCW.bind('<<ListboxSelect>>', self.ShowICF)


    #Function to update the listbox
    def UpdateF(self, data):
        self.LstCW.delete(0, END)

        for item in data:
            self.LstCW.insert(0, item)


    #Function to check the Entry
    def CheckF(self, key):
        typed = self.SrcCW.get()

        if typed == '':
            data = self.my_ctclist

        else:
            data = []
            for item in self.my_ctclist:
                if typed.lower() in item.lower():
                    data.append(item)

        self.UpdateF(data)


    #Function to create a new contact
    def AddCF(self):
        #Disabled the search
        self.SrcCW.configure(state='readonly')
        self.LstCW.configure(state='disabled')

        #Remove the buttons and replace
        self.AddCW.place_forget()
        self.SelCW.place_forget()
        self.SngsW.place_forget()
        self.EdB.place_forget()

        #Add the buttons "Cancel" and "Done"
        self.DoB.configure(state='disabled')
        self.ClB.place(x=100, y=22, anchor=E)
        self.DoB.place(x=480, y=22, anchor=E)

        
        #Adding the entrys to add the information
        self.CName.configure(state='normal', width=25, font=('Arial', 15))
        self.CName.delete(0, END)
        self.CName.insert(0, 'Full Name')
        self.CName.bind("<FocusIn>", self.PlaceHCF)
        self.CName.bind("<KeyRelease>", self.ValF)
        self.CName.place(x=250, y=150, anchor=CENTER)
        
        self.CEmail.configure(state='normal', width=25, font=('Arial', 15))
        self.CEmail.delete(0, END)
        self.CEmail.insert(0, 'Email')
        self.CEmail.bind("<FocusIn>", self.PlaceHCF)
        self.CEmail.place(x=250, y=270, anchor=CENTER)
        
        self.CPhone.configure(state='normal', width=25, font=('Arial', 15))
        self.CPhone.delete(0, END)
        self.CPhone.insert(0, 'Number Phone')
        self.CPhone.bind("<FocusIn>", self.PlaceHCF)
        self.CPhone.place(x=250, y=390, anchor=CENTER)

        #Change the focus
        self.windTwo.focus()



    #Function to Cancel Button
    def ClF(self):
        #Active the search
        self.SrcCW.configure(state='normal')
        self.LstCW.configure(state='normal')

        #Delete the text in the entrys
        self.CName.delete(0, END)
        self.CEmail.delete(0, END)
        self.CPhone.delete(0, END)

        #Remove the buttons, entrys and replace
        self.ClB.place_forget()
        self.DoB.place_forget()
        self.CName.place_forget()
        self.CEmail.place_forget()
        self.CPhone.place_forget()

        #Add the buttons "Add", "Settings" and "Select"
        self.AddCW.place(x=50, y=22, anchor=E)
        self.SelCW.place(x=260, y=22, anchor=E)
        self.SngsW.place(x=210, y=22, anchor=E)

        #Reseting the Done Button
        self.DoB.configure(state='disabled')

        #Change the focus
        self.windTwo.focus()


    #Function to Done Button
    def DoF(self):
        #Active the search
        self.SrcCW.configure(state='normal')
        self.LstCW.configure(state='normal')
        self.SrcCW.delete(0, END)

        #Extracting the data from the entrys

        #Removing the "Add Stage"
        self.ClB.place_forget()
        self.DoB.place_forget()

        #Delete the text in the entrys
        self.CName.delete(0, END)
        self.CEmail.delete(0, END)
        self.CPhone.delete(0, END)

        #Add the buttons "Add", "Settings" and "Select"
        self.AddCW.place(x=50, y=22, anchor=E)
        self.SelCW.place(x=260, y=22, anchor=E)
        self.SngsW.place(x=210, y=22, anchor=E)
        
        #Inserting the name in the contact list
        data = self.my_ctclist

        #Sending the data to show the contact
        self.UpdateF(data)
        self.ShowICF(0, self.name)

        #Change the focus
        self.windTwo.focus()
            


    #Function to show the information of the selected contact
    def ShowICF(self, key, na=None):
        #Verifiy method
        if na != None:
            #Remove the buttons, entrys and replace
            self.ClB.place_forget()
            self.DoB.place_forget()
            
            #Delete the text in the entrys
            self.CName.delete(0, END)
            self.CEmail.delete(0, END)
            self.CPhone.delete(0, END)

            #Adding the information
            self.CName.insert(0, na)
            self.CEmail.insert(0, self.email)
            self.CPhone.insert(0, self.phone)

            #Disabled entrys
            self.CName.configure(state='readonly')
            self.CEmail.configure(state='readonly')
            self.CPhone.configure(state='readonly')

            #Adding the button to edit
            self.EdB.place(x=480, y=22, anchor=E)

            #Change the focus
            self.windTwo.focus()
        
        else:
            lst = self.LstCW.get(ACTIVE)
            
            if lst == '':
                print('iloveaitsukinakuru')
            else:
                print(lst)
            #Delete the text in the entrys


        


    #Function to clear the placerholder when click
    def PlaceHCF(self, key):
        name = self.CName.get()
        email = self.CEmail.get()
        phone = self.CPhone.get()

        #Cleaning the entrys
        if name == 'Full Name':
            self.CName.delete(0, END)

        elif email == 'Email':
            self.CEmail.delete(0, END)

        elif phone == 'Number Phone':
            self.CPhone.delete(0, END)

    
    #Function to validate the state of the button and the entry "Name"
    def ValF(self, key):
        name = self.CName.get()
        while name != '':
            self.DoB.configure(state='active')
            break
        else:
            self.DoB.configure(state='disabled')

        


if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()