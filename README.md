![Python](https://img.shields.io/badge/python-3.11-blue)

# Docker DDNS Updater

This is a lightweight Dockerized Python service that checks your machine's public IP address at regular intervals and sends a notification when it changes.

## 🔧 How It Works

The script:
1. Fetches the current public IP address using `ipinfo.io`
2. Compares it to the last known IP
3. If it changed, it sends a GET request to a templated URL with `{IP}` replaced by the current IP

## 🐳 Docker Usage
### Run the image
```bash
docker run -d --name ddns-updater \
           -e NOTIFY_URL="https://your.webhook.url/?ip={IP}" \
           -e CHECK_INTERVAL_SECONDS=300 \
           ghcr.io/astrophil583/dockerddnsupdater:latest
```
#### ENV Variables
|Name|Description|
|----|----|
|`NOTIFY_URL`|The url for the POST request (you can use the {ip} tag for the IP)|
|`CHECK_INTERVAL_SECONDS`|The time between two consecutive checks|

### Build the image locally

```bash
docker build -t dockerddnsupdater:latest .