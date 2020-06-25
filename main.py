import os
import tkinter
import tkcalendar
from jira import JIRA
from guizero import (App, PushButton, Picture, TextBox, 
                     Slider, Window, Text, Combo)

from helpers import info_text_message, address


def create_connection(address, credentials):
    """
    creates connection to JIRA
    Args:
        address (str): jira server address
        credentials (tuple): strings -> login, password 
    Returns:
        [type]: JIRA interface object
    """
    return JIRA(server=address, 
                basic_auth=credentials)

def add_worklog(jira_connection, issue, hours, date, commentary):
    """
    adds worklog to specified issue with hours, date and commentary arguments
    Args:
        jira_connection (JIRA): JIRA interface object
        issue (str): issue code
        hours (str): how many hours to log
        date (datetime): date to log
        commentary (str): commentary to log
    """
    jira_connection.add_worklog(issue=issue, 
                                timeSpent=hours, 
                                comment=commentary, 
                                started=date)

def send(login, password, hours, issue, date, commentary=""):
    """
    TODO: one object one responsibility!
    TODO: random commentary from list if empty
    """
    jira_connection = create_connection(address=address, 
                                        credentials=(login, password))
    add_worklog(jira_connection, issue, hours, date, commentary)
    summary(app, hours, issue, date)

def get_login_from_filename():
    text_files = [file for file in os.listdir(".") if file.endswith(".txt")]
    assert len(text_files) == 1, f"<login>.txt file not found or too many .txt files"
    return text_files[0].split(".")[0]

def get_issues_from_file():
    path = get_login_from_filename()
    with open("{}.txt".format(path), "r") as file:
        lines = file.read().splitlines()
    return lines

def summary(app, hours, issue, date):
    summary = Text(app, text="{} sent to {}, date: {}".format(hours, issue, date), grid=[0, 12])
    summary.text_size = 8
    summary.text_color = "#034DA4"
    
def info():
    window = Window(app, width=250, height=180, title="how to use")
    instruction = Text(window,
                       text=info_text_message,
                       align="left"
                       )
    instruction.text_size = 8

if __name__ == '__main__':
    issues = get_issues_from_file()
    username = get_login_from_filename()
    app = App(title="JIRA log work", width=460, height=400, bg="white", layout="grid")
    app.text_color = "black"
    input_password = tkinter.Entry(show="*", width=20)
    calendar = tkcalendar.Calendar(background="#034DA4", selectbackground="#034DA4")
    calendar_widget = app.add_tk_widget(calendar, grid=[0, 1, 1, 8])
    input_login = TextBox(app, username, width=20, grid=[1, 1])
    password_widget = app.add_tk_widget(input_password, grid=[1, 2])
    issues = Combo(app, options=issues, grid=[1, 9])
    slider = Slider(app, start=1, end=8, grid=[1, 4])
    comment = TextBox(app, "<comment>", width=30, height=4, grid=[0, 10], multiline=True)
    comment.text_size = 8
    ok = PushButton(app, 
                    text="SEND", 
                    command=send, 
                    args=(input_login.value, input_password.get(), 
                          "{}h".format(slider.value), issues.value.split()[0],
                          calendar.selection_get(), comment.value), 
                    grid=[1, 10], 
                    align="right")
    ok.bg = "#034DA4"
    ok.text_color = "white"
    how_to = PushButton(app, text="How to?", command=info, grid=[1, 10], align="left")
    how_to.bg = "#E7E7E9"
    info.text_size = 6
    info.text_color = "grey"
    app.display()


