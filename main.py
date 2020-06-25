import os
import tkinter
import tkcalendar
from guizero import (App, PushButton, Picture, TextBox, 
                     Slider, Window, Text, Combo)

from utilities import (info_text_message, get_login_from_filename, 
                       get_issues_from_file)

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


