import os
import time
import random
import shutil
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


my_username = "<username>"
my_password = "<password>"
download_path = "D:\\AutoDownload"
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': download_path,
         "profile.default_content_setting_values.automatic_downloads": 1
         }

f = open('website.txt', encoding='utf-8')
webpage = []
for line in f:
    webpage.append(line.strip())
f.close()


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


mkdir(download_path)

option = Options()
option.add_experimental_option('prefs', prefs)

option.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Edge(options=option)
driver.get("https://www.stmcu.com.cn/")

driver.find_element(By.LINK_TEXT, "登录").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "账号密码登录").click()
driver.find_element(By.ID, "username").send_keys(my_username)
driver.find_element(By.ID, "password").send_keys(my_password)
time.sleep(random.randint(1, 5))
driver.find_element(By.CLASS_NAME, "l1").click()

rd = [randrange(1000) for j in range(30)]
js = ''
print("以下网址下载失败")
for i in rd:
    js = 'window.open("' + webpage[i] + '");'
    driver.execute_script(js)
    time.sleep(10)
    handles = driver.window_handles
    try:
        driver.switch_to.window(handles[-1])
        time.sleep(random.randint(1, 4))
        driver.find_element(By.XPATH, '//*[@id="down_load_btn"]').click()
        time.sleep(random.randint(1, 4))
    except:
        print(webpage[i])
time.sleep(random.randint(1, 4))
driver.quit()
print('下载已完成')
shutil.rmtree(download_path)
print(download_path + '文件夹已经删除')