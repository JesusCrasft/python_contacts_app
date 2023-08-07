from tkinter import ttk
from tkinter import * 

class Product:

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
        self.my_ctclist = ['Aimel', 'Pablo', 'Jaimar', 'Shawnee', 'Jesus']

        #Label Add Contact
        self.LblCtc = Label(self.windTwo, height=23, width=50)
        self.LblCtc.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblCtc.place(x=550, y=52, anchor=N)

        #Labels Buttons Navigation
        self.LblBtnF = Label(self.windTwo, height=2, width=29)
        self.LblBtnF.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblBtnF.place(x=149, y=52, anchor=S)

        self.LblBtnS = Label(self.windTwo, height=2, width=50)
        self.LblBtnS.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblBtnS.place(x=550, y=52, anchor=S)

        #Add Contacts
        self.AddCW = Button(self.LblBtnF, text='+', command=self.AddCF)
        self.AddCW.config(height=1, width=1, font=('Arial',5))
        self.AddCW.place(x=50, y=22, anchor=E)

        #Select Contacts
        self.SelCW = Button(self.LblBtnF, text='+')
        self.SelCW.config(height=1, width=1, font=('Arial',5))
        self.SelCW.place(x=260, y=22, anchor=E)

        #Settings
        self.SngsW = Button(self.LblBtnF, text='+')
        self.SngsW.config(height=1, width=1, font=('Arial',5))
        self.SngsW.place(x=210, y=22, anchor=E)



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
        pass


    #Function to show the information of the selected contact
    def ShowICF(self, key):
        pass


if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()