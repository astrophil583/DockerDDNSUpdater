import requests
import os
import time
import sys

last_ip = ""

def get_notify_url():
    url = os.environ.get("NOTIFY_URL")
    if not url:
        print("ERROR: NOTIFY_URL environment variable not set.")
        sys.exit(1)
    return url

def get_check_interval():
    val = os.environ.get("CHECK_INTERVAL_SECONDS", "300")
    try:
        return int(val)
    except ValueError:
        print(f"ERROR: CHECK_INTERVAL_SECONDS must be an integer, got '{val}'")
        sys.exit(1)

def get_current_ip():
    try:
        return requests.get("https://ipinfo.io/ip").text.strip()
    except Exception as e:
        print(f"ERROR: Could not retrieve current IP: {e}")
        return None

def notify(ip, url_template):
    global last_ip
    url = url_template.replace("{IP}", ip)
    print(f"Notifying {url} with IP {ip}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            last_ip = ip
        print(f"Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to notify: {e}")

def check(url_template):
    current_ip = get_current_ip()
    if current_ip != last_ip:
        notify(current_ip, url_template)


def main():
    url_template = get_notify_url()
    interval = get_check_interval()
    print(f"Starting IP checker. Interval: {interval}s, Notify URL: {url_template}")
    while True:
        check(url_template)
        time.sleep(interval)

if __name__ == "__main__":
    main()