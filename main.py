from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from pprint import pprint
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


header = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding" : "gzip, deflate",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection" : "keep-alive",
    # "Host" : "myhttpheader.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

response = requests.get(url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22:%7B%7D,%22usersSearchTerm%22:null,%22mapBounds%22:%7B%22west%22:-122.56276167822266,%22east%22:-122.30389632177734,%22south%22:37.69261345230467,%22north%22:37.857877098316834%7D,%22isMapVisible%22:true,%22filterState%22:%7B%22fr%22:%7B%22value%22:true%7D,%22fsba%22:%7B%22value%22:false%7D,%22fsbo%22:%7B%22value%22:false%7D,%22nc%22:%7B%22value%22:false%7D,%22cmsn%22:%7B%22value%22:false%7D,%22auc%22:%7B%22value%22:false%7D,%22fore%22:%7B%22value%22:false%7D,%22pmf%22:%7B%22value%22:false%7D,%22pf%22:%7B%22value%22:false%7D,%22mp%22:%7B%22max%22:3000%7D,%22price%22:%7B%22max%22:872627%7D,%22beds%22:%7B%22min%22:1%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12%7D", headers = header)

webpage = response.content



soup = BeautifulSoup(webpage, "html.parser")
# print(soup)

link_tags = soup.select(selector = ".list-card-top a")
links = []
for link_tag in link_tags:
    if "http" not in link_tag.get('href'):
        links.append("https://zillow.com" + link_tag.get('href'))
    else:
        links.append(link_tag.get('href'))

price_tags = soup.find_all(class_ = "list-card-price")
prices = []
for price_tag in price_tags:
    prices.append(price_tag.get_text())

address_tags = soup.find_all(class_ = "list-card-addr")
addresses = []
for address_tag in address_tags:
    addresses.append(address_tag.get_text())

PATH = "C:/Users/Saniya Maheshwari/OneDrive/Desktop/Development/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(executable_path = PATH)

for n in range(len(links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScvCjMj2R0xs1E1v8WbKtGu31SktUukJuON01yDBbvQRhQUAg/viewform?usp=sf_link")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'quantumWizTextinputPaperinputInput')))
    form = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")

    form[0].send_keys(addresses[n])
    form[1].send_keys(prices[n])
    form[2].send_keys(links[n])

    button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()