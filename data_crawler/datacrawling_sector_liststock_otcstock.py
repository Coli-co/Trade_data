from selenium import webdriver
import time
from bs4 import BeautifulSoup
# 注意：使用Keys方法要先引入以下這一行
from selenium.webdriver.common.keys import Keys
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

# Remember to adjust to different page
# search_page
url0 = os.getenv("url0")
# categories_page
url1 = os.getenv("url1")
url2 = os.getenv("url2")
url3 = os.getenv("url3")
url4 = os.getenv("url4")


def get_page():
    driver = webdriver.Chrome('D:\\timothyTest\data_crawler\chromedriver')
    page = driver.get(url1)

    return driver


run_listwinner = get_page()
# run_listloser = get_page()
# run_otcwinner = get_page()
# run_otcloser = get_page()


def sector_of_listwinner(run_listwinner):
    time.sleep(3)
    box = []
    # 日期
    for q in range(10, 11):
        temp = []
        z = run_listwinner.find_elements_by_css_selector(
            "time[class='text-muted ml-auto']")[0]
        date = z.text
        temp.append(date)
        time.sleep(2)
        # 上市類股代碼
        for i in range(q, q+1):
            # temp = []
            a = "#rankingData > tr:nth-child(%s) > td.lt > a" % (q)
            a1 = run_listwinner.find_element_by_css_selector(a)
            stock_num = a1.text
            temp.append(stock_num)
            time.sleep(2)
            # 上市類股名稱
            for j in range(i, i+1):
                b = "#rankingData > tr:nth-child(%s) > td.zw > a" % (q)
                b1 = run_listwinner.find_element_by_css_selector(b)
                stock_name = b1.text
                temp.append(stock_name)
                time.sleep(2)
                run_listwinner.get(url0)
                time.sleep(2)
                # 上市類股種類
                for k in range(j, j+1):
                    # 定位搜尋
                    searchstock = run_listwinner.find_element_by_css_selector(
                        "span[class='twitter-typeahead'] input[type='text']")
                    # 輸入類股名稱
                    searchstock.send_keys(stock_num)
                    time.sleep(3)
                    # 按下ENTER
                    searchstock.send_keys(Keys.ENTER)
                    time.sleep(4)
                    # 定位股票種類
                    h = run_listwinner.find_elements_by_css_selector(
                        "a[class='nav-link'] span[class='mr-1']")[1]
                    sector = h.text
                    time.sleep(3)
                    temp.append(sector)
                    run_listwinner.get(url1)
                    time.sleep(3)
                # 收盤價
                    for l in range(k, k+1):
                        c = "#rankingData > tr:nth-child(%s) > td:nth-child(4)" % (
                            q)
                        c1 = run_listwinner.find_element_by_css_selector(c)
                        close_price = c1.text
                        temp.append(close_price)
                        time.sleep(2)
                # 漲跌
                        for m in range(l, l+1):
                            d = "#rankingData > tr:nth-child(%s) > td:nth-child(5)" % (
                                q)
                            d1 = run_listwinner.find_element_by_css_selector(d)
                            high_and_low = d1.text
                            temp.append(high_and_low)
                            time.sleep(2)
                # 漲幅%
                            for n in range(m, m+1):
                                e = "#rankingData > tr:nth-child(%s) > td:nth-child(6)" % (
                                    q)
                                e1 = run_listwinner.find_element_by_css_selector(
                                    e)
                                width_of_high = e1.text
                                temp.append(width_of_high)
                                time.sleep(2)
                # 振幅%
                                for o in range(n, n+1):
                                    f = "#rankingData > tr:nth-child(%s) > td:nth-child(8)" % (
                                        q)
                                    f1 = run_listwinner.find_element_by_css_selector(
                                        f)
                                    amplitude = f1.text
                                    temp.append(amplitude)
                                    time.sleep(2)
                # 成交量
                                    for p in range(o, o+1):
                                        g = "#rankingData > tr:nth-child(%s) > td:nth-child(11)" % (
                                            q)
                                        g1 = run_listwinner.find_element_by_css_selector(
                                            g)
                                        volume = g1.text
                                        temp.append(volume)
                                        time.sleep(2)

        box.append(temp)

    return box


listwinner_info = sector_of_listwinner(run_listwinner)


def sector_of_listloser(run_listloser):
    time.sleep(3)
    box = []
    # 日期
    for q in range(1, 11):
        temp = []
        z = run_listloser.find_elements_by_css_selector(
            "time[class='text-muted ml-auto']")[0]
        date = z.text
        temp.append(date)
        time.sleep(2)
        # 上市類股代碼
        for i in range(q, q+1):
            # temp = []
            a = "#rankingData > tr:nth-child(%s) > td.lt > a" % (q)
            a1 = run_listloser.find_element_by_css_selector(a)
            stock_num = a1.text
            temp.append(stock_num)
            time.sleep(2)
            # 上市類股名稱
            for j in range(i, i+1):
                b = "#rankingData > tr:nth-child(%s) > td.zw > a" % (q)
                b1 = run_listloser.find_element_by_css_selector(b)
                stock_name = b1.text
                temp.append(stock_name)
                time.sleep(2)
                run_listloser.get(url0)
                time.sleep(2)
                # 上市類股種類
                for k in range(j, j+1):
                    # 定位搜尋
                    searchstock = run_listloser.find_element_by_css_selector(
                        "span[class='twitter-typeahead'] input[type='text']")
                    # 輸入類股名稱
                    searchstock.send_keys(stock_num)
                    time.sleep(3)
                    # 按下ENTER
                    searchstock.send_keys(Keys.ENTER)
                    time.sleep(4)
                    # 定位股票種類
                    h = run_listloser.find_elements_by_css_selector(
                        "a[class='nav-link'] span[class='mr-1']")[1]
                    sector = h.text
                    time.sleep(3)
                    temp.append(sector)
                    run_listloser.get(url2)
                    time.sleep(3)
                # 收盤價
                    for l in range(k, k+1):
                        c = "#rankingData > tr:nth-child(%s) > td:nth-child(4)" % (
                            q)
                        c1 = run_listloser.find_element_by_css_selector(c)
                        close_price = c1.text
                        temp.append(close_price)
                        time.sleep(2)
                # 漲跌
                        for m in range(l, l+1):
                            d = "#rankingData > tr:nth-child(%s) > td:nth-child(5)" % (
                                q)
                            d1 = run_listloser.find_element_by_css_selector(d)
                            high_and_low = d1.text
                            temp.append(high_and_low)
                            time.sleep(2)
                # 漲幅%
                            for n in range(m, m+1):
                                e = "#rankingData > tr:nth-child(%s) > td:nth-child(6)" % (
                                    q)
                                e1 = run_listloser.find_element_by_css_selector(
                                    e)
                                width_of_high = e1.text
                                temp.append(width_of_high)
                                time.sleep(2)
                # 振幅%
                                for o in range(n, n+1):
                                    f = "#rankingData > tr:nth-child(%s) > td:nth-child(8)" % (
                                        q)
                                    f1 = run_listloser.find_element_by_css_selector(
                                        f)
                                    amplitude = f1.text
                                    temp.append(amplitude)
                                    time.sleep(2)
                # 成交量
                                    for p in range(o, o+1):
                                        g = "#rankingData > tr:nth-child(%s) > td:nth-child(11)" % (
                                            q)
                                        g1 = run_listloser.find_element_by_css_selector(
                                            g)
                                        volume = g1.text
                                        temp.append(volume)
                                        time.sleep(2)

        box.append(temp)

    return box


# listloser_info = sector_of_listloser(run_listloser)


def sector_of_otcwinner(run_otcwinner):
    time.sleep(3)
    box = []
    # 日期
    for q in range(1, 11):
        temp = []
        z = run_otcwinner.find_elements_by_css_selector(
            "time[class='text-muted ml-auto']")[0]
        date = z.text
        temp.append(date)
        time.sleep(2)
        # 上市類股代碼
        for i in range(q, q+1):
            # temp = []
            a = "#rankingData > tr:nth-child(%s) > td.lt > a" % (q)
            a1 = run_otcwinner.find_element_by_css_selector(a)
            stock_num = a1.text
            temp.append(stock_num)
            time.sleep(2)
            # 上市類股名稱
            for j in range(i, i+1):
                b = "#rankingData > tr:nth-child(%s) > td.zw > a" % (q)
                b1 = run_otcwinner.find_element_by_css_selector(b)
                stock_name = b1.text
                temp.append(stock_name)
                time.sleep(2)
                run_otcwinner.get(url0)
                time.sleep(2)
                # 上市類股種類
                for k in range(j, j+1):
                    # 定位搜尋
                    searchstock = run_otcwinner.find_element_by_css_selector(
                        "span[class='twitter-typeahead'] input[type='text']")
                    # 輸入類股名稱
                    searchstock.send_keys(stock_num)
                    time.sleep(3)
                    # 按下ENTER
                    searchstock.send_keys(Keys.ENTER)
                    time.sleep(4)
                    # 定位股票種類
                    h = run_otcwinner.find_elements_by_css_selector(
                        "a[class='nav-link'] span[class='mr-1']")[1]
                    sector = h.text
                    time.sleep(3)
                    temp.append(sector)
                    run_otcwinner.get(url3)
                    time.sleep(3)
                # 收盤價
                    for l in range(k, k+1):
                        c = "#rankingData > tr:nth-child(%s) > td:nth-child(4)" % (
                            q)
                        c1 = run_otcwinner.find_element_by_css_selector(c)
                        close_price = c1.text
                        temp.append(close_price)
                        time.sleep(2)
                # 漲跌
                        for m in range(l, l+1):
                            d = "#rankingData > tr:nth-child(%s) > td:nth-child(5)" % (
                                q)
                            d1 = run_otcwinner.find_element_by_css_selector(d)
                            high_and_low = d1.text
                            temp.append(high_and_low)
                            time.sleep(2)
                # 漲幅%
                            for n in range(m, m+1):
                                e = "#rankingData > tr:nth-child(%s) > td:nth-child(6)" % (
                                    q)
                                e1 = run_otcwinner.find_element_by_css_selector(
                                    e)
                                width_of_high = e1.text
                                temp.append(width_of_high)
                                time.sleep(2)
                # 振幅%
                                for o in range(n, n+1):
                                    f = "#rankingData > tr:nth-child(%s) > td:nth-child(8)" % (
                                        q)
                                    f1 = run_otcwinner.find_element_by_css_selector(
                                        f)
                                    amplitude = f1.text
                                    temp.append(amplitude)
                                    time.sleep(2)
                # 成交量
                                    for p in range(o, o+1):
                                        g = "#rankingData > tr:nth-child(%s) > td:nth-child(11)" % (
                                            q)
                                        g1 = run_otcwinner.find_element_by_css_selector(
                                            g)
                                        volume = g1.text
                                        temp.append(volume)
                                        time.sleep(2)

        box.append(temp)

    return box


# otcwinner_info = sector_of_otcwinner(run_otcwinner)


def sector_of_otcloser(run_otcloser):
    time.sleep(3)
    box = []
    # 日期
    for q in range(1, 11):
        temp = []
        z = run_otcloser.find_elements_by_css_selector(
            "time[class='text-muted ml-auto']")[0]
        date = z.text
        temp.append(date)
        time.sleep(2)
        # 上市類股代碼
        for i in range(q, q+1):
            # temp = []
            a = "#rankingData > tr:nth-child(%s) > td.lt > a" % (q)
            a1 = run_otcloser.find_element_by_css_selector(a)
            stock_num = a1.text
            temp.append(stock_num)
            time.sleep(2)
            # 上市類股名稱
            for j in range(i, i+1):
                b = "#rankingData > tr:nth-child(%s) > td.zw > a" % (q)
                b1 = run_otcloser.find_element_by_css_selector(b)
                stock_name = b1.text
                temp.append(stock_name)
                time.sleep(2)
                run_otcloser.get(url0)
                time.sleep(2)
                # 上市類股種類
                for k in range(j, j+1):
                    # 定位搜尋
                    searchstock = run_otcloser.find_element_by_css_selector(
                        "span[class='twitter-typeahead'] input[type='text']")
                    # 輸入類股名稱
                    searchstock.send_keys(stock_num)
                    time.sleep(3)
                    # 按下ENTER
                    searchstock.send_keys(Keys.ENTER)
                    time.sleep(4)
                    # 定位股票種類
                    h = run_otcloser.find_elements_by_css_selector(
                        "a[class='nav-link'] span[class='mr-1']")[1]
                    sector = h.text
                    time.sleep(3)
                    temp.append(sector)
                    run_otcloser.get(url4)
                    time.sleep(3)
                # 收盤價
                    for l in range(k, k+1):
                        c = "#rankingData > tr:nth-child(%s) > td:nth-child(4)" % (
                            q)
                        c1 = run_otcloser.find_element_by_css_selector(c)
                        close_price = c1.text
                        temp.append(close_price)
                        time.sleep(2)
                # 漲跌
                        for m in range(l, l+1):
                            d = "#rankingData > tr:nth-child(%s) > td:nth-child(5)" % (
                                q)
                            d1 = run_otcloser.find_element_by_css_selector(d)
                            high_and_low = d1.text
                            temp.append(high_and_low)
                            time.sleep(2)
                # 漲幅%
                            for n in range(m, m+1):
                                e = "#rankingData > tr:nth-child(%s) > td:nth-child(6)" % (
                                    q)
                                e1 = run_otcloser.find_element_by_css_selector(
                                    e)
                                width_of_high = e1.text
                                temp.append(width_of_high)
                                time.sleep(2)
                # 振幅%
                                for o in range(n, n+1):
                                    f = "#rankingData > tr:nth-child(%s) > td:nth-child(8)" % (
                                        q)
                                    f1 = run_otcloser.find_element_by_css_selector(
                                        f)
                                    amplitude = f1.text
                                    temp.append(amplitude)
                                    time.sleep(2)
                # 成交量
                                    for p in range(o, o+1):
                                        g = "#rankingData > tr:nth-child(%s) > td:nth-child(11)" % (
                                            q)
                                        g1 = run_otcloser.find_element_by_css_selector(
                                            g)
                                        volume = g1.text
                                        temp.append(volume)
                                        time.sleep(2)

        box.append(temp)

    return box


# otcloser_info = sector_of_otcloser(run_otcloser)

""" 
Get information from  sector of liststock which dominate the day of high_and_low .
The function include  stock_number, stock_name, sector, close_price, high_and_low,
width_of_high, amplitude, and volume.
"""


def data_crawling_extract(listwinner_info):

    box2 = []
    for i in range(len(listwinner_info)):
        date = listwinner_info[i][0].replace("/", "-")
        stock_number = listwinner_info[i][1]
        stock_name = listwinner_info[i][2]
        sector = listwinner_info[i][3]
        close_price = listwinner_info[i][4]
        high_and_low = listwinner_info[i][5]
        width_of_high = listwinner_info[i][6]
        amplitude = listwinner_info[i][7]
        volume = listwinner_info[i][8].replace(",", "")

        box2.append((date, stock_number, stock_name, sector,
                    close_price, high_and_low, width_of_high,
                    amplitude, volume))

    return box2


"""
Withdraw data from crawling.
"""

real_data_get1 = data_crawling_extract(listwinner_info)


def data_crawling_extract(listloser_info):
    box2 = []
    for i in range(len(listloser_info)):
        date = listloser_info[i][0].replace("/", "-")
        stock_number = listloser_info[i][1]
        stock_name = listloser_info[i][2]
        sector = listloser_info[i][3]
        close_price = listloser_info[i][4]
        high_and_low = listloser_info[i][5]
        width_of_high = listloser_info[i][6]
        amplitude = listloser_info[i][7]
        volume = listloser_info[i][8].replace(",", "")

        box2.append((date, stock_number, stock_name, sector,
                    close_price, high_and_low, width_of_high,
                    amplitude, volume))

    return box2


# real_data_get2 = data_crawling_extract(listloser_info)


def data_crawling_extract(otcwinner_info):
    box2 = []
    for i in range(len(otcwinner_info)):
        date = otcwinner_info[i][0].replace("/", "-")
        stock_number = otcwinner_info[i][1]
        stock_name = otcwinner_info[i][2]
        sector = otcwinner_info[i][3]
        close_price = otcwinner_info[i][4]
        high_and_low = otcwinner_info[i][5]
        width_of_high = otcwinner_info[i][6]
        amplitude = otcwinner_info[i][7]
        volume = otcwinner_info[i][8].replace(",", "")

        box2.append((date, stock_number, stock_name, sector,
                    close_price, high_and_low, width_of_high,
                    amplitude, volume))

    return box2


# real_data_get3 = data_crawling_extract(otcwinner_info)


def data_crawling_extract(otcloser_info):
    box2 = []
    for i in range(len(otcloser_info)):
        date = otcloser_info[i][0].replace("/", "-")
        stock_number = otcloser_info[i][1]
        stock_name = otcloser_info[i][2]
        sector = otcloser_info[i][3]
        close_price = otcloser_info[i][4]
        high_and_low = otcloser_info[i][5]
        width_of_high = otcloser_info[i][6]
        amplitude = otcloser_info[i][7]
        volume = otcloser_info[i][8].replace(",", "")

        box2.append((date, stock_number, stock_name, sector,
                    close_price, high_and_low, width_of_high,
                    amplitude, volume))

    return box2


# real_data_get4 = data_crawling_extract(otcloser_info)


def listwinner_data_insert(real_data_get1):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("AWS_Host"),
                           port=int(os.getenv("AWS_Port")),
                           user=os.getenv("AWS_User"),
                           passwd=os.getenv("AWS_Pass"),
                           db=os.getenv("AWS_DB"),
                           charset=os.getenv("AWS_Charset"))
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(real_data_get1)):
        sql = "insert into %s\
                    (date, stock_number, stock_name, sector, close_price,\
                    high_and_low, width_of_high, amplitude, volume)\
                    values('%s', %s, '%s', '%s', %s, '%s', %s, %s, %s)"\
                    % (os.getenv("table_d"), real_data_get1[i][0], real_data_get1[i][1],
                       real_data_get1[i][2], real_data_get1[i][3], real_data_get1[i][4],
                       real_data_get1[i][5], real_data_get1[i][6], real_data_get1[i][7],
                       real_data_get1[i][8])
        try:
            cursor.execute(sql)
            conn.commit()
            print("listwinner_info successfully inserted.")
        except:
            print("listwinner_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


"""
Insert renew data into MySQL table from withdrawal
"""

mysql_data_insert1 = listwinner_data_insert(real_data_get1)


def listloser_data_insert(real_data_get2):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("AWS_Host"),
                           port=int(os.getenv("AWS_Port")),
                           user=os.getenv("AWS_User"),
                           passwd=os.getenv("AWS_Pass"),
                           db=os.getenv("AWS_DB"),
                           charset=os.getenv("AWS_Charset"))
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(real_data_get2)):
        sql = "insert into %s\
                    (date, stock_number, stock_name, sector, close_price,\
                    high_and_low, width_of_high, amplitude, volume)\
                    values('%s', %s, '%s', '%s', %s, '%s', %s, %s, %s)"\
                    % (os.getenv("table_e"), real_data_get2[i][0], real_data_get2[i][1],
                       real_data_get2[i][2], real_data_get2[i][3], real_data_get2[i][4],
                       real_data_get2[i][5], real_data_get2[i][6], real_data_get2[i][7],
                       real_data_get2[i][8])
        try:
            cursor.execute(sql)
            conn.commit()
            print("listloser_info successfully inserted.")
        except:
            print("listloser_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


# mysql_data_insert2 = listloser_data_insert(real_data_get2)


def otcwinner_data_insert(real_data_get3):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("AWS_Host"),
                           port=int(os.getenv("AWS_Port")),
                           user=os.getenv("AWS_User"),
                           passwd=os.getenv("AWS_Pass"),
                           db=os.getenv("AWS_DB"),
                           charset=os.getenv("AWS_Charset"))
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(real_data_get3)):
        sql = "insert into %s\
                    (date, stock_number, stock_name, sector, close_price,\
                    high_and_low, width_of_high, amplitude, volume)\
                    values('%s', %s, '%s', '%s', %s, '%s', %s, %s, %s)"\
                    % (os.getenv("table_f"), real_data_get3[i][0], real_data_get3[i][1],
                       real_data_get3[i][2], real_data_get3[i][3], real_data_get3[i][4],
                       real_data_get3[i][5], real_data_get3[i][6], real_data_get3[i][7],
                       real_data_get3[i][8])
        try:
            cursor.execute(sql)
            conn.commit()
            print("otcwinner_info successfully inserted.")
        except:
            print("otcwinner_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


# mysql_data_insert3 = otcwinner_data_insert(real_data_get3)


def otcloser_data_insert(real_data_get4):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("AWS_Host"),
                           port=int(os.getenv("AWS_Port")),
                           user=os.getenv("AWS_User"),
                           passwd=os.getenv("AWS_Pass"),
                           db=os.getenv("AWS_DB"),
                           charset=os.getenv("AWS_Charset"))
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(real_data_get4)):
        sql = "insert into %s\
                    (date, stock_number, stock_name, sector, close_price,\
                    high_and_low, width_of_high, amplitude, volume)\
                    values('%s', %s, '%s', '%s', %s, '%s', %s, %s, %s)"\
                    % (os.getenv("table_g"), real_data_get4[i][0], real_data_get4[i][1],
                       real_data_get4[i][2], real_data_get4[i][3], real_data_get4[i][4],
                       real_data_get4[i][5], real_data_get4[i][6], real_data_get4[i][7],
                       real_data_get4[i][8])
        try:
            cursor.execute(sql)
            conn.commit()
            print("otcloser_info successfully inserted.")
        except:
            print("otcloser_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


# mysql_data_insert4 = otcloser_data_insert(real_data_get4)


run_listwinner.close()
# run_listloser.close()
# run_otcwinner.close()
# run_otcloser.close()
