import time
import uuid
import requests
import platform
import psutil
import os
import subprocess

SERVER_URL = "http://127.0.0.1:5000"
AGENT_ID = str(uuid.uuid1())
USER_AGENT = "Mozilla/5.0 (Linux; Android 8.1.0; Core-X3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36"

headers = {
        "Content-Type": 'application/json',
        "User-Agent": USER_AGENT,
        "Authorization": f"Bearer {AGENT_ID}",
        "X-Session-ID": "12345"
}

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_minutes = uptime_seconds / 60

    return f"{uptime_minutes:.2f}"

def get_task():
    resp = requests.get(SERVER_URL + "/task/"+AGENT_ID, headers=headers)

    if resp.status_code == 200:
        for t in resp.json():
            print(t)

def status(): 
    payload = {"agent_id": AGENT_ID, "hostname":platform.node(),"uptime":get_uptime(), "os":platform.system() }

    try:
        resp = requests.post(SERVER_URL + "/status", json=payload, headers=headers)
        

        if resp.status_code == 200:
            data = resp.json()
            print(data)
    except Exception as err:
        print(err)


def main():
    while 1:
        status()
        get_task()
        print(time.time())
        time.sleep(5)

if "__main__" == __name__:
    main()
