import requests

def get_region(ip):
    resp = requests.get(f"https://ipapi.co/{ip}/json/")

    if resp.status_code == 200:
        try:
            data = resp.json()["country_name"]
            return data
        except:
            return "None"
