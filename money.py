import pandas as pd
import requests # Assuming the API uses HTTP requests

# Replace with the actual API endpoint URL if available
api_url = "https://ncaa-api.henrygd.me/rankings/football/fbs/associated-press"

# Example API parameters (adjust based on API documentation)
params = {
    "sport": "basketball",  # Or other supported sports
    "division": "1",       # Or other divisions
    "year": 2023,
    'month': 12 # Adjust for the desired year
}

response = requests.get(api_url, params=params)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)  # Assuming response is JSON-formatted data
    print(df)
else:
    print("Error:", response.status_code, response.text)