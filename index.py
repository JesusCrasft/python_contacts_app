from tkinter import ttk
from tkinter import * 
from validate_email import *

import phonenumbers
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
        self.list_id = []
        self.list_old_id = []
        self.name = ''
        self.email = ''
        self.phone = ''
        self.id = ''
        self.request_name = ''
        self.select_id = ''
        self.title_wind = ''
        self.label_wind = ''
        self.label_btns_text = 'Select a Contact'

        #Label Add Contact
        self.label_stage = Label(self.windTwo, height=23, width=50)
        self.label_stage.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_stage.place(x=550, y=52, anchor=N)

        self.CName = Entry(self.label_stage, exportselection=False, bg='#323232', fg='white',
        highlightbackground='#1F1F1F')
        self.CEmail = Entry(self.label_stage, exportselection=False, bg='#323232', fg='white',
        highlightbackground='#1F1F1F')        
        self.CPhone = Entry(self.label_stage, exportselection=False, bg='#323232', fg='white',
        highlightbackground='#1F1F1F')


        #Labels Buttons Navigation
        self.label_btnf = Label(self.windTwo, height=2, width=29)
        self.label_btnf.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_btnf.place(x=149, y=52, anchor=S)

        self.label_btns = Label(self.windTwo, height=2, width=50, text=self.label_btns_text)
        self.label_btns.configure(background='#1F1F1F', relief=SOLID, borderwidth=2, fg='white')
        self.label_btns.place(x=550, y=52, anchor=S)

        #Add Contacts
        self.img_add_btn = PhotoImage(file='img/img_add_btn.png')
        self.add_btn = Button(self.label_btnf, image=self.img_add_btn, command=self.add_buttonF)
        self.add_btn.configure(height=30, width=30, borderwidth=0, bg='#1F1F1F', highlightbackground='#1F1F1F')
        self.add_btn.place(x=50, y=22, anchor=E )

        #Select Contacts
        self.img_sel_btn = PhotoImage(file='img/img_sel_btn.png')
        self.sel_btn = Button(self.label_btnf, image=self.img_sel_btn)
        self.sel_btn.configure(height=30, width=30, borderwidth=0, bg='#1F1F1F', highlightbackground='#1F1F1F')
        self.sel_btn.place(x=210, y=22, anchor=E)

        #Settings
        self.img_settings_btn = PhotoImage(file='img/img_settings_btn.png')
        self.settings_btn = Button(self.label_btnf, image=self.img_settings_btn)
        self.settings_btn.configure(height=30, width=30, borderwidth=0, bg='#1F1F1F', highlightbackground='#1F1F1F')
        self.settings_btn.place(x=260, y=22, anchor=E)

        #Cancel Button
        self.cancel_btn = Button(self.label_btns, text='Cancel', command=self.cancel_buttonF)
        self.cancel_btn.configure(height=1, width=5, font=('Arial', 10, 'bold'),
        bg='gray', activebackground='#676767', activeforeground='white', fg='black', highlightbackground='#1F1F1F')

        #Done Button
        self.done_btn = Button(self.label_btns, text='Done', state='disabled')
        self.done_btn.configure(height=1, width=5, font=('Arial', 10, 'bold'), highlightbackground='#1F1F1F')

        #Edit Button
        self.img_edit_btn = PhotoImage(file='img/img_edit_btn.png')
        self.edit_btn = Button(self.label_btns, image=self.img_edit_btn, command=self.edit_buttonF)
        self.edit_btn.configure(height=30, width=30, borderwidth=0, bg='#1F1F1F', highlightbackground='#1F1F1F')

        #Delete Button
        self.img_delete_btn = PhotoImage(file='img/img_delete_btn.png')
        self.delete_btn = Button(self.label_btns, image=self.img_delete_btn, command=self.delete_buttonF)
        self.delete_btn.configure(height=30, width=30, borderwidth=0, bg='#1F1F1F', highlightbackground='#1F1F1F')

        #Label Search Widgets
        self.label_search = Label(self.windTwo, height=23, width=29)
        self.label_search.configure(background='#1F1F1F', relief=SOLID, borderwidth=2)
        self.label_search.place(x=149, y=52, anchor=N)

        #Search Bar
        self.searchbar_widget = Entry(self.label_search)
        self.searchbar_widget.configure(width=15, font=('Arial',20), bg='#323232', fg='white',
        highlightbackground='#1F1F1F')
        self.searchbar_widget.place(x=145, y=47, anchor=S)

        #List of Contacts
        self.listctc_widget = Listbox(self.label_search, selectmode=SINGLE , exportselection=False)
        self.listctc_widget.configure(height=18, width=15, bg='#1F1F1F', font=('Arial', 20), fg='white',
        highlightbackground='#1F1F1F', borderwidth=0)
        self.listctc_widget.place(x=145, y=50, anchor=N)

        #Calling the functions
        self.EvnTk()
        self.getctc_list()

    #Functions 

    #Function to call the events
    def EvnTk(self):
        #Blocking the tab key 
        self.windTwo.unbind_all("<<NextWindow>>")

        #Entry event
        self.searchbar_widget.bind('<KeyRelease>', self.check_entryF)

        #Listbox event
        self.listctc_widget.bind('<<ListboxSelect>>', lambda m="": self.show_infoF(0, val_list=True))


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


    #Function to mount the Add Stage
    def add_buttonF(self):
        #Control widgets
        self.control_widgets('del_search', 'del_entry', 'forget_entrys', 'forget_select_stage',
        'disable_search', 'forget_edit_stage')
        self.control_widgets('place_add_stage', 'place_entrys', 'reset_entrys',
        'insert_placeholder', 'placeholder','validate_add_stage', 'done_add_btn', 'reset_done_btn')
        
        #Label name
        self.label_btns_text = 'Adding a new Contact'
        self.control_widgets('refresh_label')

        #Change the focus
        self.windTwo.focus()


    #Function to mount the Select Stage
    def cancel_buttonF(self):
        #Control widgets
        self.control_widgets('del_search', 'active_search', 'del_entry', 'forget_add_stage',
        'forget_entrys', 'place_select_stage', 'reset_done_btn')

        #Label name
        self.label_btns_text = 'Select a Contact'
        self.control_widgets('refresh_label')

        #Change the focus
        self.windTwo.focus()


    #Function to mount the Edit Stage
    def edit_buttonF(self):
        #Control widgets
        self.control_widgets('disable_search', 'del_search', 'forget_edit_stage',
        'forget_select_stage', 'place_add_stage', 'reset_entrys', 'validate_edit_stage',
        'done_edit_btn', 'reset_done_btn')

        #Between string
        self.convert_thingsF(self.CName.get())
        
        #Label name
        self.label_btns_text = 'Editing a Contact'
        self.control_widgets('refresh_label')

        #Change the focus
        self.windTwo.focus()


    #Function to mount the Delete Stage
    def delete_buttonF(self):
        #Title name and Label name
        self.title_wind = 'Delete Contact'
        self.label_wind = 'Want to delete this contact?'
        
        #Create the window and disable all buttons
        self.control_widgets('disable_all_btn', 'create_wind', 'fill_wind', 'fill_delete')

        #Validation var
        self.email = self.CEmail.get()
        self.phone = self.CPhone.get()

        #Check if the window is closed with the X button
        self.wind.bind("<Destroy>", lambda m="": self.destroy_windowsF(event="delete_wind"))


    #Function to mount the Wrong stage
    def invalid_entryF(self):
        #Title Name
        self.title_wind = 'Invalid Data'

        #Create the window and disable all buttons
        self.control_widgets('disable_all_btn', 'create_wind')

        #Validate to create the window warn
        if self.phone == False and self.email == False:
            self.label_wind = 'Invalid Phone Number and Email Address'
            self.control_widgets('fill_wind', 'fill_invalid')

        elif self.phone == False:
            self.label_wind = 'Invalid Number Phone'
            self.control_widgets('fill_wind', 'fill_invalid')

        elif self.email == False:
            self.label_wind = 'Invalid Email Address'
            self.control_widgets('fill_wind', 'fill_invalid')

        #Check if the window is closed with the X button
        self.wind.bind("<Destroy>", lambda m="": self.destroy_windowsF(event='invalid_wind'))


    #Function to Add Done Button
    def done_addF(self):
        #Extract the data and validate the data
        self.name = self.CName.get()
        self.email = self.validate_emailF(self.CEmail.get())
        self.phone = self.validate_phoneF(self.CPhone.get())

        #Validate the entrys
        if self.phone != False and self.email != False:
            if self.name.isspace():
                self.name = 'Unnamed'

            #Control widgets
            self.control_widgets('active_search', 'del_search', 'forget_add_stage',
            'place_select_stage', 'place_edit_stage')

            #Inserting the name in the contact list
            self.my_ctclist_old = []
            self.my_ctclist = []

            #Sending the data to show the contact
            self.show_infoF(0, val_button=self.name)
                
            #Inserting the contact in the database
            self.add_contactF()

            #Change the focus
            self.windTwo.focus()
            
        else:
            self.invalid_entryF()


    #Function to Edit Done Button
    def done_editF(self):
        #Extract the data and validate the data
        self.name = self.CName.get()
        self.email = self.validate_emailF(self.CEmail.get())
        self.phone = self.validate_phoneF(self.CPhone.get())
        
        #Validate the entrys
        if self.phone != False and self.email != False:
            if self.name.isspace() or self.name == '':
                self.name = 'Unnamed'

            #Control widgets
            self.control_widgets('active_search', 'del_search', 'forget_add_stage', 'place_select_stage', 'edit_active')

            #Inserting the name in the contact list
            self.my_ctclist_old = []
            self.my_ctclist = []

            #Sending the data to show the contact
            self.show_infoF(0, val_button=self.name)
            
            #Inserting the contact in the database
            self.edit_contactF()

            #Change the focus
            self.windTwo.focus()

        else:
            self.invalid_entryF()

    
    #Function to show the information of the selected contact
    def show_infoF(self, key, val_button=None, val_list=None):
        #Verifiy method
        if val_button != None:
            #Control widgets
            self.control_widgets('forget_add_stage', 'del_entry', 'place_edit_stage') 

            #Adding the information
            self.control_widgets('insert_data_entrys',
            na=val_button,
            em=self.email,
            ph=self.phone)

            self.control_widgets('disable_entrys')

            #Change the focus and the name
            self.windTwo.focus()
            
            #Label name
            self.label_btns_text = 'Contact Information'
            self.control_widgets('refresh_label')
        
        elif val_list == True:
            #Request the data
            self.list_info = self.getctc_info(self.convert_thingsF())

            #Validation blank tuple
            if self.list_info != False:
                #Control widget
                self.control_widgets('place_entrys', 'configure_entrys',
                'place_edit_stage', 'del_entry')

                #Adding the data
                self.control_widgets('insert_data_entrys',
                na=self.list_info[0],
                em=self.list_info[1],
                ph=self.list_info[2])
                
                self.control_widgets('disable_entrys')

                #Change the focus
                #self.windTwo.focus()

                #Label name
                self.label_btns_text = 'Contact Information'
                self.control_widgets('refresh_label')

            else:
                pass
            
            
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

        if phone == True and phone_second == 'Number Phone':
            self.CPhone.delete(0, END)

    
    #Function to validate the state of the button and the entry "Name"
    def validate_stageF(self, key, add=None, edit=None):
        #Get the information
        name = self.CName.get()
        email = self.CEmail.get()
        phone = self.CPhone.get()
    
        #Validate the blank in add stage
        if add == True:            
            while name != '':
                self.control_widgets('color_done_btn')
                break
            else:
                self.control_widgets('reset_done_btn')
        
        #Validate the blank in edit stage
        if edit == True:
            while name or phone or email != '':
                self.control_widgets('color_done_btn')
                break
            else:
                self.control_widgets('reset_done_btn')
                

    #Function to validate the phone number entry
    def validate_phoneF(self, new_phone=''):
        
        if new_phone != '' and new_phone != 'Number Phone' and new_phone != 'No Number Phone Added':
            #Try because phonenumbers dont return false?
            try:
                phone_string = phonenumbers.parse(new_phone)
                phone = phonenumbers.is_possible_number(phone_string)
                
                #Validation always true
                if phone:
                    return new_phone

                else:
                    return False
                
            except Exception as ex:
                return False

        return 'No Number Phone Added'


    #Function to validate the email entry
    def validate_emailF(self, new_email=''):
        if new_email != '' and new_email != 'Email' and new_email != 'No Email Added':
            valid_email = validate_email(new_email)

            if valid_email:
                return new_email

            else:
                return False
            
        return 'No Email Added'


    #Function to add things between two '', get the anchor from lst and the id
    def convert_thingsF(self, name=None):

        if name != None:
            #Inserting the old name between 'name' with aitsuki help 
            aitsuki = "'"
            nakuru = "'"
            self.request_name = aitsuki + name + nakuru
            return self.request_name
           
        else:
            #Convert the lst into a string with aitsuki help
            lst = self.listctc_widget.get(ANCHOR)
            lst_join = "".join(lst)
            nakuru = "'"
            aitsuki = "'"
            self.request_name = aitsuki + lst_join + nakuru
            
            #Select one id from que list
            tuple_id = self.listctc_widget.curselection()
            if tuple_id != ():
                id = tuple_id[0]
                self.select_id = self.list_id[id]
                return self.request_name, self.select_id
            else:
                return False


    #Function to destroy windows
    def destroy_windowsF(self, event=None):
        if event == 'delete_wind':
            self.my_ctclist_old = []
            self.my_ctclist = []
            self.getctc_list()

            self.show_infoF(0, val_button=self.CName.get())
            
            #Control widget
            self.control_widgets('active_all_btn')

        if event == 'invalid_wind':
            self.control_widgets('active_all_btn')
            
        return


    #Function to control the widgets
    def control_widgets(self, *args, na=None, em=None, ph=None):
        for value in args:
            
            """Places Stages"""

            #Select Stage
            if value == 'place_select_stage':
                #Add the buttons "Add", "Settings" and "Select"
                self.add_btn.place(x=50, y=22, anchor=E)
                self.sel_btn.place(x=260, y=22, anchor=E)
                self.settings_btn.place(x=210, y=22, anchor=E)

            #Add Stage
            if value == 'place_add_stage':
                #Add the buttons "Cancel" and "Done"
                self.cancel_btn.place(x=100, y=22, anchor=E)
                self.done_btn.place(x=480, y=22, anchor=E)

            #Edit Stage
            if value == 'place_edit_stage':
                #Adding the button to edit
                self.delete_btn.place(x=480, y=22, anchor=E)
                self.edit_btn.place(x=100, y=22, anchor=E)


            """Forget Stages"""

            #Select Stage
            if value == 'forget_select_stage':
                #Remove the buttons in the main 
                self.add_btn.place_forget()
                self.sel_btn.place_forget()
                self.settings_btn.place_forget()

            #Add Stage
            if value == 'forget_add_stage':
                #Remove the buttons in the add stage or edit
                self.cancel_btn.place_forget()
                self.done_btn.place_forget()

            #Edit Stage
            if value == 'forget_edit_stage':
                #Removing the edit button
                self.edit_btn.place_forget()
                self.delete_btn.place_forget()


            """Buttons"""
            
            #Done Button Command Add Stage
            if value == 'done_add_btn':
                #Configure the button to call the function button done in add stage
                self.done_btn.configure(command=self.done_addF)

            #Done Button Command Edit Stage
            if value == 'done_edit_btn':
                #Configure the button to call the function button edit in edit stage
                self.done_btn.configure(command=self.done_editF)

            #Done Button Disable
            if value == 'reset_done_btn':
                self.done_btn.configure(state='disabled', bg='#161616', disabledforeground='white')

            #Done Button Colors
            if value == 'color_done_btn':
                #configuration while mouse is over the button
                self.done_btn.configure(state='normal', bg='#1924FF', fg='black')

                #configuration while mouse is not over the button
                self.done_btn.configure(activebackground='#363FFF', activeforeground='white')

            #Disable All Buttons
            if value == 'disable_all_btn':
                self.delete_btn.configure(state='disabled')
                self.edit_btn.configure(state='disabled')
                self.add_btn.configure(state='disabled')
                self.done_btn.configure(state='disabled')
                self.cancel_btn.configure(state='disabled')

            #Active All Buttons
            if value == 'active_all_btn':
                self.delete_btn.configure(state='normal')
                self.edit_btn.configure(state='normal')
                self.add_btn.configure(state='normal')
                self.done_btn.configure(state='normal')
                self.cancel_btn.configure(state='normal')


            """Search"""
            #Active Search
            if value == 'active_search':
                #Active the search
                self.searchbar_widget.configure(state='normal')
                self.listctc_widget.configure(state='normal')

            #Del Search
            if value == 'del_search':
                #Delete search bar text
                self.searchbar_widget.configure(state='normal')
                self.searchbar_widget.delete(0, END)

            #Disable Search
            if value == 'disable_search':
                #Disable the search
                self.searchbar_widget.configure(state='disabled', readonlybackground='#1F1F1F')
                self.listctc_widget.configure(state='disabled')
            
            if value == 'refresh_label':
                self.label_btns.configure(text=self.label_btns_text)

            """Entrys"""

            #Place Entrys
            if value == 'place_entrys':
                #Add the entrys
                self.CName.place(x=250, y=150, anchor=CENTER)
                self.CEmail.place(x=250, y=270, anchor=CENTER)
                self.CPhone.place(x=250, y=390, anchor=CENTER)

            #Configure Entrys
            if value == 'configure_entrys':
                #Configure entrys
                self.CName.configure(state='normal', width=25, font=('Arial', 15), fg='black')
                self.CEmail.configure(state='normal', width=25, font=('Arial', 15), fg='black')
                self.CPhone.configure(state='normal', width=25, font=('Arial', 15), fg='black')
            
            #Reset Entrys
            if value == 'reset_entrys':
                #Reset entrys
                self.CName.configure(state='normal', width=25, font=('Arial', 15), fg='white')
                self.CEmail.configure(state='normal', width=25, font=('Arial', 15), fg='white')
                self.CPhone.configure(state='normal', width=25, font=('Arial', 15), fg='white')

            #Disable Entrys
            if value == 'disable_entrys':
                #Disabled entrys
                self.CName.configure(state='readonly')
                self.CEmail.configure(state='readonly')
                self.CPhone.configure(state='readonly')
            
            #Insert Data Entrys
            if value == 'insert_data_entrys':
                #Delete the entrys
                self.CName.delete(0, END)
                self.CEmail.delete(0, END)
                self.CPhone.delete(0, END)

                #Insert the data in the entry
                self.CName.insert(0, na)
                self.CEmail.insert(0, em)
                self.CPhone.insert(0, ph)

            #Del Entrys
            if value == 'del_entry':
                #Delete the entrys
                self.CName.configure(state='normal')
                self.CEmail.configure(state='normal')
                self.CPhone.configure(state='normal')
                self.CName.delete(0, END)
                self.CEmail.delete(0, END)
                self.CPhone.delete(0, END)
            
            #Insert placeholder
            if value == 'insert_placeholder':
                #Delete the entrys
                self.CName.delete(0, END)
                self.CEmail.delete(0, END)
                self.CPhone.delete(0, END)

                #Insert in the entry
                self.CName.insert(0, 'Full Name')
                self.CEmail.insert(0, 'Email')
                self.CPhone.insert(0, 'Number Phone')

            #Forget Entrys
            if value == 'forget_entrys':
                #Remove the entrys
                self.CName.place_forget()
                self.CEmail.place_forget()
                self.CPhone.place_forget()
            

            """Validations"""
            
            #Placeholder Validation
            if value == 'placeholder':
                #Deleting the placeholder
                self.CName.bind("<FocusIn>", lambda m="": self.placeholderF(0, name=True))
                self.CEmail.bind("<FocusIn>", lambda m="": self.placeholderF(0, email=True))
                self.CPhone.bind("<FocusIn>", lambda m="": self.placeholderF(0, phone=True))
            
            #Done Button Add Stage Validation
            if value == 'validate_add_stage':
                #Validating blank
                self.CName.bind("<KeyRelease>", lambda m="": self.validate_stageF(0, add=True))
            
            #Done Button Edit Stage Validation
            if value == 'validate_edit_stage':
                #Validating edit stage
                self.CName.bind("<KeyRelease>", lambda m="": self.validate_stageF(0, edit=True))
                self.CEmail.bind("<KeyRelease>", lambda m="": self.validate_stageF(0, edit=True))
                self.CPhone.bind("<KeyRelease>", lambda m="": self.validate_stageF(0, edit=True))
            

            """Window"""

            #Create Window
            if value == 'create_wind':
                self.wind = Tk()
                self.wind.title(self.title_wind)
                self.wind.geometry("500x200+700+700")
                self.wind.resizable(False, False)
                self.wind.configure(bg='#1F1F1F')

            #Fill Window
            if value == 'fill_wind':
                #Label
                confirm_lbl = Label(self.wind, text=self.label_wind, width=40, height=2)
                confirm_lbl.configure( background='#1F1F1F', relief=SOLID, borderwidth=2, fg='white')
                confirm_lbl.place(x=250, y=25, anchor=CENTER)

                for value in args:
                    #Fill Invalid Window
                    if value == 'fill_invalid':
                        #Button
                        confirm_btnF = Button(self.wind, text='Ok', width=1, height=1)
                        confirm_btnF.configure(command=lambda m="": self.control_widgets('active_all_btn', 'destroy_wind'))
                        #confirm_lbl.configure(background='#1F1F1F', relief=SOLID, borderwidth=2, fg='white')
                        confirm_btnF.place(x=250, y=120, anchor=CENTER)

                    #Fill Delete Window
                    if value == 'fill_delete':
                        #Buttons
                        confirm_btnF = Button(self.wind, text='Yes', width=1, height=1)
                        confirm_btnF.configure(command=lambda m="": self.delete_contactF(Yes=True))
                        #confirm_lbl.configure(background='#1F1F1F', relief=SOLID, borderwidth=2, fg='white')
                        confirm_btnF.place(x=150, y=120, anchor=CENTER)

                        confirm_btnS = Button(self.wind, text='No',width=1, height=1)
                        confirm_btnS.configure(command=lambda m="": self.delete_contactF(No=True))
                        #confirm_lbl.configure(background='#1F1F1F', relief=SOLID, borderwidth=2, fg='white')
                        confirm_btnS.place(x=350, y=120, anchor=CENTER)

            #Destroy Window   
            if value == 'destroy_wind':
                self.wind.destroy()

    #SQLITE FUNCTIONS

    #Function to connect the basedata
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
    

    #Function to get the contacts from database
    def getctc_list(self):
        #Quering the data
        query = 'SELECT name, id FROM contacts ORDER BY name DESC'
        db_rows = self.run_query(query)
        
        #Filling the list
        for rows in db_rows:
            self.my_ctclist_old = ''.join(rows[0])
            self.list_old_id = str(rows[1])
            self.list_id.insert(0, self.list_old_id)
            self.my_ctclist.append(self.my_ctclist_old)
            self.update_listboxF(self.my_ctclist)
            
    
    #Function to get the last id from the database
    def get_last_id(self):
        #Quering the data
        query = 'SELECT MAX(id) AS LastID FROM contacts'
        db_rows = self.run_query(query)

        #Save the id
        for rows in db_rows:
            self.select_id = ''.join(str(rows[0]))


    #Function to get the data from database with name
    def getctc_info(self, request = []):
        #Validation blank tuple
        if request != False:
            #Quering the data
            query = f"SELECT name, email, phone FROM contacts WHERE id LIKE {request[1]} AND name LIKE {request[0]}"
            db_rows = self.run_query(query)
            for rows in db_rows:
                name = rows[0]
                email = rows[1]
                phone = rows[2]
            return name, email, phone
        else:
            return False


    #Function to insert contact in the database
    def add_contactF(self):
        #Queriny the data
        query = 'INSERT INTO contacts VALUES(NULL, ?, ?, ?)'
        parameters = (self.name, self.email, self.phone)
        self.run_query(query, parameters)

        #Get the last id
        self.get_last_id()

        #Update the contact list
        self.getctc_list()
    

    #Function to edit the contact in database
    def edit_contactF(self):
        #Quering the data
        query = f'UPDATE contacts SET name = ?, email = ?, phone = ? WHERE name = {self.request_name} and id = {self.select_id}'
        parameters = (self.name, self.email, self.phone)
        self.run_query(query, parameters)

        #Update the contact list
        self.getctc_list()


    #Function to delete the contact in the database
    def delete_contactF(self, Yes=None, No=None):
        
        if Yes == True:
            #Quering the data
            query = f'DELETE FROM contacts WHERE name = {self.convert_thingsF(name=self.CName.get())} AND id = {self.select_id}'
            self.run_query(query)
            self.my_ctclist_old = []
            self.my_ctclist = []
            self.getctc_list()

            #Control widget
            self.control_widgets('destroy_wind', 'forget_entrys', 'place_select_stage', 'forget_add_stage',
            'forget_edit_stage', 'reset_done_btn', 'active_all_btn')
        
        if No == True:
            self.my_ctclist_old = []
            self.my_ctclist = []
            self.getctc_list()

            self.show_infoF(0, val_button=self.CName.get())
            
            #Control widget
            self.control_widgets('destroy_wind', 'active_all_btn')

        

if __name__ == '__main__':
    PryWind = Tk()
    application = Product(PryWind)
    PryWind.mainloop()