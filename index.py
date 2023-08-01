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
        self.windTwo.geometry("800x588+300+300")
        self.windTwo.resizable(False, False)
        self.windTwo.configure(bg='#1F1F1F')

        #Labels
        self.lblbtn = Label(self.windTwo, height=2, width=28)
        self.lblbtn.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.lblbtn.place(x=139, y=52, anchor=S)

        self.lblsrc = Label(self.windTwo, height=23, width=28)
        self.lblsrc.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.lblsrc.place(x=139, y=52, anchor=N)




        #Buttons

        # Buttons Navigation

        #Add Contacts
        self.addctc = Button(self.lblbtn, text='+')
        self.addctc.config(height=1, width=1, font='Arial 5')
        self.addctc.place(x=50, y=22, anchor=E)

        #Select Contacts
        self.selctc = Button(self.lblbtn, text='+')
        self.selctc.config(height=1, width=1, font='Arial 5')
        self.selctc.place(x=260, y=22, anchor=E)

        #Settings
        self.sngs = Button(self.lblbtn, text='+')
        self.sngs.config(height=1, width=1, font='Arial 5')
        self.sngs.place(x=210, y=22, anchor=E)

        #Search Bar




if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()