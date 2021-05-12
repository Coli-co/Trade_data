from optioncrawling import choose_date, option_callitem_crawling, win_close
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome('D:\\timothyTest\data_crawler\chromedriver')
# driver.get('https://www.taifex.com.tw/cht/3/optDailyMarketSummary')
# time.sleep(2)


if __name__ == '__main__':
    choose_date()
    call_rawdata = option_callitem_crawling()
    print(call_rawdata)
    win_close()


# driver.close()
