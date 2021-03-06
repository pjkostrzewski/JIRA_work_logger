import os


info_text_message = "1. Place text file next to .exe file with your login\n "\
                    "for example:\n- tnowak.txt\n"\
                    "2. In .txt file place issue<space>your_comment\n"\
                    "for example: \n- FCA_5GIV-421 My feature\n"\
                    "3. Use next line for another one\n"\
                    "for example: \n"\
                    "- issue1 My first\n"\
                    "- issue2 My second\n"\
                    "- issue3 My third"
 
  
def get_login_from_filename():
    """
    search specified file in directory and get user login from <login>.txt file
    
    username123.txt -> username123
    
    Returns:
        str: login, JIRA username
    """
    text_files = [file for file in os.listdir(".") if file.endswith(".txt")]
    assert len(text_files) == 1, "<login>.txt file not found or too many .txt files | {}".format(text_files)
    return text_files[0].split(".")[0]

  
def get_issues_from_file():
    """
    open and get all issues from user's file

    Returns:
        [list]: all issues in file
    """
    path = get_login_from_filename()
    with open("{}.txt".format(path), "r") as file:
        lines = file.read().splitlines()
    return lines
