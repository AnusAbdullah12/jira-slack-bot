import requests
from requests.auth import HTTPBasicAuth
from config import EnvironmentSettings
CONFLUENCE_API_URL = EnvironmentSettings.get_confluence_api_url().rstrip("/")
CONFLUENCE_USER = EnvironmentSettings.get_confluence_user()
CONFLUENCE_API_TOKEN = EnvironmentSettings.get_confluence_api_token()
CONFLUENCE_SPACE_KEY = EnvironmentSettings.get_confluence_space_key()

def post_to_confluence(content):
    """Posts formatted release notes to Confluence and returns the page URL."""
    url = f"{CONFLUENCE_API_URL}/rest/api/content" # Confluence REST API URL
    auth = HTTPBasicAuth(CONFLUENCE_USER, CONFLUENCE_API_TOKEN)
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    data = {
        "type": "page",
        "title": "Sprint Release Notes",
        "ancestors": [],  # Optional: Set a parent page if needed
        "space": {"key": CONFLUENCE_SPACE_KEY},  # Ensure space key is passed correctly
        "body": {
            "storage": {
                "value": content,
                "representation": "storage"
            }
        }
    }

    response = requests.post(url, auth=auth, headers=headers, json=data)


    # Debugging: Print response
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    try:
        return response.json().get("_links", {}).get("webui", "")
    except requests.exceptions.JSONDecodeError:
        print("Error: Confluence did not return valid JSON.")
        return None
