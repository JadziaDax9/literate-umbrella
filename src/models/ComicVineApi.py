import requests

class ComicVineAPI:
    def __init__(self, api_key, user_agent):
        self.api_key = api_key
        self.user_agent = user_agent

    def get_issue(self, issue_id):
        url = f"https://comicvine.gamespot.com/api/issue/{issue_id}/"
        params = {
            "api_key": self.api_key,
            "format": "json"
        }
        headers = {
            "User-Agent": self.user_agent
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        return data

# Usage example
api_key = "xxxxxx"  # Replace with your Comic Vine API key
user_agent = "PaulBlartMallcop"  # Replace with your desired user agent

# Instantiate the ComicVineAPI object
comic_vine_api = ComicVineAPI(api_key, user_agent)

# Specify the issue ID
issue_id = "4000-146961"  # Replace with the desired issue ID

# Get the issue data
issue_data = comic_vine_api.get_issue(issue_id)

# Print the issue data
print(issue_data['results'].keys())

# For each key in results, print the key and the value
for key in issue_data['results']: 
    print(key, issue_data['results'][key])




