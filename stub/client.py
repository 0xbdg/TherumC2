import requests
import json
from time import sleep

# URL of the Flask API
url = 'http://localhost:8000/send_command'

headers = {
    'Content-Type': 'application/json',
}

while True:
    response = requests.get(url ,headers=headers, params={"bot_id":"12923233232"})

    if response.json().get('command') == None:
        continue
    else:
        print(response.json().get('command'))

    sleep(2)