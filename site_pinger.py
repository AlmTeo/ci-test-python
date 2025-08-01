import requests

def check_site_status(url="https://www.google.com/"):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN ({response.status_code})"
    except requests.RequestException as e:
        return f"ERROR ({str(e)})"

if __name__ == "__main__":
    result = check_site_status()
    print(f"Health Check Result: {result}")