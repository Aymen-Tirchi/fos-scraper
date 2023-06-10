# Web Scraper

This project is a web scraper built using Python. It scrapes data from https://www.ouedkniss.com/automobiles/1 

## Prerequisites

- Python 3.7
- Docker (optional)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Aymen-Tirchi/fos-scraper.git

```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

3. Run the scraper:

```bash
python scraper.py
```

This will start the scraper and create a results.txt that contains the output of scraper.py

## Docker

Alternatively, you can use Docker to run the scraper in a containerized environment:

1. Build the Docker image:

```bash
docker build -t web-scraper .
```

2. Run the Docker container:

```bash
docker run web-scraper
```

This will execute the scraper inside the Docker container.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.
