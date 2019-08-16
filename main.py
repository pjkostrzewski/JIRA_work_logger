from jira import JIRA
from guizero import App, PushButton, Picture, TextBox, Slider, Window, Text, Combo
import tkinter
import tkcalendar
import os

address = "your address of jira"


def send():
    hours = "{}h".format(slider.value)
    login = input_login.value
    password = input_password.get()
    issue = issues.value.split()[0]
    commentary = comment.value
    date = calendar.selection_get()
    jira = JIRA(address, basic_auth=(login, password))
    jira.add_worklog(issue=issue, timeSpent=hours, comment=commentary, started=date)
    summary = Text(app, text="{} sent to {}, date: {}".format(hours, issue, date), grid=[0, 12])
    summary.text_size = 8
    summary.text_color = "#034DA4"


def get_list_from_file():
    path = get_login_from_filename()
    with open("{}.txt".format(path), "r") as file:
        lines = file.read().splitlines()
    return lines


def get_login_from_filename():
    return [file for file in os.listdir(".") if file.endswith(".txt")][0].split(".")[0]


def info():
    window = Window(app, width=250, height=180, title="how to use")
    instruction = Text(window,
                       text="1. Place text file next to .exe file with your login\n "
                            "for example:\n- tnowak.txt\n"
                            "2. In .txt file place issue<space>your_comment\n"
                            "for example: \n- FCA_5GIV-421 My feature\n"
                            "3. Use next line for another one\n"
                            "for example: \n"
                            "- issue1 My first\n"
                            "- issue2 My second\n"
                            "- issue3 My third",
                       align="left"
                       )

    instruction.text_size = 8


if __name__ == '__main__':
    issues_list = get_list_from_file()
    username = get_login_from_filename()
    app = App(title="JIRA log work", width=460, height=400, bg="white", layout="grid")
    app.text_color = "black"
    input_password = tkinter.Entry(show="*", width=20)
    calendar = tkcalendar.Calendar(background="#034DA4", selectbackground="#034DA4")
    calendar_widget = app.add_tk_widget(calendar, grid=[0, 1, 1, 8])
    input_login = TextBox(app, username, width=20, grid=[1, 1])
    password_widget = app.add_tk_widget(input_password, grid=[1, 2])
    issues = Combo(app, options=issues_list, grid=[1, 9])
    slider = Slider(app, start=1, end=8, grid=[1, 4])
    comment = TextBox(app, "<comment>", width=30, height=4, grid=[0, 10], multiline=True)
    comment.text_size = 8
    ok = PushButton(app, text="SEND", command=send, grid=[1, 10], align="right")
    ok.bg = "#034DA4"
    ok.text_color = "white"
    how_to = PushButton(app, text="How to?", command=info, grid=[1, 10], align="left")
    how_to.bg = "#E7E7E9"
    info.text_size = 6
    info.text_color = "grey"
    app.display()


