from selenium import webdriver
import time
from bs4 import BeautifulSoup
# 注意：使用Keys方法要先引入以下這一行
from selenium.webdriver.common.keys import Keys
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome('D:\\timothyTest\data_crawler\chromedriver')


def date_and_close_price():
    # 證交所網站
    driver.get('https://www.twse.com.tw/zh/')
    time.sleep(3)
    # 日期
    button = driver.find_element_by_css_selector("li[class='info']")
    button.click()
    time.sleep(2)
    box = []
    temp = []
    date = driver.find_element_by_css_selector(
        "#main > div.row.row1 > div.col1 > section:nth-child(3) > div > div > div.body.active > div > div.body.active > div > ul > li:nth-child(1)")
    date1 = date.text
    date2 = date1.replace("資料時間：", "")
    date3 = date2.replace("/", "-")
    temp.append(date3)
    # 大盤收盤價
    b = driver.find_element_by_css_selector(
        "#main-index-info > table > tbody > tr:nth-child(3) > td:nth-child(2)")
    b1 = b.text
    b2 = b1.replace(",", "")
    temp.append(b2)
    box.append(temp)
    print(box)
    return box


a = date_and_close_price()


def insert_data_and_closeprice_into_database(a):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))
    # 建立操作遊標, 查詢資料預設為元組型別

    cursor = conn.cursor()
    for i in range(len(a)):
        sql = "insert into % s\
                    (date, market_close_price)\
                    values('%s', % s)" % ((os.getenv("table_a"), a[i][0], a[i][1])
    # try:
    cursor.execute(sql)
    conn.commit()
    #     print("market_bargainingchip successfully inserted.")
    # except:
    #     print("market_bargainingchip update failed!")
    #     conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


date_closeprice_realdata=insert_data_and_closeprice_into_database(a)


def foreign_capital_cost():
    driver.get('https://www.taifex.com.tw/cht/3/futContractsDate')
    time.sleep(2)
    temp=[]
    box=[]
    # 選擇外資成本日期
    button1=driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button1.click()
    time.sleep(2)
    button2=driver.find_element_by_link_text("13")
    button2.click()
    time.sleep(2)
    button3=driver.find_element_by_css_selector("#button")
    button3.click()
    time.sleep(2)
    # driver.close()

    # 外資當日成本
    money=driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(13) > div:nth-child(1)")
    money1=money.text
    # print(money1)
    position=driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1) > font")
    position1=position.text
    # print(position1)
    truemoney=money1.replace(",", "")
    trueposition=position1.replace(",", "")
    trueposition=round(int(truemoney)/int(trueposition)/200*1000, 2)
    # print(trueposition)
    temp.append(trueposition)
    # print(temp)

    # 外資前一天成本
    # 選擇日期
    button_1=driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button_1.click()
    time.sleep(2)
    button_2=driver.find_element_by_link_text("12")
    button_2.click()
    time.sleep(2)
    button_3=driver.find_element_by_css_selector("#button")
    button_3.click()
    time.sleep(2)
    previousone_money=driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(13) > div:nth-child(1)")
    previousone_money1=previousone_money.text

    previousone_position=driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1) > font")
    previousone_position1=previousone_position.text

    previousone_truemoney=previousone_money1.replace(",", "")
    previousone_trueposition=previousone_position1.replace(",", "")
    previousone_trueposition=round(
        int(previousone_truemoney)/int(previousone_trueposition)/200*1000, 2)
    # print(previousone_trueposition)

    # 外資前兩天成本
    # 選擇日期
    button1=driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button1.click()
    time.sleep(2)
    button2=driver.find_element_by_link_text("11")
    button2.click()
    time.sleep(2)
    button3=driver.find_element_by_css_selector("#button")
    button3.click()
    time.sleep(2)
    previoustwo_money=driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(13) > div:nth-child(1)")
    previoustwo_money1=previoustwo_money.text

    previoustwo_position=driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1) > font")
    previoustwo_position1=previoustwo_position.text

    previoustwo_truemoney=previoustwo_money1.replace(",", "")
    previoustwo_trueposition=previoustwo_position1.replace(",", "")
    previoustwo_trueposition=round(
        int(previoustwo_truemoney)/int(previoustwo_trueposition)/200*1000, 2)
    # print(previoustwo_trueposition)

    foreign_average_cost=round((
        trueposition+previousone_trueposition+previoustwo_trueposition)/3, 2)
    # print(foreign_average_cost)
    temp.append(foreign_average_cost)
    box.append(temp)
    print(box)
    return box


# b = foreign_capital_cost()


def insert_renewdata_into_database(b):
    # 建立連線
    conn=pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset")
                           )
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor=conn.cursor()

    for i in range(len(a)):
        sql="insert into market_bargainingchip\
                    (foreign_capital_cost, foreign_capital_average_cost)\
                    values('%s', '%s')" % (a[i][0], a[i][1])
        # try:
        cursor.execute(sql)
        conn.commit()
        #     print("market_bargainingchip successfully inserted.")
        # except:
        #     print("market_bargainingchip update failed!")
        #     conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


# foreign_realdata = insert_renewdata_into_database(b)
driver.close()
