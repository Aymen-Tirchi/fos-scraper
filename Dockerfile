FROM python:3.7-alpine

COPY scraper.py /app/
COPY requirements.txt /app/

WORKDIR /app

RUN apk add --no-cache busybox-suid # Install cron
RUN pip install -r requirements.txt

RUN echo "*/10 * * * * python /app/scraper.py >> /app/cron.log 2>&1" > /etc/crontabs/root && \
    chmod 0644 /etc/crontabs/root && \
    touch /app/cron.log

CMD crond -f && tail -f /app/cron.log
