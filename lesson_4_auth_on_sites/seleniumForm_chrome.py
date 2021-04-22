from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from fake_useragent import UserAgent
from auth_data import vk_password, user_name

#
# user_agent = UserAgent()

# Создаём объект Опций
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")

driver = webdriver.Chrome(executable_path='/home/vyacheslav/python_selenium/lesson_1/chromedriver/chromedriver',
                          options=options)

try:
    driver.get('https://vk.com')
    sleep(5)

    email_input = driver.find_element_by_id("index_email")
    # Очищает поле
    email_input.clear()
    email_input.send_keys(user_name)
    sleep(3)

    password_input = driver.find_element_by_xpath('//*[@id="index_pass"]')
    password_input.clear()
    password_input.send_keys(vk_password)
    sleep(3)
    password_input.send_keys(Keys.ENTER)
    # login_button = driver.find_element_by_id('index_login_button')
    # login_button.click()
    sleep(15)

    news_link = driver.find_element_by_id('l_nwsf').click()
    sleep(15)

except Exception as ex:
    print(ex)
finally:
    # Закрывает окно браузера
    driver.close()
    driver.quit()
