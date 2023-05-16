import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러메세지 삭제
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#크롬 드라이버 최신 버전
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

'''#해당 웹페이지로 이동
print('잠시 뒤 네이버로 이동합니다.')
driver.get("https://www.naver.com")

#네이버 뉴스 크롤링
print('잠시 뒤 네이버 뉴스로 이동합니다')
driver.get("https://www.naver.com")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)
title = driver.find_element(By.XPATH, "/html/body/div/div[6]/div[1]/div/div[3]/div[2]/div/ul/li[1]/a/strong").text
print(title)'''

#네이버 부동산 매물 크롤링
print('네이버 부동산으로 이동합니다')
driver.get("https://land.naver.com/")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/input[6]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/input[6]").send_keys("압구정동 현대3차")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/a[1]/i").click()
time.sleep(3)
salesPrices = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/dl[1]/dd").text
jeonse = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/dl[2]/dd").text
print('매매가', salesPrices)
print('전세', jeonse)