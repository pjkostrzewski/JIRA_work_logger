from guizero import Window, Text
from utilities import info_text_message


def generate_summary(app, hours, issue, date):
    summary = Text(app, text="{} sent to {}, date: {}".format(hours, issue, date), grid=[0, 12])
    summary.text_size = 8
    summary.text_color = "#034DA4"
    
def generate_info(app):
    window = Window(app, width=250, height=180, title="how to use")
    instruction = Text(window,
                       text=info_text_message,
                       align="left"
                       )
    instruction.text_size = 8