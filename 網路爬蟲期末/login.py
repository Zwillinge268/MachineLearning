from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

#瀏覽器設定
ua = UserAgent()
userAgent = ua.random

#options & service 設定
options = Options() 
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--headless')  # 非本機執行，必須啟動Headless模式
options.add_argument('--disable-gpu') # 關閉GPU 避免某些系統或是網頁出錯
options.add_argument("--disable-notifications") # 關閉彈出視窗
service1 = Service()

#載入driver
driver1 = webdriver.Edge(service=service1, options=options)

#設定網址
url = 'http://120.105.96.87/index.html'
driver1.get(url)

#id欄位
myid = driver1.find_element(By.NAME, "id")
myid.clear()
myid.send_keys("B09280065")

#password欄位
passwd = driver1.find_element(By.NAME, "pwd")
passwd.clear()
passwd.send_keys("B09280065")

# 登入畫面（填入資料）截取
driver1.get_screenshot_as_file('image\\data3.png')

#按下登入
mysubmit = WebDriverWait(driver1, 5).until(EC.presence_of_element_located((By.NAME, "submit")))
mysubmit.submit()
time.sleep(1)

# 登入畫面（成功登入）截取
driver1.get_screenshot_as_file('image\\data4.png')

#關閉driver
driver1.close()