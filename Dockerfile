FROM python:3.7-alpine

RUN apk update && \
    apk add --no-cache \
    chromium \
    chromium-chromedriver

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROME_DRIVER=/usr/bin/chromedriver

CMD ["python", "scraper.py"]
