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


def market_bargainingchip():
    # 證交所網站
    # driver = webdriver.Chrome('D:\\timothyTest\data_crawler\chromedriver')
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
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 切換至期交所網站
    driver.get('https://www.taifex.com.tw/cht/3/futContractsDate')
    time.sleep(2)
    # 選擇外資成本日期
    button1 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button1.click()
    time.sleep(2)
    button2 = driver.find_element_by_link_text("18")
    button2.click()
    time.sleep(2)
    button3 = driver.find_element_by_css_selector("#button")
    button3.click()
    time.sleep(2)
    # driver.close()

    # 外資當日成本
    money = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(13) > div:nth-child(1)")
    money1 = money.text
    # print(money1)
    position = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1) > font")
    position1 = position.text
    # print(position1)
    truemoney = money1.replace(",", "")
    trueposition = position1.replace(",", "")
    trueposition = round(int(truemoney)/int(trueposition)/200*1000, 2)
    # print(trueposition)
    temp.append(trueposition)
    # print(temp)

    # 外資前一天成本
    # 選擇日期
    button_1 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button_1.click()
    time.sleep(2)
    button_2 = driver.find_element_by_link_text("17")
    button_2.click()
    time.sleep(2)
    button_3 = driver.find_element_by_css_selector("#button")
    button_3.click()
    time.sleep(2)
    previousone_money = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(13) > div:nth-child(1)")
    previousone_money1 = previousone_money.text

    previousone_position = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1) > font")
    previousone_position1 = previousone_position.text

    previousone_truemoney = previousone_money1.replace(",", "")
    previousone_trueposition = previousone_position1.replace(",", "")
    previousone_trueposition = round(
        int(previousone_truemoney)/int(previousone_trueposition)/200*1000, 2)
    # print(previousone_trueposition)

    # 外資前兩天成本
    # 選擇日期
    button1 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button1.click()
    time.sleep(2)
    button2 = driver.find_element_by_link_text("14")
    button2.click()
    time.sleep(2)
    button3 = driver.find_element_by_css_selector("#button")
    button3.click()
    time.sleep(2)
    previoustwo_money = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(13) > div:nth-child(1)")
    previoustwo_money1 = previoustwo_money.text

    previoustwo_position = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1) > font")
    previoustwo_position1 = previoustwo_position.text

    previoustwo_truemoney = previoustwo_money1.replace(",", "")
    previoustwo_trueposition = previoustwo_position1.replace(",", "")
    previoustwo_trueposition = round(
        int(previoustwo_truemoney)/int(previoustwo_trueposition)/200*1000, 2)
    # print(previoustwo_trueposition)

    foreign_average_cost = round((
        trueposition+previousone_trueposition+previoustwo_trueposition)/3, 2)
    # print(foreign_average_cost)
    temp.append(foreign_average_cost)
    # print(temp)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 介面切換至期貨大額交易人
    button4 = driver.find_element_by_css_selector("#id_03_03000000_1 > a")
    button4.click()
    time.sleep(2)
    button5 = driver.find_element_by_css_selector("#id_03_03010000_1 > a")
    button5.click()
    time.sleep(2)
    button6 = driver.find_element_by_css_selector("#id_03_03010100_1 > a")
    button6.click()
    time.sleep(2)
    # 選擇日期
    button7 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button > img")
    button7.click()
    time.sleep(2)
    button8 = driver.find_element_by_link_text("18")
    button8.click()
    time.sleep(2)
    button9 = driver.find_element_by_css_selector("#submitButton")
    button9.click()
    time.sleep(2)

    # 10 big_legalperson買方部位
    e = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(3) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(4) > div")
    g = e.text

    a = ''
    buyposition = ''
    for i in g:
        if i == '(':
            break
        else:
            a = ''.join(i)
            buyposition += a

    buyposition1 = buyposition.replace("\n", "")
    buyposition2 = buyposition1.replace(",", "")
    # print(buyposition1)
    # temp.append(buyposition1)
    # print(temp)

    # 10_big_legalperson賣方部位
    f = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(3) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(8) > div")
    h = f.text
    s = ''
    sellposition = ''
    for j in h:
        if j == '(':
            break
        else:
            s = ''.join(j)
            sellposition += s

    sellposition1 = sellposition.replace("\n", "")
    sellposition2 = sellposition1.replace(",", "")
    # print(sellposition1)
    # temp.append(sellposition1)
    # print(temp)
    big_legalperson_trueposition = int(buyposition2) - int(sellposition2)

    temp.append(big_legalperson_trueposition)
    # print(temp)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 介面切換至三大法人計算散戶期貨籌碼
    driver.get('https://www.taifex.com.tw/cht/3/futContractsDate')
    time.sleep(2)
    # 選擇日期
    button10 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button10.click()
    time.sleep(2)
    button11 = driver.find_element_by_link_text("18")
    button11.click()
    time.sleep(2)
    button12 = driver.find_element_by_css_selector("#button")
    button12.click()
    time.sleep(2)
    # 散戶大台
    m = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td:nth-child(14) > div:nth-child(1) > font")
    m1 = m.text
    m2 = m1.replace(",", "")
    n = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(12) > div:nth-child(1) > font")
    n1 = n.text
    n2 = n1.replace(",", "")
    o = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(12) > div:nth-child(1)")
    o1 = o.text
    o2 = o1.replace(",", "")

    retailTX = -(int(m2)+int(n2)+int(o2))
    temp.append(retailTX)
    # print(temp)

    # 散戶小台
    p = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(13) > td:nth-child(14) > div:nth-child(1) > font")
    p1 = p.text
    p2 = p1.replace(",", "")
    q = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(14) > td:nth-child(12) > div:nth-child(1)")
    q1 = q.text
    q2 = q1.replace(",", "")
    r = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(15) > td:nth-child(12) > div:nth-child(1) > font")
    r1 = r.text
    r2 = r1.replace(",", "")

    retailMTX = -(int(p2)+int(q2)+int(r2))
    temp.append(retailMTX)
    # print(temp)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 散戶option(當日未平倉 - 前一日未平倉)
    # 先計算前一日，選定前一日日期
    s = driver.get("https://www.taifex.com.tw/cht/3/callsAndPutsDate")
    time.sleep(2)
    button13 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button13.click()
    time.sleep(2)
    button14 = driver.find_element_by_link_text("17")
    button14.click()
    time.sleep(2)
    button15 = driver.find_element_by_css_selector("#button")
    button15.click()
    time.sleep(2)
    # 先算前一日散戶sc未平倉
    s = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td:nth-child(11) > font")
    s1 = s.text
    s2 = s1.replace(",", "")
    t = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(8) > font")
    t1 = t.text
    t2 = t1.replace(",", "")
    u = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(8) > font")
    u1 = u.text
    u2 = u1.replace(",", "")
    previoussc = int(s2)+int(t2)+int(u2)
    # print(previoussc)

    # 前一日散戶bc未平倉
    v = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td:nth-child(13) > font")
    v1 = v.text
    v2 = v1.replace(",", "")
    w = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(10) > font")
    w1 = w.text
    w2 = w1.replace(",", "")
    x = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(10) > font")
    x1 = x.text
    x2 = x1.replace(",", "")
    previousbc = int(v2)+int(w2)+int(x2)
    # print(previousbc)

    # 前一日散戶sp未平倉
    h = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(7) > td:nth-child(9) > font")
    h1 = h.text
    h2 = h1.replace(",", "")
    i = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(8) > td:nth-child(8) > font")
    i1 = i.text
    i2 = i1.replace(",", "")
    j = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(9) > td:nth-child(8) > font")
    j1 = j.text
    j2 = j1.replace(",", "")
    previoussp = int(h2)+int(i2)+int(j2)
    # print(previoussp)

    # 前一日散戶bp未平倉
    e = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(7) > td:nth-child(11) > font")
    e1 = e.text
    e2 = e1.replace(",", "")
    f = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(8) > td:nth-child(10) > font")
    f1 = f.text
    f2 = f1.replace(",", "")
    g = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(9) > td:nth-child(10) > font")
    g1 = g.text
    g2 = g1.replace(",", "")
    previousbp = int(e2)+int(f2)+int(g2)
    # print(previousbp)

    # 選定當日日期
    button16 = driver.find_element_by_css_selector(
        "#uForm > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > button")
    button16.click()
    time.sleep(2)
    button17 = driver.find_element_by_link_text("18")
    button17.click()
    time.sleep(2)
    button18 = driver.find_element_by_css_selector("#button")
    button18.click()
    time.sleep(2)

    # 當日散戶sc未平倉
    ss = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td:nth-child(11) > font")
    ss1 = ss.text
    ss2 = ss1.replace(",", "")
    tt = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(8) > font")
    tt1 = tt.text
    tt2 = tt1.replace(",", "")
    uu = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(8) > font")
    uu1 = uu.text
    uu2 = uu1.replace(",", "")
    currentsc = int(ss2)+int(tt2)+int(uu2)
    # print(currentsc)

    # 當日散戶bc未平倉
    vv = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(4) > td:nth-child(13) > font")
    vv1 = vv.text
    vv2 = vv1.replace(",", "")
    ww = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td:nth-child(10) > font")
    ww1 = ww.text
    ww2 = ww1.replace(",", "")
    xx = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td:nth-child(10) > font")
    xx1 = xx.text
    xx2 = xx1.replace(",", "")
    currentbc = int(vv2)+int(ww2)+int(xx2)
    # print(currentbc)

    # 當日散戶sp未平倉
    hh = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(7) > td:nth-child(9) > font")
    hh1 = hh.text
    hh2 = hh1.replace(",", "")
    ii = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(8) > td:nth-child(8) > font")
    ii1 = ii.text
    ii2 = ii1.replace(",", "")
    jj = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(9) > td:nth-child(8) > font")
    jj1 = jj.text
    jj2 = jj1.replace(",", "")
    currentsp = int(hh2)+int(ii2)+int(jj2)
    # print(currentsp)

    #  當日散戶bp未平倉
    ee = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(7) > td:nth-child(11) > font")
    ee1 = ee.text
    ee2 = ee1.replace(",", "")
    ff = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(8) > td:nth-child(10) > font")
    ff1 = ff.text
    ff2 = ff1.replace(",", "")
    gg = driver.find_element_by_css_selector(
        "#printhere > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(9) > td:nth-child(10) > font")
    gg1 = gg.text
    gg2 = gg1.replace(",", "")
    currentbp = int(ee2)+int(ff2)+int(gg2)
    # print(currentbp)

    # 散戶sc-bc
    retailscbc = (currentsc-previoussc)-(currentbc-previousbc)
    # print(retailscbc)
    # 散戶sp-bp
    retailspbp = (currentsp-previoussp)-(currentbp-previousbp)
    # print(retailspbp)
    # 散戶sc
    retailsc = retailscbc - retailspbp
    # print(retailsc)

    temp.append(retailsc)
    box.append(temp)
    return box


"""
Remembered to adjust the date below:

1. foreign_average_cost, adjust to currentdate first and then the date of two days ago
2. option of bargaining chips for retail_sc : adjust to the date of one day ago first and then currentdate
3. other items: adjust to currentdate 

"""

a = market_bargainingchip()
print(a)


def insert_renewdata_into_database(a):
    # 建立連線
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset")
                           )

    # 建立操作遊標, 查詢資料預設為元組型別
    cursor = conn.cursor()
    for i in range(len(a)):
        sql = "insert into %s\
                    (date, market_close_price, foreign_capital_cost, foreign_capital_average_cost, 10_biglegalperson_variety, retail_TX, retail_MTX, retail_sc)\
                    values('%s', %s, '%s', '%s', '%s', '%s', '%s', '%s')"\
                    % (os.getenv("table_a"), a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7])
        try:
            cursor.execute(sql)
            conn.commit()
            print("market_bargainingchip successfully inserted.")
        except:
            print("market_bargainingchip update failed!")
            conn.rollback()

    # 關閉遊標
    cursor.close()
    # 關閉連線
    conn.close()


b = insert_renewdata_into_database(a)
driver.close()
