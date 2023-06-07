import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds

url = "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

driver.get(url)

elements = driver.find_elements(By.CSS_SELECTOR, ".primary")

with open("results.txt", "w") as file:
    for elt in elements:
        text = elt.text
        file.write(text + "\n")

driver.quit()
