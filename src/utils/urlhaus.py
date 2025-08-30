import requests

def check_domain_urlhaus(domain: str):
    """
    Check if any URLs related to the domain are in URLhaus database.
    """
    API_URL = "https://urlhaus-api.abuse.ch/v1/host/"
    try:
        response = requests.post(API_URL, data={"host": domain}, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("query_status") == "ok" and data.get("url_list"):
            return True, data
        else:
            return False, {}
    except Exception:
        return False, {}

def check_url_urlhaus(url: str):
    """
    Check if full URL is in URLhaus database.
    """
    API_URL = "https://urlhaus-api.abuse.ch/v1/url/"
    try:
        response = requests.post(API_URL, data={"url": url}, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("query_status") == "ok" and data.get("url_info"):
            return True, data
        else:
            return False, {}
    except Exception:
        return False, {}
