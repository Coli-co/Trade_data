from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:\\timothyTest\chromedriver')
driver.get('https://zh-tw.facebook.com/')
# print (driver.title)
# driver.quit()
# driver.close()
# 然後盤點會使用到的 Selenium WebDriver 方法：
# driver.get() ：前往 IMDB.com 首頁
# driver.find_element_by_xpath() 或 driver.find_element_by_css_selector() ：定位搜尋欄位、搜尋按鈕與搜尋結果連結
# driver.current_url ：取得當下瀏覽器的網址
# elem.send_keys() ：輸入電影名稱
# elem.click() ：按下搜尋按鈕與連結

# 定位搜尋框
# element = driver.find_element_by_class_name("gLFyf.gsfi")
# # 輸入關鍵字
# element.send_keys("Selenium Python")
# 清除關鍵字
# element.clear()
# 定位搜尋位置並前往搜尋頁面

email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

email.send_keys('awese@gmail.com')
password.send_keys('abcdefg')
password.submit()

time.sleep(3)
driver.get('https://www.facebook.com/learncodewithmike')

# 滑動滾輪
for x in range(1, 4):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)


soup = BeautifulSoup(driver.page_source, 'html.parser')

titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ojkyduve'})


for title in titles:

    post = title.find('span', {'dir': 'auto'})

    if post:
        print(post.getText())

driver.quit()
