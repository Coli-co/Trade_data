from selenium import webdriver
import time
from bs4 import BeautifulSoup
# 注意：使用Keys方法要先引入以下這一行
from selenium.webdriver.common.keys import Keys
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


def get_page():
    driver = webdriver.Chrome('D:\\timothyTest\data_crawler\chromedriver')
    driver.get('https://www.taifex.com.tw/cht/3/optDailyMarketSummary')

    return driver


run_option = get_page()


def choose_date(run_option):
    time.sleep(2)
    # 開啟日歷
    button = run_option.find_element_by_css_selector(
        "#myform > table > tbody > tr:nth-child(1) > td:nth-child(2) > button > img")
    button.click()
    time.sleep(2)
    # 調整月份
    # 上月
    # button0 = driver.find_element_by_css_selector(
    #     "#ui-datepicker-div > div > a.ui-datepicker-prev.ui-corner-all")
    # button0.click()
    # time.sleep(2)
    # 下月
    # but = driver.find_element_by_css_selector(
    #     "#ui-datepicker-div > div > a.ui-datepicker-next.ui-corner-all")
    # but.click()
    # time.sleep(2)
    # 選擇日期
    button1 = run_option.find_element_by_link_text("13")
    button1.click()
    time.sleep(2)
    # 選擇交易時段 (一般交易時段:value = 0 盤後:value =1)
    button2 = run_option.find_element_by_css_selector(
        "td[align ='left'] select[id ='MarketCode'] option[value ='0']")
    button2.click()
    time.sleep(2)
    # 送出查詢
    button3 = run_option.find_element_by_css_selector("input[type='button']")
    button3.click()
    time.sleep(2)


"""adjust date of option daily trade website """

choose_date(run_option)


def option_callitem_crawling(run_option):
    time.sleep(2)
    box = []
    # 日期資料
    for o in range(2, 32):
        temp = []
        p = run_option.find_element_by_css_selector(
            '#printhere > div:nth-child(3) > p.clearfix > span.right')
        date = p.text
        temp.append(date)
        # print(temp)
    # 買權
        for i in range(o, o+1):
            # temp = []
            a = run_option.find_element_by_css_selector(
                "#printhere > div:nth-child(3) > table:nth-child(3) > tbody > tr:nth-child(2) > td > table > caption")
            call = a.text
            temp.append(call)
    # 項目欄位
            # for j in range(i, i+1):
            #     b = "#printhere > div:nth-child(3) > table:nth-child(3) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(%s)" % j
            #     b1 = run_option.find_elements_by_css_selector(b)
    # 到期月份
            for k in range(o, o+1):
                c = "#printhere > div:nth-child(3) > table:nth-child(3) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(%s) > td:nth-child(1)" % (o)
                c1 = run_option.find_element_by_css_selector(c)
                expire = c1.text
                temp.append(expire)
    # 履約價格: Strike Price
                for l in range(k, k+1):
                    d = "#printhere > div:nth-child(3) > table:nth-child(3) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(%s) > td:nth-child(2)" % (o)
                    d1 = run_option.find_element_by_css_selector(d)
                    sp = d1.text
                    temp.append(sp)
    # 未平倉量: Open Interest
                    for m in range(l, l+1):
                        e = "#printhere > div:nth-child(3) > table:nth-child(3) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(%s) > td:nth-child(9)" % (
                            o)
                        e1 = run_option.find_element_by_css_selector(e)
                        oi = e1.text
                        temp.append(oi)
                        box.append(temp)
    return box
    # print(temp)

    print(box)


"""adjust number of option_call items """

call_rawdata = option_callitem_crawling(run_option)


def data_crawling_extract(call_rawdata):
    box2 = []
    for i in range(len(call_rawdata)):
        date = call_rawdata[i][0].replace("/", "-")
        realdate = date.replace("日期:", "")
        call_or_put = call_rawdata[i][1]
        expire_date = call_rawdata[i][2]
        strike_place = call_rawdata[i][3]
        open_interest = call_rawdata[i][4]

        box2.append((realdate, call_or_put, expire_date, strike_place,
                    open_interest))
        # print(box2)

    return box2


call_realdata = data_crawling_extract(call_rawdata)


def mysql_renewdata_insert(call_realdata):

    # 建立連線
    conn = pymysql.connect(host=os.getenv("AWS_Host"),
                           port=int(os.getenv("AWS_Port")),
                           user=os.getenv("AWS_User"),
                           passwd=os.getenv("AWS_Pass"),
                           db=os.getenv("AWS_DB"),
                           charset=os.getenv("AWS_Charset"))
    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(call_realdata)):
        sql = "insert into %s\
            (date, call_or_put, expire_date, strike_price, open_interest)\
            values('%s', '%s', '%s', %s, %s)"\
            % (os.getenv("table_b"), call_realdata[i][0], call_realdata[i][1], call_realdata[i][2],
               call_realdata[i][3], call_realdata[i][4])

        try:
            cursor.execute(sql)
            conn.commit()
            print("call_info successfully inserted.")
        except:
            print("call_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


mysql_renewdata_insert(call_realdata)
run_option.close()


def option_put_item_crawling(run_option):
    time.sleep(2)
    box1 = []
    # 日期資料
    for o in range(2, 32):
        temp = []
        p = run_option.find_element_by_css_selector(
            '#printhere > div:nth-child(3) > p.clearfix > span.right')
        date = p.text
        temp.append(date)
        # print(temp)
    # printhere > div:nth-child(3) > table:nth-child(4) > tbody > tr > td > table > caption
    # 賣權
        for i in range(o, o+1):
            a = run_option.find_element_by_css_selector(
                "#printhere > div:nth-child(3) > table:nth-child(4) > tbody > tr > td > table > caption")
            put = a.text
            temp.append(put)
    # 項目欄位(第2欄位算起)
            # for j in range(i, i+1):
            #     b = "#printhere > div:nth-child(3) > table:nth-child(4) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(%s)" % (j)
            #     b1 = run_option.find_elements_by_css_selector(b)
    # 到期月份 (每一欄位中的第2個項目)
            for k in range(o, o+1):
                c = "#printhere > div:nth-child(3) > table:nth-child(4) > tbody > tr > td > table > tbody:nth-child(3) > tr:nth-child(%s) > td:nth-child(1)" % (o)
                c1 = run_option.find_element_by_css_selector(c)
                expire = c1.text
                temp.append(expire)
            # print(temp)
    # 履約價格: Strike Price
                for l in range(k, k+1):
                    d = "#printhere > div:nth-child(3) > table:nth-child(4) > tbody > tr > td > table > tbody:nth-child(3) > tr:nth-child(%s) > td:nth-child(2)" % (o)
                    d1 = run_option.find_element_by_css_selector(d)
                    strike_price = d1.text
                    temp.append(strike_price)
    # 未平倉量: Open Interest
                    for m in range(l, l+1):
                        e = "#printhere > div:nth-child(3) > table:nth-child(4) > tbody > tr > td > table > tbody:nth-child(3) > tr:nth-child(%s) > td:nth-child(9)"\
                            % (o)
                        e1 = run_option.find_element_by_css_selector(e)
                        open_interest = e1.text
                        temp.append(open_interest)
                        box1.append(temp)

    return box1
    # print(temp)

    # print(box1)


"""adjust number of option_put items """

# put_rawdata = option_put_item_crawling(run_option)


def data_crawling_extract(put_rawdata):

    box2 = []
    for i in range(len(put_rawdata)):
        date = put_rawdata[i][0].replace("/", "-")
        realdate = date.replace("日期:", "")
        call_or_put = put_rawdata[i][1]
        expire_date = put_rawdata[i][2]
        strike_place = put_rawdata[i][3]
        open_interest = put_rawdata[i][4]

        box2.append((realdate, call_or_put, expire_date, strike_place,
                    open_interest))
        # print(box2)

    return box2


# put_realdata = data_crawling_extract(put_rawdata)


def mysql_renewdata_insert(put_realdata):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("AWS_Host"),
                           port=int(os.getenv("AWS_Port")),
                           user=os.getenv("AWS_User"),
                           passwd=os.getenv("AWS_Pass"),
                           db=os.getenv("AWS_DB"),
                           charset=os.getenv("AWS_Charset"))

    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(put_realdata)):
        sql = "insert into %s\
                    (date, call_or_put, expire_date, strike_price, open_interest)\
                    values('%s', '%s', '%s', %s, %s)"\
                    % (os.getenv("table_c"), put_realdata[i][0], put_realdata[i][1],
                       put_realdata[i][2], put_realdata[i][3], put_realdata[i][4])
        try:
            cursor.execute(sql)
            conn.commit()
            print("put_info successfully inserted.")
        except:
            print("put_info update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


# mysql_renewdata_insert(put_realdata)
# run_option.close()
