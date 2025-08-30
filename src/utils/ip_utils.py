import requests

def get_user_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        ip = response.json().get("ip")
        return ip
    except Exception:
        return None
