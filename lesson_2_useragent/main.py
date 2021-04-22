from selenium import webdriver
from time import sleep
import random
from fake_useragent import UserAgent


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


driver = webdriver.Chrome(executable_path='/home/vyacheslav/python_selenium/lesson_1/chromedriver/chromedriver',
                          options=options)

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    sleep(5)

    # refrash - обновляет окно браузера.
    driver.refresh()

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
    # Закрывает окно браузера
    driver.close()
    driver.quit()
