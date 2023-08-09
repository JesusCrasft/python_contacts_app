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
        self.LocalCtc = Button(self.windOne, text='Save Contacts Locally', command=self.secondary_window)
        self.LocalCtc.configure(width=25, height=2, bg='#1F1F1F', fg='white', highlightthickness='0', font=('Arial 15 bold'))
        self.LocalCtc.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    #Secondary Window

    #Function: Secondary window creation
    def secondary_window(self):
        self.windOne.destroy()

        #Secondary Window Attributes
        
        SryWind = Tk()
        self.windTwo = SryWind
        self.windTwo.title('Local Contacts')
        self.windTwo.geometry("804x588+300+300")
        self.windTwo.resizable(False, False)
        self.windTwo.configure(bg='#1F1F1F')

        #Variables
        self.my_ctclist = []
        self.name = ''
        self.email = ''
        self.phone = 0

        #Label Add Contact
        self.label_addctc = Label(self.windTwo, height=23, width=50)
        self.label_addctc.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_addctc.place(x=550, y=52, anchor=N)

        self.CName = Entry(self.label_addctc)
        self.CEmail = Entry(self.label_addctc)        
        self.CPhone = Entry(self.label_addctc)


        #Labels Buttons Navigation
        self.label_btnf = Label(self.windTwo, height=2, width=29)
        self.label_btnf.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_btnf.place(x=149, y=52, anchor=S)

        self.label_btns = Label(self.windTwo, height=2, width=50)
        self.label_btns.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_btns.place(x=550, y=52, anchor=S)

        #Add Contacts
        self.add_btn = Button(self.label_btnf, text='+', command=self.add_buttonF)
        self.add_btn.configure(height=1, width=1, font=('Arial',5))
        self.add_btn.place(x=50, y=22, anchor=E)

        #Select Contacts
        self.sel_btn = Button(self.label_btnf, text='+')
        self.sel_btn.configure(height=1, width=1, font=('Arial',5))
        self.sel_btn.place(x=260, y=22, anchor=E)

        #Settings
        self.settings_btn = Button(self.label_btnf, text='+')
        self.settings_btn.configure(height=1, width=1, font=('Arial',5))
        self.settings_btn.place(x=210, y=22, anchor=E)

        #Cancel Button
        self.cancel_btn = Button(self.label_btns, text='Cancel', command=self.cancel_buttonF)
        self.cancel_btn.configure(height=1, width=5, font=('Arial',10))

        #Done Button
        self.done_btn = Button(self.label_btns, text='Done', state='disabled', command=self.done_buttonF)
        self.done_btn.configure(height=1, width=5, font=('Arial',10))

        self.edit_btn = Button(self.label_btns, text='Edit')
        self.edit_btn.configure(height=1, width=5, font=('Arial',10))


        #Label Search Widgets
        self.label_search = Label(self.windTwo, height=23, width=29)
        self.label_search.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_search.place(x=149, y=52, anchor=N)

        #Search Bar
        self.searchbar_widget = Entry(self.label_search)
        self.searchbar_widget.configure(width=15, font=('Arial',20), bg='#323232', fg='white')
        self.searchbar_widget.place(x=145, y=47, anchor=S)

        #List of Contacts
        self.listctc_widget = Listbox(self.label_search)
        self.listctc_widget.configure(height=18, width=15, bg='#1F1F1F', font=('Arial', 20), fg='white')
        self.listctc_widget.place(x=145, y=50, anchor=N)

        #Calling the functions
        self.EvnTk()
        self.get_contacts()

    #Functions 

    #Function to call the events
    def EvnTk(self):
        #Entry event
        self.searchbar_widget.bind('<KeyRelease>', self.check_entryF)

        #Listbox event
        self.listctc_widget.bind('<<ListboxSelect>>', self.show_infoF)


    #Function to update the listbox
    def update_listboxF(self, data):
        self.listctc_widget.delete(0, END)

        for item in data:
            self.listctc_widget.insert(0, item)


    #Function to check the Entry
    def check_entryF(self, key):
        typed = self.searchbar_widget.get()

        if typed == '':
            data = self.my_ctclist

        else:
            data = []
            for item in self.my_ctclist:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update_listboxF(data)


    #Function to create a new contact
    def add_buttonF(self):
        #Disabled the search
        self.searchbar_widget.configure(state='readonly')
        self.listctc_widget.configure(state='disabled')

        #Remove the buttons and replace
        self.add_btn.place_forget()
        self.sel_btn.place_forget()
        self.settings_btn.place_forget()
        self.edit_btn.place_forget()

        #Add the buttons "Cancel" and "Done"
        self.done_btn.configure(state='disabled')
        self.cancel_btn.place(x=100, y=22, anchor=E)
        self.done_btn.place(x=480, y=22, anchor=E)

        
        #Adding the entrys to add the information
        self.CName.configure(state='normal', width=25, font=('Arial', 15))
        self.CName.delete(0, END)
        self.CName.insert(0, 'Full Name')
        self.CName.bind("<FocusIn>", self.placeholderF)
        self.CName.bind("<KeyRelease>", self.validate_blankF)
        self.CName.place(x=250, y=150, anchor=CENTER)
        
        self.CEmail.configure(state='normal', width=25, font=('Arial', 15))
        self.CEmail.delete(0, END)
        self.CEmail.insert(0, 'Email')
        self.CEmail.bind("<FocusIn>", self.placeholderF)
        self.CEmail.place(x=250, y=270, anchor=CENTER)
        
        self.CPhone.configure(state='normal', width=25, font=('Arial', 15))
        self.CPhone.delete(0, END)
        self.CPhone.insert(0, 'Number Phone')
        self.CPhone.bind("<FocusIn>", self.placeholderF)
        self.CPhone.place(x=250, y=390, anchor=CENTER)

        #Change the focus
        self.windTwo.focus()



    #Function to Cancel Button
    def cancel_buttonF(self):
        #Active the search
        self.searchbar_widget.configure(state='normal')
        self.listctc_widget.configure(state='normal')

        #Delete the text in the entrys
        self.CName.delete(0, END)
        self.CEmail.delete(0, END)
        self.CPhone.delete(0, END)

        #Remove the buttons, entrys and replace
        self.cancel_btn.place_forget()
        self.done_btn.place_forget()
        self.CName.place_forget()
        self.CEmail.place_forget()
        self.CPhone.place_forget()

        #Add the buttons "Add", "Settings" and "Select"
        self.add_btn.place(x=50, y=22, anchor=E)
        self.sel_btn.place(x=260, y=22, anchor=E)
        self.settings_btn.place(x=210, y=22, anchor=E)

        #Reseting the Done Button
        self.done_btn.configure(state='disabled')

        #Change the focus
        self.windTwo.focus()


    #Function to Done Button
    def done_buttonF(self):
        #Active the search
        self.searchbar_widget.configure(state='normal')
        self.listctc_widget.configure(state='normal')
        self.searchbar_widget.delete(0, END)

        #Extracting the data from the entrys
        self.name = self.CName.get()
        self.email = self.CEmail.get()
        self.phone = self.CPhone.get()

        #Removing the "Add Stage"
        self.cancel_btn.place_forget()
        self.done_btn.place_forget()

        #Delete the text in the entrys
        self.CName.delete(0, END)
        self.CEmail.delete(0, END)
        self.CPhone.delete(0, END)

        #Add the buttons "Add", "Settings" and "Select"
        self.add_btn.place(x=50, y=22, anchor=E)
        self.sel_btn.place(x=260, y=22, anchor=E)
        self.settings_btn.place(x=210, y=22, anchor=E)
        
        #Inserting the name in the contact list
        self.my_ctclist.insert(0, self.name)
        self.update_listboxF(self.my_ctclist)

        #Sending the data to show the contact
        self.show_infoF(0, self.name)

        #Inserting the contact in the database
        self.add_contactF()

        #Change the focus
        self.windTwo.focus()
    


    #Function to show the information of the selected contact
    def show_infoF(self, key, na=None):
        #Verifiy method
        if na != None:
            #Remove the buttons, entrys and replace
            self.cancel_btn.place_forget()
            self.done_btn.place_forget()
            
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
            self.edit_btn.place(x=480, y=22, anchor=E)

            #Change the focus
            self.windTwo.focus()
        
        else:
            print(self.name, self.email, self.phone)
            lst = self.listctc_widget.get(ACTIVE)
            
            if lst == '':
                print('iloveaitsukinakuru')
            else:
                print(lst)
            #Delete the text in the entrys



    #Function to clear the placerholder when click
    def placeholderF(self, key):
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
    def validate_blankF(self, key):
        name = self.CName.get()
        while name != '':
            self.done_btn.configure(state='active')
            break
        else:
            self.done_btn.configure(state='disabled')
        

    #Function to connect the basedata
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    

    #Function to get the contactos from database
    def get_contacts(self):
        #Quering the data
        query = 'SELECT name FROM contacts ORDER BY name DESC'
        db_rows = self.run_query(query)
        print(db_rows)
        
        #Filling the list
        for rows in db_rows:
            self.my_ctclist.insert(0, rows)
            self.update_listboxF(self.my_ctclist)

    
    #Function to insert the data in the database
    def add_contactF(self):
        query = 'INSERT INTO contacts VALUES(NULL, ?, ?, ?)'
        print(self.email)
        parameters = (self.name, self.email, self.phone)
        self.run_query(query, parameters)

if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()