import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(60)  # seconds

url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

max_retries = 3
retry_count = 0
success = False

while not success and retry_count < max_retries:
    try:
        driver.get(url)
        time.sleep(3)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")

        elements = soup.select(".shelfProductTile-description .shelfProductTile-descriptionContainer")

        with open("results.txt", "w") as file:
            for elt in elements:
                text = elt.get_text(strip=True)
                file.write(text + "\n")

        success = True

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        retry_count += 1
        time.sleep(5)  

if retry_count == max_retries and not success:
    print("Max retries reached. Unable to scrape the data.")

driver.quit()
