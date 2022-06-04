import time
from random import *
from selenium import webdriver
from selenium.webdriver.common.by import By

my_username = "<username>"
my_password = "<password>"

f = open('website.txt', encoding='utf-8')
webpage = []
for line in f:
    webpage.append(line.strip())
f.close

driver = webdriver.Edge()

driver.get("https://www.stmcu.com.cn/")

driver.find_element(By.LINK_TEXT, "登录").click()
driver.find_element(By.LINK_TEXT, "账号密码登录").click()
driver.find_element(By.ID, "username").send_keys(my_username)
driver.find_element(By.ID, "password").send_keys(my_password)
driver.find_element(By.CSS_SELECTOR, ".an_lan").click()

rd = [randrange(1000) for j in range(30)]
js = ''

for i in rd:
    js = 'window.open("' + webpage[i] + '");'
    driver.execute_script(js)
    time.sleep(1)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="down_load_btn"]').click()
    time.sleep(4)
time.sleep(10)
driver.quit()
