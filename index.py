from tkinter import ttk
from tkinter import * 

class Product:

    def __init__(self, window):
        
        self.wind = window
        self.wind.title('Contacts')
        self.wind.geometry('800x800')
        self.wind.resizable(False, False)
        self.wind.configure(bg='gray')


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()