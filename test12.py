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

rows = cursor.execute(
    "SELECT * FROM trader_info.sector_of_liststock_high ")
# rows = cursor.fetchmany(15)
rows = cursor.fetchall()
# print(rows)

box = []
sector = []
sector_categories = []
high = []
for i in range(len(rows)):
    temp = []
    for j in range(len(rows[i])):
        temp.append(rows[i][j])
    box.append(temp)

    sector.append(box[i][4])
    # high digit transform
    high.append(float(box[i][6].replace("▲", "")))

# for plot: sector categories count
for k in range(30):
    item = sector[k]
    if sector[k] not in sector_categories:
        sector_categories.append(sector[k])
    else:
        pass

# print(sector_categories)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def data1():
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='1qaz2wsx', db='trader_info', charset='utf8')

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM trader_info.sector_of_liststock_high where date = 20210426 ")
    rows = cursor.fetchmany(10)

    # print(rows)

    box1 = []
    sector1 = []
    # sector_categories = []
    high1 = []
    hub1 = {}
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box1.append(temp)

        sector1.append(box[i][4])
        # high digit transform
        high1.append(float(box[i][6].replace("▲", "")))

    data1 = []
    for l in range(len(sector1)):
        if sector[l] not in hub1:
            hub1[sector1[l]] = {}
            hub1[sector1[l]]["Total"] = round(high1[l], 2)
            hub1[sector1[l]]["count"] = 1
        else:
            hub1[sector1[l]]["Total"] += round(high1[l], 2)
            hub1[sector1[l]]["count"] += 1
            # digit control
        a = hub1[sector1[l]]["Total"] / hub1[sector[l]]["count"]
        real = round(a, 2)
        hub1[sector[l]]["Ave"] = real

    for r in range(len(sector_categories)):
        if sector_categories[r] not in hub1:
            hub1[sector_categories[r]] = {}
            hub1[sector_categories[r]]["Total"] = 0
            hub1[sector_categories[r]]["count"] = 0
            hub1[sector_categories[r]]["Ave"] = 0

    keysList = list(hub1.keys())
    valuesList = list(hub1.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub1[index]["Ave"]

        data1.append(b)
    return hub1, data1


val = data1()
# hub1
# print(val[0])
# # data1
# print(val[1])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def data2():
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='1qaz2wsx', db='trader_info', charset='utf8')

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM trader_info.sector_of_liststock_high where date = 20210427")
    rows = cursor.fetchmany(10)

    # print(rows)

    box2 = []
    sector2 = []
    # sector_categories = []
    high2 = []
    hub2 = {}
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box2.append(temp)

        sector2.append(box2[i][4])
        # high digit transform
        high2.append(float(box2[i][6].replace("▲", "")))

    data2 = []
    for l in range(len(sector2)):
        if sector2[l] not in hub2:
            hub2[sector2[l]] = {}
            hub2[sector2[l]]["Total"] = round(high2[l], 2)
            hub2[sector2[l]]["count"] = 1
        else:
            hub2[sector2[l]]["Total"] += round(high2[l], 2)
            hub2[sector2[l]]["count"] += 1
            # digit control
        a = hub2[sector2[l]]["Total"] / hub2[sector2[l]]["count"]
        real = round(a, 2)
        hub2[sector2[l]]["Ave"] = real

    for r in range(len(sector_categories)):
        if sector_categories[r] not in hub2:
            hub2[sector_categories[r]] = {}
            hub2[sector_categories[r]]["Total"] = 0
            hub2[sector_categories[r]]["count"] = 0
            hub2[sector_categories[r]]["Ave"] = 0

    keysList = list(hub2.keys())
    valuesList = list(hub2.values())
    # print(hub1)

    for y in range(len(keysList)):
        index = keysList[y]
        b = hub2[index]["Ave"]

        data2.append(b)

    return hub2, data2


val2 = data2()
# hub2
# print(val2[0])
# data2
# print(val2[1])


def data3():
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='1qaz2wsx', db='trader_info', charset='utf8')

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM trader_info.sector_of_liststock_high where date = 20210428")
    rows = cursor.fetchmany(10)

    # print(rows)

    box3 = []
    sector3 = []
    # sector_categories = []
    high3 = []
    hub3 = {}
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box3.append(temp)

        sector3.append(box3[i][4])
        # high digit transform
        high3.append(float(box3[i][6].replace("▲", "")))

    data3 = []
    for l in range(len(sector3)):
        if sector3[l] not in hub3:
            hub3[sector3[l]] = {}
            hub3[sector3[l]]["Total"] = round(high3[l], 2)
            hub3[sector3[l]]["count"] = 1
        else:
            hub3[sector3[l]]["Total"] += round(high3[l], 2)
            hub3[sector3[l]]["count"] += 1
            # digit control
        a = hub3[sector3[l]]["Total"] / hub3[sector3[l]]["count"]
        real = round(a, 2)
        hub3[sector3[l]]["Ave"] = real
    for r in range(len(sector_categories)):
        if sector_categories[r] not in hub3:
            hub3[sector_categories[r]] = {}
            hub3[sector_categories[r]]["Total"] = 0
            hub3[sector_categories[r]]["count"] = 0
            hub3[sector_categories[r]]["Ave"] = 0

    keysList = list(hub3.keys())
    valuesList = list(hub3.values())
    # print(hub1)

    for z in range(len(keysList)):
        index = keysList[z]
        b = hub3[index]["Ave"]

        data3.append(b)

    return hub3, data3


val3 = data3()
# hub3
# print(data3[0])
# data3
# print(val3[1])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Plot
output_file("liststock_high_group_by_sector.html")

sector = sector_categories


date = ['20210426', '20210427', '20210428']


width_of_high = {'sector': sector_categories,
                 '20210426': val[1],
                 '20210427': val2[1],
                 '20210428': val3[1]}
source = ColumnDataSource(data=width_of_high)

p = figure(x_range=sector, y_range=(0, 50), plot_height=250, title="Sector of Liststock High",
           sizing_mode="scale_width")

p.vbar(x=dodge('sector', -0.25, range=p.x_range), top='20210426', width=0.2, source=source,
       color="#c9d9d3", legend_label="20210426")

p.vbar(x=dodge('sector',  0.0,  range=p.x_range), top='20210427', width=0.2, source=source,
       color="#718dbf", legend_label="20210427")

p.vbar(x=dodge('sector',  0.25, range=p.x_range), top='20210428', width=0.2, source=source,
       color="#e84d60", legend_label="20210428")


p.x_range.range_padding = 0.05
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
