import requests
import json
from datetime import timezone, datetime

def check_site_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN ({response.status_code})"
    except requests.RequestException as e:
        return f"ERROR ({str(e)})"

if __name__ == "__main__":
    # url = "https://www.google.com/"
    url = "https://httpstat.us/503"
    status = check_site_status(url)
    timestamp = datetime.now(timezone.utc).isoformat()

    # result = {
    #     "url": "https://www.google.com/",
    #     "status": status,
    #     "timestamp": timestamp
    # }

    result = {
        "url": "https://httpstat.us/503",
        "status": "DOWN (503)",
        "timestamp": "..."
        }

    print("Health check result:", result)

    with open("status.json", "w") as f:
        json.dump(result, f, indent=2)