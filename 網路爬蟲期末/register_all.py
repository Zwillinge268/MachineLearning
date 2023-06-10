from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from fake_useragent import UserAgent
import time

#瀏覽器設定
ua = UserAgent()
userAgent = ua.random

#options 設定
options = Options() 
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--headless')  # 非本機執行，必須啟動Headless模式
options.add_argument('--disable-gpu') # 關閉GPU 避免某些系統或是網頁出錯
options.add_argument("--disable-notifications") # 關閉彈出視窗

#service 設定
service = Service()

#載入driver
driver = webdriver.Edge(service=service, options=options)

#設定網址
url = 'http://120.105.96.87/register_all.html'
driver.get(url)

#==================================================================#

#id欄位
myid = driver.find_element(By.NAME, "id")
myid.clear()
myid.send_keys("B09280065")

#email 欄位
myemail = driver.find_element(By.NAME, "email")
myemail.clear()
myemail.send_keys("B09280065@std.must.edu.tw")

#password 欄位
passwd = driver.find_element(By.NAME, "pwd")
passwd.clear()
passwd.send_keys("B09280065")

#sex 欄位
sex = driver.find_element(By.XPATH,".//input[@type='radio' and @value='m']")
sex.click()

#interest 欄位
interest = driver.find_element(By.XPATH,".//input[@type='checkbox' and @value='tv']")
interest.click()

#country 欄位
country = driver.find_element(By.NAME,"county")
select = Select(country)
select.select_by_value('miaoli')

# 註冊畫面（填入資料）截取
driver.get_screenshot_as_file('image\\data5.png') 

#按下注冊
mysubmit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "submit")))
mysubmit.submit()
time.sleep(1)

# 註冊畫面（成功注冊）截取
driver.get_screenshot_as_file('image\\data6.png')

#關閉driver
driver.close()