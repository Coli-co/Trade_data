from selenium import webdriver
import time
from bs4 import BeautifulSoup
# 注意：使用Keys方法要先引入以下這一行
from selenium.webdriver.common.keys import Keys
import pymysql

# 上市或上櫃類股網站
driver = webdriver.Chrome('D:\\timothyTest\data_crawling\chromedriver')
driver.get('https://www.wantgoo.com/stock/ranking/top-loser?market=OTC')
time.sleep(2)


def sector_of_liststock_high():
    box = []
    # 日期
    for q in range(10):
        temp = []
        z = driver.find_elements_by_css_selector(
            "time[class='text-muted ml-auto']")[0]
        date = z.text
        temp.append(date)
        time.sleep(2)
        # 上市類股代碼
        for i in range(q, q+1):
            # temp = []
            a = driver.find_elements_by_class_name("lt")[i]
            stock_num = a.text
            temp.append(stock_num)
            time.sleep(2)
            # 上市類股名稱
            for j in range(i, i+1):
                b = driver.find_elements_by_class_name("zw")[j]
                stock_name = b.text
                temp.append(stock_name)
                time.sleep(2)
                driver.get('https://www.wantgoo.com/stock')
                time.sleep(2)
                # 上市類股種類
                for k in range(j, j+1):
                    # 定位搜尋
                    searchstock = driver.find_element_by_css_selector(
                        "span[class='twitter-typeahead'] input[type='text']")
                    # 輸入類股名稱
                    searchstock.send_keys(stock_num)
                    time.sleep(2)
                    # 按下ENTER
                    searchstock.send_keys(Keys.ENTER)
                    time.sleep(3)
                    # 定位股票種類
                    h = driver.find_elements_by_css_selector(
                        "a[class='nav-link'] span[class='mr-1']")[1]
                    sector = h.text
                    time.sleep(2)
                    temp.append(sector)
                    driver.get(
                        'https://www.wantgoo.com/stock/ranking/top-loser?market=OTC')
                    time.sleep(2)
                # 收盤價
                    for l in range(k, k+1):
                        c = driver.find_elements_by_css_selector(
                            "td[c-model-dazzle='class:upDn,text:close']")[l]
                        close_price = c.text
                        temp.append(close_price)
                        time.sleep(2)
                # 漲跌
                        for m in range(l, l+1):
                            d = driver.find_elements_by_css_selector(
                                "td[c-model-dazzle='class:upDn,text:`{changeSymbol}{change}`']")[m]
                            high_and_low = d.text
                            temp.append(high_and_low)
                            time.sleep(2)
                # 漲幅%
                            for n in range(m, m+1):
                                e = driver.find_elements_by_css_selector(
                                    "td[c-model-dazzle='class:upDn,text:changePercent']")[n]
                                width_of_high = e.text
                                temp.append(width_of_high)
                                time.sleep(2)
                # 振幅%
                                for o in range(n, n+1):
                                    f = driver.find_elements_by_css_selector(
                                        "td[c-model='amplitute']")[o]
                                    amplitude = f.text
                                    temp.append(amplitude)
                                    time.sleep(2)
                # 成交量
                                    for p in range(o, o+1):
                                        g = driver.find_elements_by_css_selector(
                                            "td[c-model='volume']")[p]
                                        volume = g.text
                                        temp.append(volume)
                                        time.sleep(2)

        box.append(temp)

    return box


""" 
Get information from  sector of liststock which dominate the day of high_and_low .
The function include  stock_number, stock_name, sector, close_price, high_and_low,
width_of_high, amplitude, and volume.
"""

stock_info = sector_of_liststock_high()


def data_crawling_extract(stock_info):

    box2 = []
    for i in range(len(stock_info)):
        date = stock_info[i][0].replace("/", "-")
        stock_number = stock_info[i][1]
        stock_name = stock_info[i][2]
        sector = stock_info[i][3]
        close_price = stock_info[i][4]
        high_and_low = stock_info[i][5]
        width_of_high = stock_info[i][6]
        amplitude = stock_info[i][7]
        volume = stock_info[i][8].replace(",", "")

        box2.append((date, stock_number, stock_name, sector,
                    close_price, high_and_low, width_of_high,
                    amplitude, volume))

    return box2


"""
Withdraw data from crawling.
"""

real_data_get = data_crawling_extract(stock_info)


def mysql_renewdata_insert(real_data_get):

    # 建立連線
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='1qaz2wsx', db='trader_info', charset='utf8')
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(real_data_get)):
        sql = "insert into sector_of_liststock_high\
                    (date, stock_number, stock_name, sector, close_price,\
                    high_and_low, width_of_high, amplitude, volume)\
                    values('%s', %s, '%s', '%s', %s, '%s', %s, %s, %s)"\
                    % (real_data_get[i][0], real_data_get[i][1], real_data_get[i][2],
                       real_data_get[i][3], real_data_get[i][4], real_data_get[i][5],
                       real_data_get[i][6], real_data_get[i][7], real_data_get[i][8])
        try:
            cursor.execute(sql)
            conn.commit()
            print("stock_info successfully inserted.")
        except:
            print("stock_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


"""
Insert renew data into MySQL table from withdrawal
"""

mysql_renewdata_insert(real_data_get)


driver.close()
