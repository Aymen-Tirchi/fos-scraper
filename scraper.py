from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.ouedkniss.com/automobiles/1'
driver.get(url)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

price_elements = soup.find_all('span', class_='price')

prices = [element.get_text() for element in price_elements]

with open('results.txt', 'w') as file:
    for price in prices:
        file.write(price + '\n')

driver.quit()
