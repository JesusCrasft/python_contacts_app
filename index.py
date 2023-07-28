from tkinter import ttk
from tkinter import * 

class Product:

    def __init__(self, window):
    
        # Windows Attributes

        self.PryWind = window
        self.PryWind.title('Contacts')
        self.PryWind.geometry('800x600')
        self.PryWind.resizable(False, False)
        self.PryWind.configure(bg='#1F1F1F')

        #Primary Window

        #Canvas
        self.slctxt = Canvas(self.PryWind, width=780, height=75, bg='#1F1F1F', relief='groove',highlightthickness='0')
        self.slctxt.create_text(390, 25, text='Select one method to save the contacts', fill='white', font=('Arial 15 bold'))
        self.slctxt.place(relx=0.5, rely=0.1, anchor=CENTER)

        #Buttons
        self.localctc = Button(self.PryWind, text='Save Contacts Locally', command=self.SryWfunc)
        self.localctc.configure(width=25, height=2, bg='#1F1F1F', fg='white', highlightthickness='0', font=('Arial 15 bold'))
        self.localctc.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Secondary Window

    def SryWfunc(self):
        self.PryWind.destroy()

        self.SryWind = Toplevel()
        self.SryWind.title('Local Contacts')
        self.SryWind.geometry('800x600')
        self.SryWind.resizable(False, False)
        self.SryWind.configure(bg='#1F1F1F')



if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()