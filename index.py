from tkinter import ttk
from tkinter import colorchooser
from tkinter import * 

class Product:

    def __init__(self, PryWind):
    
        # Primary Window Attributes

        self.windOne = PryWind
        self.windOne.title('Contacts')
        self.windOne.geometry('800x600')
        self.windOne.resizable(False, False)
        self.windOne.configure(bg='#1F1F1F')

        #Primary Window

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

        # Secondary Window Attributes
        
        SryWind = Tk()
        self.windTwo = SryWind
        self.windTwo.title('Local Contacts')
        self.windTwo.geometry("800x588+300+300")
        self.windTwo.resizable(False, False)
        self.windTwo.configure(bg='#1F1F1F')

        #Labels
        self.LblBtn = Label(self.windTwo, height=2, width=29)
        self.LblBtn.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblBtn.place(x=149, y=52, anchor=S)

        self.LblSrc = Label(self.windTwo, height=23, width=29)
        self.LblSrc.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.LblSrc.place(x=149, y=52, anchor=N)


        #Buttons

        # Buttons Navigation

        #Add Contacts
        self.AddCtc = Button(self.LblBtn, text='+')
        self.AddCtc.config(height=1, width=1, font=('Arial',5))
        self.AddCtc.place(x=50, y=22, anchor=E)

        #Select Contacts
        self.SelCtc = Button(self.LblBtn, text='+')
        self.SelCtc.config(height=1, width=1, font=('Arial',5))
        self.SelCtc.place(x=260, y=22, anchor=E)

        #Settings
        self.Sngs = Button(self.LblBtn, text='+')
        self.Sngs.config(height=1, width=1, font=('Arial',5))
        self.Sngs.place(x=210, y=22, anchor=E)


        #Search Bar
        self.SrcCtc = Text(self.LblSrc)
        self.SrcCtc.configure(height=1, width=15, font=('Arial',20), bg='#323232', fg='white')
        self.SrcCtc.place(x=145, y=52, anchor=S)


if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()