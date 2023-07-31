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

        #Primary Window

        #Canvas
        self.seltxt = Canvas(self.windOne, width=780, height=75, bg='#1F1F1F', relief='groove',highlightthickness='0')
        self.seltxt.create_text(390, 25, text='Select one method to save the contacts', fill='white', font=('Arial 15 bold'))
        self.seltxt.place(relx=0.5, rely=0.1, anchor=CENTER)

        #Buttons
        self.localctc = Button(self.windOne, text='Save Contacts Locally', command=self.SryWfunc)
        self.localctc.configure(width=25, height=2, bg='#1F1F1F', fg='white', highlightthickness='0', font=('Arial 15 bold'))
        self.localctc.place(relx=0.5, rely=0.5, anchor=CENTER)


        #Secondary Window

    #Function: Secondary window creation
    def SryWfunc(self):
        self.windOne.destroy()

        # Secondary Window Attributes
        
        SryWind = Tk()
        self.windTwo = SryWind
        self.windTwo.title('Local Contacts')
        self.windTwo.geometry('800x600')
        self.windTwo.resizable(False, False)
        self.windTwo.configure(bg='#1F1F1F')


        #Labels
        self.lblbtn = Label(self.windTwo, height=1, width=27)
        self.lblbtn.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.lblbtn.place(x=151, y=34, anchor=S)


        #Buttons

        # Buttons Navigation

        #Add Contacts
        self.addctc = Button(self.lblbtn, text='+')
        self.addctc.config(height=1, width=1, font='Arial 5')
        self.addctc.place(x=50, y=14, anchor=E)

        #Select Contacts
        self.selctc = Button(self.lblbtn, text='+')
        self.selctc.config(height=1, width=1, font='Arial 5')
        self.selctc.place(x=250, y=14, anchor=E)

        #Settings
        self.stings = Button(self.lblbtn, text='+')
        self.stings.config(height=1, width=1, font='Arial 5')
        self.stings.place(x=150, y=14, anchor=E)


if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()