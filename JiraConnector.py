from jira import JIRA
from utilities import get_login_from_filename


class JiraConnector(object):
    
    address = "your jira adress here"
    
    def __init__(self):
        self.login = get_login_from_filename()
        self.connection = None
        
    def connect(self, password):
        """
        create connection to JIRA server with credentials
        Args:
            password (str): password to JIRA account
        """
        credentials = tuple(self.login, password)
        self.connection = JIRA(server=self.address, 
                               basic_auth=credentials)
        
    def add_worklog(self, issue, hours, date, commentary):
        """
        add worklog to specified issue with hours, date and commentary arguments
        Args:
            jira_connection (JIRA): JIRA interface object
            issue (str): issue code
            hours (str): how many hours to log
            date (datetime): date to log
            commentary (str): commentary to log
        """
        assert self.connection, "not connected"
        self.connection.add_worklog(issue=issue, 
                                    timeSpent=hours, 
                                    comment=commentary, 
                                    started=date)

    def send(self, password, hours, issue, date, commentary=""):
        """
        send worklog data to JIRA server
            - connect to server if not connected
            - add worklog
        Args:
            password (str): password to JIRA account
            hours (str): hours to log
            issue (str): issue code to log
            date (datetime): specified day to log
            commentary (str, optional): comment to log. Defaults to "".
        """
        if not self.connection:
            self.connect(password=password)
        self.add_worklog(issue, hours, date, commentary)
