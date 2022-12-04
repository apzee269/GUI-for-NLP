from tkinter import *
from mydb import Database
from tkinter import messagebox #to show the msg to user
from myapi import API

class NLPApp:

    def __init__(self):

        #create db object
        self.dbo = Database()
        self.apio = API()

        # Load gui of login
        self.root = Tk() #self.root is a variable where we are saving Tk class
        self.root.title("nlpApp")
        #self.root.iconbitmap("resources/favicon.ico") #to add icon on top left of gui
        self.root.geometry('350x600') #select the width and height of gui at opening
        self.root.configure(bg = '#057F85') #set the background colour

        self.login_gui()

        self.root.mainloop()  # it holds the GUI on screen, if it is not used, GUI will be removed

    def login_gui(self):
        self.clear_gui()

        heading = Label(self.root,text = "NLPApp", bg = '#057F85', fg = 'white')
        heading.pack(pady = (30,30)) #to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana',24,'bold')) #change the font style

        label1 = Label(self.root,text = "Enter Email",bg = '#057F85',fg = 'white')
        label1.pack(pady = (10,10))
        self.email_input = Entry(self.root, width = 50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password", bg='#057F85',fg = 'white')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50, show = "*")
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root,text = "Login", command=self.perform_login)
        login_btn.pack(pady = (10,10))

        label3 = Label(self.root, text="Not A member?", bg='#057F85',fg = 'white')
        label3.pack(pady=(10, 10))
        redirect_btn = Button(self.root, text="Register Here", command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear_gui()

        heading = Label(self.root, text="NLPApp", bg='#057F85', fg='white')
        heading.pack(pady=(30, 30))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 24, 'bold'))  # change the font style

        label0 = Label(self.root, text="Enter Name", bg='#057F85',fg = 'white')
        label0.pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email", bg='#057F85',fg = 'white')
        label1.pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password", bg='#057F85', fg = 'white')
        label2.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50, show = '*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already a member?", bg='#057F85', fg = 'white')
        label3.pack(pady=(10, 10))
        redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def home_gui(self):
        self.clear_gui()

        heading = Label(self.root, text="NLPApp", bg='#057F85', fg='white')
        heading.pack(pady=(30, 30))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 24, 'bold'))  # change the font style

        label = Label(self.root, text = "What would you like to perform?", bg = '#057F85',fg = 'white')
        label.pack(pady=(10,10))

        sentiment_analysis_btn = Button(self.root, text="Sentiment Analysis",width=40, height = 4,command=self.sentiment_gui)
        sentiment_analysis_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text="Named Entity Recognition Button",height=4,width=40, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="Emotion Analysis",height=4,width=40, command=self.emotional_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear_gui()

        heading = Label(self.root, text="NLPApp", bg='#057F85', fg='white')
        heading.pack(pady=(10, 20))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 24, 'bold'))  # change the font style

        heading = Label(self.root, text="Sentiment Analysis", bg='#057F85', fg='white')
        heading.pack(pady=(20, 20))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 16, 'bold'))  # change the font style

        label1 = Label(self.root,text = "Enter the text")
        label1.pack(pady = (20,20))

        self.sentiment_input = Entry(self.root,width = 40)
        self.sentiment_input.pack(pady= (20,20))

        analyse_button = Button(self.root,text = "Analyse Sentiment",width = 30, command=self.do_sentiment_analysis)
        analyse_button.pack(pady=(20,20))

        self.sentiment_result = Label(self.root, text="", bg='#057F85')
        self.sentiment_result.pack(pady=(20, 20))

        restart_button = Button(self.root, text="Want to try again?", command=self.sentiment_gui)
        restart_button.pack(pady=(10, 10))

        go_back_button = Button(self.root, text="Go Back", command=self.home_gui)
        go_back_button.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ""
        for i in result['sentiment']:
            txt = txt + i + " --> " + str(result['sentiment'][i]) + "\n"

        self.sentiment_result['text'] = txt

    def ner_gui(self):
        self.clear_gui()

        heading = Label(self.root, text="NLPApp", bg='#057F85', fg='white')
        heading.pack(pady=(10, 20))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 24, 'bold'))  # change the font style

        heading = Label(self.root, text="Named Entity Recognition", bg='#057F85', fg='white')
        heading.pack(pady=(20, 20))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 16, 'bold'))  # change the font style

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(20, 20))

        self.ner_input = Entry(self.root, width=40)
        self.ner_input.pack(pady=(20, 20))

        analyse_button = Button(self.root, text="Analyse Sentiment", width = 30, command=self.do_ner)
        analyse_button.pack(pady=(20, 20))

        self.ner_result = Label(self.root, text="", bg='#057F85')
        self.ner_result.pack(pady=(20, 20))

        restart_button = Button(self.root, text="Want to try again?", command=self.ner_gui)
        restart_button.pack(pady=(10, 10))
        go_back_button = Button(self.root, text="Go Back", command=self.home_gui)
        go_back_button.pack(pady=(20, 20))

    def do_ner(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)

        txt = ""
        for i in result['entities']:
            txt = txt + str(i['category']).capitalize() + ": " + i['name'] + "\n"
        self.ner_result['text'] = txt
            #print(i['category'].capitalize(), " ", i['name'])

    def emotional_gui(self):
        self.clear_gui()

        heading = Label(self.root, text="NLPApp", bg='#057F85', fg='white')
        heading.pack(pady=(10, 20))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 24, 'bold'))  # change the font style

        heading = Label(self.root, text="Emotional Analysis", bg='#057F85', fg='white')
        heading.pack(pady=(20, 20))  # to display the text, pady is used to change the orientation or position
        heading.configure(font=('verdana', 16, 'bold'))  # change the font style

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(5, 5))

        self.emotional_input = Entry(self.root, width=40)
        self.emotional_input.pack(pady=(10, 10))

        analyse_button = Button(self.root, text="Analyse Sentiment",  width = 30, command=self.do_emotional_analysis)
        analyse_button.pack(pady=(10, 10))

        self.emotional_result = Label(self.root, text="", bg='#057F85')
        self.emotional_result.pack(pady=(10, 10))

        display_full_result_button = Button(self.root, text="See Sentiment Analysis", width = 30, command=self.do_emotional_analysis_full)
        display_full_result_button.pack(pady=(5, 5))

        self.emotional_result_full = Label(self.root, text="", bg='#057F85')
        self.emotional_result_full.pack(pady=(5, 5))

        restart_button = Button(self.root, text="Want to try again?", command=self.emotional_gui)
        restart_button.pack(pady=(5, 5))
        go_back_button = Button(self.root, text="Go Back", command=self.home_gui)
        go_back_button.pack(pady=(5, 5))

    def do_emotional_analysis(self):
        text = self.emotional_input.get()
        result = self.apio.emotion_prediction(text)
        txt = {}
        for i in result['emotion']:
            temp = {i: str(result['emotion'][i])}
            txt.update(temp)
        Keymax = max(zip(txt.values(), txt.keys()))[1]
        self.emotional_result['text'] = Keymax

    def do_emotional_analysis_full(self):
        text = self.emotional_input.get()
        result = self.apio.emotion_prediction(text)
        txt = ""
        for i in result['emotion']:
            txt = txt + i + " --> " + str(result['emotion'][i]) + "\n"

        self.emotional_result_full['text'] = txt

    def clear_gui(self):
        # clear the existing gui
        for i in self.root.pack_slaves():  # it prints all the elements in our gui
            # print(i)
            i.destroy() # all elements are removed from gui

    def perform_registration(self):
        # fetch data from gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration Succesfull, you can login now')
            self.login_gui()
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo("Success", "Logged in successfully")
            self.home_gui()
        else:
            messagebox.showerror("Error", "Email/Password Incorrect")

nlp = NLPApp()