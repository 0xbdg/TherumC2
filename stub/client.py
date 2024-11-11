import requests
import json
from time import sleep

# URL of the Flask API
url = 'http://localhost:8000/api/bot/38273827838273'

headers = {
    'Content-Type': 'application/json',
}
# Send POST request with Content-Type application/json
response = requests.get(url ,headers=headers)

# Check if the request was successful (status code 201 means success)

if response.status_code == 200:
    # Read and parse the response JSON data
        response_data = response.json()
        print(f"ID: {response_data['id']}")
        print(f"Name: {response_data['command']}")
else:
        print(f"Response: {response.text}")
