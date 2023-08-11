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
        self.my_ctclist_old = []
        self.my_ctclist = []
        self.list_info = []
        self.name = ''
        self.email = ''
        self.phone = 0
        self.request_name = ''
        CName_val = False
        CEmail_val = False
        CPhone_val = False

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

        self.edit_btn = Button(self.label_btns, text='Edit', command=self.edit_contactF)
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
        self.getctc_list()

    #Functions 

    #Function to call the events
    def EvnTk(self):
        #Entry event
        self.searchbar_widget.bind('<KeyRelease>', self.check_entryF)

        #Listbox event
        self.listctc_widget.bind('<<ListboxSelect>>', self.show_infoF)

        #Blocking the tab key 
        self.windTwo.unbind_all("<<NextWindow>>")


    #Function to update the listbox
    def update_listboxF(self, data):
        self.listctc_widget.delete(0, END)

        for item in data:
            self.listctc_widget.insert(0, item)


    #Function to check the Entry
    def check_entryF(self, key):
        typed = self.searchbar_widget.get()
        print(typed)

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
        #Control widgets
        self.control_widgets(del_entry=True, forget_entrys=True, forget_add=True,
        disable_search=True, edit_disable=True)
        self.control_widgets(place_done=True, place_entrys=True, configure_entrys=True,
        insert_placeholder=True, placeholder=True, validate_blank=True)
        
        #Change the focus
        self.windTwo.focus()
        self.windTwo.title('Adding a new contact')

    #Function to Cancel Button
    def cancel_buttonF(self):
        #Control widgets
        self.control_widgets(active_search=True, del_entry=True, forget_done=True,
        forget_entrys=True, place_add=True)

        self.done_btn.configure(state='disabled')

        #Change the focus
        self.windTwo.focus()
        self.windTwo.title('Local Contacts')


    #Function to Done Button
    def done_buttonF(self):
        #Control widgets
        self.control_widgets(active_search=True, del_search=True, forget_done=True,
        del_entry=True, place_add=True, edit_active=True)

        #Extracting the data from the entrys
        self.name = self.CName.get()
        self.email = self.CEmail.get()
        self.phone = self.CPhone.get()
        
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
    def show_infoF(self, key, val=None):
        self.windTwo.focus()
        #Verifiy method
        if val != None:
            #Control widgets
            self.control_widgets(forget_done=True, del_entry=True, edit_active=True) 

            #Adding the information
            self.control_widgets(insert_data_entrys=True,
            na=val,
            em=self.email,
            ph=self.phone)

            self.control_widgets(disable_entrys=True)

            #Change the focus and the name
            self.windTwo.focus()
            self.windTwo.title('Contact Information')
        
        else:
            #Request the data
            self.list_info = self.getctc_info(self.get_anchor())

            #Control widget
            self.control_widgets(place_entrys=True, configure_entrys=True,
            edit_active=True, del_entry=True)

            #Adding the data
            self.control_widgets(insert_data_entrys=True,
            na=self.list_info[0],
            em=self.list_info[1],
            ph=self.list_info[2])
            
            self.control_widgets(disable_entrys=True)

            #Change the focus
            self.windTwo.focus()
            self.windTwo.title('Contact Information')
            
            
    #Function to clear the placerholder when click
    def placeholderF(self, key, name=None, email=None, phone=None):
        name_second = self.CName.get()
        email_second = self.CEmail.get()
        phone_second = self.CPhone.get()

        #Validating
        if name == True and name_second == 'Full Name':
            self.CName.delete(0, END)

        if email == True and email_second == 'Email':
            self.CEmail.delete(0, END)

        if phone == True and phone_second == 'Phone Number':
            self.CPhone.delete(0, END)

    
    #Function to validate the state of the button and the entry "Name"
    def validate_blankF(self, key):
        name = self.CName.get()
        while name != '':
            self.done_btn.configure(state='active')
            break
        else:
            self.done_btn.configure(state='disabled')
    

    #Function to remove widgets
    def control_widgets(self, na=None, em=None, ph=None, 
    place_add=None, place_entrys=None, place_done=None, 
    forget_done=None, forget_entrys=None, forget_add=None,
    del_entry=None, disable_search=None, active_search=None,
    configure_entrys=None, placeholder=None, insert_placeholder=None, reset_done=None,
    del_search=None, disable_entrys=None, edit_active=None, edit_disable=None,
    insert_data_entrys=None, validate_blank=None):
        
        if place_add == True:
            #Add the buttons "Add", "Settings" and "Select"
            self.add_btn.place(x=50, y=22, anchor=E)
            self.sel_btn.place(x=260, y=22, anchor=E)
            self.settings_btn.place(x=210, y=22, anchor=E)

        if forget_add == True:
            #Remove the buttons in the main 
            self.add_btn.place_forget()
            self.sel_btn.place_forget()
            self.settings_btn.place_forget()

        if place_done == True:
            #Add the buttons "Cancel" and "Done"
            self.cancel_btn.place(x=100, y=22, anchor=E)
            self.done_btn.place(x=480, y=22, anchor=E)

        if forget_done == True:
            #Remove the buttons in the add stage or edit
            self.cancel_btn.place_forget()
            self.done_btn.place_forget()

        if disable_search == True:
            #Disabled the search
            self.searchbar_widget.configure(state='readonly')
            self.listctc_widget.configure(state='disabled')

        if active_search == True:
            #Active the search
            self.searchbar_widget.configure(state='normal')
            self.listctc_widget.configure(state='normal')

        if place_entrys == True:
            #Add the entrys
            self.CName.place(x=250, y=150, anchor=CENTER)
            self.CEmail.place(x=250, y=270, anchor=CENTER)
            self.CPhone.place(x=250, y=390, anchor=CENTER)

        if del_entry == True:
            #Delete the entrys
            self.CName.configure(state='normal')
            self.CEmail.configure(state='normal')
            self.CPhone.configure(state='normal')
            self.CName.delete(0, END)
            self.CEmail.delete(0, END)
            self.CPhone.delete(0, END)
            
        if insert_placeholder == True:
            #Delete the entrys
            self.CName.delete(0, END)
            self.CEmail.delete(0, END)
            self.CPhone.delete(0, END)

            #Insert in the entry
            self.CName.insert(0, 'Full Name')
            self.CEmail.insert(0, 'Email')
            self.CPhone.insert(0, 'Number Phone')

        if configure_entrys == True:
            #Configure entrys
            self.CName.configure(state='normal', width=25, font=('Arial', 15))
            self.CEmail.configure(state='normal', width=25, font=('Arial', 15))
            self.CPhone.configure(state='normal', width=25, font=('Arial', 15))
        
        if disable_entrys == True:
            #Disabled entrys
            self.CName.configure(state='readonly')
            self.CEmail.configure(state='readonly')
            self.CPhone.configure(state='readonly')

        if forget_entrys == True:
            #Remove the entrys
            self.CName.place_forget()
            self.CEmail.place_forget()
            self.CPhone.place_forget()
 
        if del_search == True:
            #Delete search bar text
            self.searchbar_widget.delete(0, END)

        if edit_active == True:
            #Adding the button to edit
            self.edit_btn.place(x=480, y=22, anchor=E)

        if edit_disable == True:
            #Removing the edit button
            self.edit_btn.place_forget()

        if insert_data_entrys == True:
            #Delete the entrys
            self.CName.delete(0, END)
            self.CEmail.delete(0, END)
            self.CPhone.delete(0, END)

            #Insert the data in the entry
            self.CName.insert(0, na)
            self.CEmail.insert(0, em)
            self.CPhone.insert(0, ph)
        
        if placeholder == True:
            #Deleting the placeholder
            self.CName.bind("<FocusIn>", lambda m="I love aitsuki nakuru": self.placeholderF(0, name=True))
            self.CEmail.bind("<FocusIn>", lambda m="I love aitsuki nakuru": self.placeholderF(0, email=True))
            self.CPhone.bind("<FocusIn>", lambda m="I love aitsuki nakuru": self.placeholderF(0, phone=True))
        
        if validate_blank == True:
            #Validating blank
            self.CName.bind("<KeyRelease>", self.validate_blankF)
    #SQLITE FUNCTIONS

    #Function to connect the basedata
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    

    #Function to get the contactos from database
    def getctc_list(self):
        #Quering the data
        query = 'SELECT name FROM contacts ORDER BY name DESC'
        db_rows = self.run_query(query)
        
        #Filling the list
        for rows in db_rows:
            self.my_ctclist_old = ''.join(rows)
            self.my_ctclist.insert(0, self.my_ctclist_old)
            self.update_listboxF(self.my_ctclist)
            

    #Function to get the data from database with name
    def getctc_info(self, request):
        #Quering the data
        query = f"SELECT name, email, phone FROM contacts WHERE name LIKE {request}"
        db_rows = self.run_query(query)
        for rows in db_rows:
            name = rows[0]
            email = rows[1]
            phone = rows[2]
        return name, email, phone

    
    #Function to get the ANCHOR from the listbox
    def get_anchor(self):
        #Convert the lst into a string with aitsuki help
        lst = self.listctc_widget.get(ANCHOR)
        lst_join = "".join(lst)
        nakuru = "'"
        aitsuki = "'"
        self.request_name = aitsuki + lst_join + nakuru
        self.windTwo.focus()
        return self.request_name


    #Function to insert the data in the database
    def add_contactF(self):
        query = 'INSERT INTO contacts VALUES(NULL, ?, ?, ?)'
        parameters = (self.name, self.email, self.phone)
        self.run_query(query, parameters)


#Function to edit the data in the database
    def edit_contactF(self):
        self.control_widgets(disable_search=True, forget_add=True, edit_disable=True, 
        place_done=True, reset_done=True, place_entrys=True, configure_entrys=True, 
        del_entry=True, placeholder=True, validate_blank=True)


        #Change the focus
        self.windTwo.focus()
        self.windTwo.title('Editing a contact')


if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()