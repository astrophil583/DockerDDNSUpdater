FROM python:3.11-slim

WORKDIR /app

COPY check_ip.py .

RUN pip install requests

ENV NOTIFY_URL=""
ENV CHECK_INTERVAL_SECONDS=300
ENV PYTHONUNBUFFERED=1

CMD ["python", "check_ip.py"]