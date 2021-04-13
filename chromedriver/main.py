from selenium import webdriver
from time import sleep


url = 'https://instagram.com/'
driver = webdriver.Chrome(executable_path='/home/vyacheslav/python_selenium/chromedriver/chromedriver')

try:
    driver.get(url=url)
    sleep(5)

    # refrash - обновляет окно браузера.
    # driver.refresh()

    # Делает скриншот страницы и сохраняет её.
    driver.get_screenshot_as_file('1.png')

    driver.get('https://stackoverflow.com/')
    sleep(5)

    # Делает скриншот страницы и сохраняет её.
    driver.save_screenshot('2.png')
    sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
