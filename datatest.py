from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import dodge
from bokeh.palettes import GnBu3, OrRd3
import pymysql


# Connect to MySQL Database
conn = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='1qaz2wsx', db='trader_info', charset='utf8')

cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM trader_info.sector_of_liststock_high")
rows = cursor.fetchmany(10)
# print(rows)

box = []
sector = []
sector_categories = []
high = []
highcalc = []

for i in range(len(rows)):
    temp = []
    for j in range(len(rows[i])):
        temp.append(rows[i][j])
    box.append(temp)
    sector.append(box[i][4])
# print(sector)
# high digit transform
    high.append(float(box[i][6].replace("▲", "")))
# print(high)


# sector categories count
for k in range(10):
    item = sector[k]
    if sector[k] not in sector_categories:
        sector_categories.append(sector[k])
    else:
        pass
    # print(sector_categories)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
for l in range(len(high)):
    if sector[l] in sector_categories:
        # highcalc.append(high[l])
        # a = sector.count(sector[l])
        sector[l] = 1
        print(sector[l])
        if sector[l] in sector:
            sector[l] += 1
        print(sector[l])

    #     print(sector)
    # print(a)
    #     high[l] += high[l]
    #     b = high[l]/sector[l]
    # print(b)
    #     b = high[l]/a
    #     highcalc.append(b)
    # print(b)
    # print(highcalc)
    # print(a)
    # if sector[l]

    # print(a)
    # if box[i][4] in sector_categories:
    #     a += 1
    #     print(a)

# print(sector_categories)


output_file("liststock_high_group_by_sector.html")

sector = ['電零組', '電腦週邊', '電機', '電器電纜', '鋼鐵', '通信網路',
          '航運', '紡織', '玻璃', '橡膠', '半導體', '其它電子', '食品',
          '化學', '貿易百貨', '光電', '營建']
date = ['20210426', '20210427', '20210428']

width_of_high = {'sector': sector,
                 '20210426': [2.25, 0, 3.95, 0, 0, 0, 5.43, 0, 0, 33.00, 2.23, 6.25, 0, 0, 0, 0, 0],
                 '20210427': [1.30, 2.45, 0, 2.00, 5.10, 1.40, 3.85, 4.70, 1.55, 0, 21.15, 0, 0, 0, 0, 0, 0],
                 '20210428': [3.15, 0, 0, 0, 0, 4.25, 0, 3.25, 1.45, 0, 46.00, 1.95,  15.00, 1.15, 0, 0, 0]}
# source = ColumnDataSource(data=width_of_high)


# p = figure(x_range=sector, y_range=(0, 50), plot_height=250, title="Sector of Liststock High",
#            sizing_mode="scale_width")

# p.vbar(x=dodge('sector', -0.25, range=p.x_range), top='20210426', width=0.2, source=source,
#        color="#c9d9d3", legend_label="20210426")

# p.vbar(x=dodge('sector',  0.0,  range=p.x_range), top='20210427', width=0.2, source=source,
#        color="#718dbf", legend_label="20210427")

# p.vbar(x=dodge('sector',  0.25, range=p.x_range), top='20210428', width=0.2, source=source,
#        color="#e84d60", legend_label="20210428")

# p.x_range.range_padding = 0.01
# p.xgrid.grid_line_color = None
# p.legend.location = "top_left"
# p.legend.orientation = "horizontal"

# show(p)
