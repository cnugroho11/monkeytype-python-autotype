import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://monkeytype.com/")

cookiePopup = driver.find_element(By.XPATH, "//div[@class='button active acceptAll']")
cookiePopup.click()

body = driver.find_element(By.XPATH, "//body")
searchInput = driver.find_element(By.XPATH, "//input[@class='input']")

# show live wpm
body.send_keys(Keys.ESCAPE)
searchInput.send_keys('live wpm')
body.send_keys(Keys.ENTER)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.ENTER)
time.sleep(0.1)

# show live accuracy
body.send_keys(Keys.ESCAPE)
searchInput.send_keys('live acc')
body.send_keys(Keys.ENTER)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.ENTER)
time.sleep(0.1)

# show live burst
body.send_keys(Keys.ESCAPE)
searchInput.send_keys('live burst')
body.send_keys(Keys.ENTER)
body.send_keys(Keys.DOWN)
body.send_keys(Keys.ENTER)
time.sleep(0.1)

# change time
body.send_keys(Keys.ESCAPE)
searchInput.send_keys('time')
body.send_keys(Keys.ENTER)
searchInput.send_keys('120')
body.send_keys(Keys.ENTER)
time.sleep(0.3)

# change language to indonesia
body.send_keys(Keys.ESCAPE)
searchInput.send_keys('lan')
body.send_keys(Keys.ENTER)
searchInput.send_keys('ind')
body.send_keys(Keys.ENTER)
time.sleep(0.3)

while True:
    word = driver.find_element(By.XPATH, "//div[@class='word active']")
    for letter in word.text:
        speed = float("0.0"+str(random.randint(1, 5)))
        wrongChar = word.text[random.randint(0,1)]
        if random.random() <= 0.2:
            body.send_keys(wrongChar)
            if wrongChar != letter:
                time.sleep(speed)
                body.send_keys(Keys.BACKSPACE)
                body.send_keys(letter)
        else:
            body.send_keys(letter)
        time.sleep(speed)
        print(speed)
    body.send_keys(Keys.SPACE)