import tkinter
import tkcalendar
from guizero import (App, PushButton, Picture, TextBox, 
                     Slider, Combo, Text, Window)
from utilities import (info_text_message, get_login_from_filename, 
                       get_issues_from_file)
from JiraConnector import JiraConnector

WIDTH = 460
HEIGHT = 400

class Application(object):

    def __init__(self):
        self.app = App(title="JIRA log work", 
                       width=WIDTH, height=HEIGHT, 
                       bg="white", layout="grid")
        self.jira = JiraConnector()
        self.username = get_login_from_filename()
        self.issues = get_issues_from_file()
        self.input_login = TextBox(self.app, self.username, 
                                   width=20, grid=[1, 1])
        self.input_password = tkinter.Entry(show="*", 
                                            width=20)
        self.calendar = tkcalendar.Calendar(background="#034DA4", 
                                            selectbackground="#034DA4")
        self.issues = Combo(self.app, options=self.issues, grid=[1, 9])
        self.slider = Slider(self.app, start=1, end=8, 
                        grid=[1, 4])
        self.comment = TextBox(self.app, "<comment>", 
                        width=30, height=4, 
                        grid=[0, 10], 
                        multiline=True)
        self.ok = PushButton(self.app, 
                        text="SEND", 
                        command=self.jira.send, 
                        args=(self.input_login.value, self.input_password.get(), 
                            "{}h".format(self.slider.value), self.issues.value.split()[0],
                            self.calendar.selection_get(), self.comment.value), 
                        grid=[1, 10], 
                        align="right")
        self.how_to = PushButton(self.app, text="How to?", command=self._generate_info, grid=[1, 10], align="left")
        self.configure()
    
    def configure(self):
        self.app.text_color = "black"
        self.app.add_tk_widget(self.input_password, grid=[1, 2])
        self.app.add_tk_widget(self.calendar, grid=[0, 1, 1, 8])
        self.comment.text_size = 8
        self.ok.bg = "#034DA4"
        self.ok.text_color = "white"
        self.how_to.bg = "#E7E7E9"
        self.how_to.text_size = 6
        self.how_to.text_color = "grey"
        
    def display(self):
        self.app.display()
        
    def _generate_summary(self, hours, issue, date):
        summary = Text(self.app, text="{} sent to {}, date: {}".format(hours, issue, date), grid=[0, 12])
        summary.text_size = 8
        summary.text_color = "#034DA4"
        
    def _generate_info(self):
        window = Window(self.app, width=250, height=180, title="how to use")
        instruction = Text(window,
                        text=info_text_message,
                        align="left"
                        )
        instruction.text_size = 8