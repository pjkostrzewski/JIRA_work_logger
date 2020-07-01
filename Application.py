import tkinter
import tkcalendar
from guizero import (App, PushButton, TextBox,
                     Slider, Combo, Text, Window)
from helpers import (info_text_message, get_login_from_filename,
                       get_issues_from_file)
from JiraConnector import JiraConnector


class Application(object):
    """
    class with interface objects, views and buttons configured
    """
    
    WIDTH = 460
    HEIGHT = 400
    
    def __init__(self):
        """
        - create all necessary elements
        - configure them with self.configure() method
        """
        self.app = App(title="JIRA log work", 
                       width=Application.WIDTH, height=Application.HEIGHT, 
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
        self.ok = self._create_send_button()
        self.how_to = PushButton(self.app, text="How to?", command=self._generate_info, grid=[1, 10], align="left")
        self.configure()
    
    def configure(self):
        """
        configure all the objects created in __init__()
        """
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
        """
        display everything after creation and configuration
        """
        self.app.display()

    def send(self):
        """
        get all data from class instance, send and generate summary
        """
        password = self.input_password.get()
        hours = "{}h".format(self.slider.value)
        issue = self.issues.value.split()[0]
        date = self.calendar.selection_get()
        commentary = self.comment.value
        self.jira.send(password, hours, issue, date, commentary)
        self._generate_summary(hours, issue, date)

    def _generate_summary(self, hours, issue, date):
        """
        to generate summary after work logging
        Args:
            hours (str): how many hours logged
            issue (str): which issue logged
            date (str): date logged
        """
        summary = Text(self.app, text="{} sent to {}, date: {}".format(hours, issue, date), grid=[0, 12])
        summary.text_size = 8
        summary.text_color = "#034DA4"
        
    def _generate_info(self):
        """
        generate info view after push "how to?" button
        """
        window = Window(self.app, width=250, height=180, title="how to use")
        instruction = Text(window,
                           text=info_text_message,
                           align="left"
                           )
        instruction.text_size = 8
    
    def _create_send_button(self):
        """
        create send buttoJiraConnectorn in interface
        Returns:
            [type]: PushButton object
        """
        return PushButton(self.app, 
                          text="SEND",
                          command=self.send,
                          grid=[1, 10], 
                          align="right")
