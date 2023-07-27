from tkinter import ttk
from tkinter import * 

class Product:

    def __init__(self, window):
        
        #+++++++++++++++++++
        # Windows Attributes
        #+++++++++++++++++++

        self.wind = window
        self.wind.title('Contacts')
        self.wind.geometry('800x600')
        self.wind.resizable(False, False)
        self.wind.configure(bg='gray')

        self.slctxt = Canvas(self.wind, width=780, height=100, bg='gray', relief='groove')
        self.slctxt.create_text(390, 50, text='Select one method to save the contacts', fill="black", font=('Arial 20 bold'))
        self.slctxt.pack(side=TOP)
        self.localctc = Button(self.wind, text='Save Contacts Locally', width=25, height=2, bg='gray', font=('Arial 20 bold'))
        self.localctc.place(relx=0.5, rely=0.5, anchor=CENTER)



if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()