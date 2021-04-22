import time

# from selenium import webdriver

# pip install selenium-wire (Надстройка для selenium с доп. возможностями)
from seleniumwire import webdriver
from time import sleep
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password


# url = 'https://instagram.com/'

# user_agents_list = [
#     'hello_world',
#     'best_of_the_best',
#     'python_fire'
# ]

user_agent = UserAgent()

# Создаём объект Опций
options = webdriver.ChromeOptions()
# добавляем опции
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# Можно выбирать любой браузер(ie, opera, chrome) или .random
options.add_argument(f"user-agent={user_agent.chrome}")

# Добавляем прокси(если не используется имя пользователя и пароль от прокси!)
# options.add_argument("--proxy-server=91.231.8.198:8000")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@91.231.8.198:8000"
    }
}


# driver = webdriver.Chrome(executable_path='/home/vyacheslav/python_selenium/lesson_1/chromedriver/chromedriver',
#                           options=options)

driver = webdriver.Chrome(executable_path='/home/vyacheslav/python_selenium/lesson_1/chromedriver/chromedriver',
                          seleniumwire_options=proxy_options)

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # sleep(5)

    # refrash - обновляет окно браузера.
    # driver.refresh()

    # Делает скриншот страницы и сохраняет её.
    # driver.get_screenshot_as_file('1.png')
    #
    # driver.get('https://stackoverflow.com/')
    # sleep(5)

    # Делает скриншот страницы и сохраняет её.
    # driver.save_screenshot('2.png')
    # sleep(2)

    driver.get("https://2ip.ru")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    # Закрывает окно браузера
    driver.close()
    driver.quit()
