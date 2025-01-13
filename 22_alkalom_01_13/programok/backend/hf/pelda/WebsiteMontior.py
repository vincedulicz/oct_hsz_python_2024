import requests
import time
from datetime import datetime


class WebsiteMonitor:
    def __init__(self):
        self.log_file = "monitor.log"

    def check_status(self, url) -> dict:
        try:
            start_time = time.time()
            response = requests.get(url)
            response.raise_for_status()
            elapsed_time = time.time() - start_time
            return {"status_code": response.status_code,
                    "elapsed_time": elapsed_time}
        except requests.RequestException as e:
            return {"error": str(e)}

    def is_online(self, url) -> bool:
        status = self.check_status(url)
        return status.get("status_code") == 200

    def get_headers(self, url) -> dict:
        try:
            response = requests.head(url)
            response.raise_for_status()
            return response.headers
        except requests.RequestException as e:
            return {"error": str(e)}

    def log_status(self, url):
        result = self.check_status(url)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as file:
            file.write(f"{timestamp} - {url} - {result}\n")


if __name__ == "__main__":
    monitor = WebsiteMonitor()
    url = "https://httpbin.org"

    print("Státusz:", monitor.check_status(url))

    print("Online:", monitor.is_online(url))

    print("Fejlécek:", monitor.get_headers(url))

    monitor.log_status(url)

    monitors = WebsiteMonitor()
    urls = ["https://httpbin.org", "https://google.com"]

    for url in urls:
        print("Státusz:", monitor.check_status(url))

        print("Online:", monitor.is_online(url))

        print("Fejlécek:", monitor.get_headers(url))

        monitor.log_status(url)
