from selenium import webdriver
from time import sleep


url = 'https://instagram.com/'
driver = webdriver.Chrome(executable_path='absolute path chromedriver')

try:
    driver.get(url=url)
    sleep(5)
    # driver.get('https://stackoverflow.com/')
    # sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
