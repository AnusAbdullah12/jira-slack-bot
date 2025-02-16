from dotenv import load_dotenv
import os

load_dotenv()

_slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
_jira_user_email = os.getenv("JIRA_USER_EMAIL")
_jira_api_token = os.getenv("JIRA_API_TOKEN")
_jira_api_server = os.getenv("JIRA_API_SERVER")
_jira_project_key = os.getenv("JIRA_PROJECT_KEY")
_slack_server = os.getenv("SLACK_SERVER")
_confluence_api_url = os.getenv("CONFLUENCE_API_URL")
_confluence_user = os.getenv("CONFLUENCE_USER")
_confluence_api_token = os.getenv("CONFLUENCE_API_TOKEN")
_confluence_space_key = os.getenv("CONFLUENCE_SPACE_KEY")
_jira_api_url = os.getenv("JIRA_API_URL")


class EnvironmentSettings:
    @staticmethod
    def get_slack_bot_token():
        return _slack_bot_token

    @staticmethod
    def get_jira_api_token():
        return _jira_api_token

    @staticmethod
    def get_jira_api_server():
        return _jira_api_server

    @staticmethod
    def get_jira_user_email():
        return _jira_user_email

    @staticmethod
    def get_jira_project_key():
        return _jira_project_key

    @staticmethod
    def get_slack_server():
        return _slack_server

    @staticmethod
    def get_confluence_api_url():
        """Returns the Confluence API URL."""
        return _confluence_api_url

    @staticmethod
    def get_confluence_user():
        """Returns the Confluence username/email."""
        return _confluence_user

    @staticmethod
    def get_confluence_api_token():
        """Returns the Confluence API token."""
        return _confluence_api_token

    @staticmethod
    def get_confluence_space_key():
        """Returns the Confluence space key."""
        return _confluence_space_key
    
    @staticmethod
    def get_jira_api_url():
        return _jira_api_url