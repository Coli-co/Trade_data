from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
# from bokeh.transform import dodge
from bokeh.palettes import GnBu3, OrRd3
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to MySQL Database
conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                       passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

cursor = conn.cursor()

rows = cursor.execute(
    "SELECT * FROM %s.%s "
    % (os.getenv("mysql_db"), os.getenv("table_e")))
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
    high.append(float(box[i][6].replace("▼", "")))

# for plot: sector categories count
for k in range(50):
    item = sector[k]
    if sector[k] not in sector_categories:
        sector_categories.append(sector[k])
    else:
        pass

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def high_data1():
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210426 "
        % (os.getenv("mysql_db"), os.getenv("table_d")))
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

        sector1.append(box1[i][4])
        # high digit transform
        high1.append(float(box1[i][6].replace("▲", "")))

    data1 = []
    for l in range(len(sector1)):
        if sector1[l] not in hub1:
            hub1[sector1[l]] = {}
            hub1[sector1[l]]["Total"] = round(high1[l], 2)
            hub1[sector1[l]]["count"] = 1
        else:
            hub1[sector1[l]]["Total"] += round(high1[l], 2)
            hub1[sector1[l]]["count"] += 1
            # digit control
        a = hub1[sector1[l]]["Total"] / hub1[sector1[l]]["count"]
        real = round(a, 2)
        hub1[sector1[l]]["Ave"] = real

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
    # del data1[15:]
    # print(data1)
    return hub1, data1


# 16
# high_data1()
val = high_data1()
# hub1
# print(val[0])
# # data1
# print("highdata1 is ")
# print(val[1])
# print()
# del val[1][15:]
# print("deleting highdata1 is")
# print(val[1])

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def high_data2():
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210427"
        % (os.getenv("mysql_db"), os.getenv("table_d")))
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
    # del data2[15:]

    return hub2, data2
# 18


val2 = high_data2()
# hub2
# print(val2[0])
# data2
# print("highdata2 is ")
# print(val2[1])
# print()
# print("deleting highdata2 is")
# del val2[1][15:]
# print(val2[1])
# print()


def high_data3():
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210428"
        % (os.getenv("mysql_db"), os.getenv("table_d")))
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
    # del data3[15:]
    return hub3, data3
# 18


val3 = high_data3()
# hub3
# print(val3[0])
# data3
# print("highdata3 is ")
# print(val3[1])
# print()
# print("deleting highdata3 is")
# del val3[1][15:]
# print(val3[1])


def low_data1():
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210426 "
        % (os.getenv("mysql_db"), os.getenv("table_e")))
    rows = cursor.fetchmany(10)

    # print(rows)

    box4 = []
    sector4 = []
    # sector_categories = []
    high4 = []
    hub4 = {}
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box4.append(temp)

        sector4.append(box4[i][4])
        # high digit transform
        high4.append(float(box4[i][6].replace("▼", "")))

    data4 = []
    for l in range(len(sector4)):
        if sector4[l] not in hub4:
            hub4[sector4[l]] = {}
            hub4[sector4[l]]["Total"] = round(high4[l], 2)
            hub4[sector4[l]]["count"] = 1
        else:
            hub4[sector4[l]]["Total"] += round(high4[l], 2)
            hub4[sector4[l]]["count"] += 1
            # digit control
        a = hub4[sector4[l]]["Total"] / hub4[sector4[l]]["count"]
        real = round(a, 2)
        hub4[sector4[l]]["Ave"] = real

    for r in range(len(sector_categories)):
        if sector_categories[r] not in hub4:
            hub4[sector_categories[r]] = {}
            hub4[sector_categories[r]]["Total"] = 0
            hub4[sector_categories[r]]["count"] = 0
            hub4[sector_categories[r]]["Ave"] = 0

    keysList = list(hub4.keys())
    valuesList = list(hub4.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub4[index]["Ave"]

        data4.append(b)
    return hub4, data4
# 15


val4 = low_data1()
# hub4
# print(val4[0])
# # data4
# print("lowdata1 is ")
# print(val4[1])
# print()


def low_data2():
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210427 "
        % (os.getenv("mysql_db"), os.getenv("table_e")))
    rows = cursor.fetchmany(10)

    # print(rows)

    box5 = []
    sector5 = []
    # sector_categories = []
    high5 = []
    hub5 = {}
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box5.append(temp)

        sector5.append(box5[i][4])
        # high digit transform
        high5.append(float(box5[i][6].replace("▼", "")))

    data5 = []
    for l in range(len(sector5)):
        if sector5[l] not in hub5:
            hub5[sector5[l]] = {}
            hub5[sector5[l]]["Total"] = round(high5[l], 2)
            hub5[sector5[l]]["count"] = 1
        else:
            hub5[sector5[l]]["Total"] += round(high5[l], 2)
            hub5[sector5[l]]["count"] += 1
            # digit control
        a = hub5[sector5[l]]["Total"] / hub5[sector5[l]]["count"]
        real = round(a, 2)
        hub5[sector5[l]]["Ave"] = real

    for r in range(len(sector_categories)):
        if sector_categories[r] not in hub5:
            hub5[sector_categories[r]] = {}
            hub5[sector_categories[r]]["Total"] = 0
            hub5[sector_categories[r]]["count"] = 0
            hub5[sector_categories[r]]["Ave"] = 0

    keysList = list(hub5.keys())
    valuesList = list(hub5.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub5[index]["Ave"]

        data5.append(b)
    return hub5, data5
# 15


val5 = low_data2()
# hub5
# print(val5[0])
# # data5
# print("lowdata2 is ")
# print(val5[1])
# print()


def low_data3():
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset")
                           )

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210428 "
        % (os.getenv("mysql_db"), os.getenv("table_e")))
    rows = cursor.fetchmany(10)

    # print(rows)

    box6 = []
    sector6 = []
    # sector_categories = []
    high6 = []
    hub6 = {}
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box6.append(temp)

        sector6.append(box6[i][4])
        # high digit transform
        high6.append(float(box6[i][6].replace("▼", "")))

    data6 = []
    for l in range(len(sector6)):
        if sector6[l] not in hub6:
            hub6[sector6[l]] = {}
            hub6[sector6[l]]["Total"] = round(high6[l], 2)
            hub6[sector6[l]]["count"] = 1
        else:
            hub6[sector6[l]]["Total"] += round(high6[l], 2)
            hub6[sector6[l]]["count"] += 1
            # digit control
        a = hub6[sector6[l]]["Total"] / hub6[sector6[l]]["count"]
        real = round(a, 2)
        hub6[sector6[l]]["Ave"] = real

    for r in range(len(sector_categories)):
        if sector_categories[r] not in hub6:
            hub6[sector_categories[r]] = {}
            hub6[sector_categories[r]]["Total"] = 0
            hub6[sector_categories[r]]["count"] = 0
            hub6[sector_categories[r]]["Ave"] = 0

    keysList = list(hub6.keys())
    valuesList = list(hub6.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub6[index]["Ave"]

        data6.append(b)
    return hub6, data6
# 15


val6 = low_data3()
# hub1
# print(val6[0])
# # data1
# print("lowdata3 is ")
# print(val6[1])
# print()


# Plot

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def liststock_high_and_low_stack_bars_by_sector():
output_file("liststock_high_and_low_stack_barsby_sector.html")

sector = sector_categories
date = ['20210426', '20210427', '20210428']

high = {'sector': sector_categories,
        '20210426': val[1],
        '20210427': val2[1],
        '20210428': val3[1]}
low = {'sector': sector_categories,
       '20210426': val4[1],
       '20210427': val5[1],
       '20210428': val6[1]
       }
# p = figure(y_range=sector, plot_height=250, x_range=(-50, 50), title="Liststock high/low by sector",
#            toolbar_location=None)

p = figure(y_range=sector, plot_height=250, x_range=(-150, 100), title="Liststock high/low by sector",
           sizing_mode="scale_width")

p.hbar_stack(date, y='sector', height=0.9, color=GnBu3, source=ColumnDataSource(low),
             legend_label=["%s low" % x for x in date])

p.hbar_stack(date, y='sector', height=0.9, color=OrRd3, source=ColumnDataSource(high),
             legend_label=["%s high" % x for x in date])

p.y_range.range_padding = 0.05
p.ygrid.grid_line_color = None
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.title.text_font_size = "25px"
# p.title.text = "Title With Options"
# p.title.align = "right"
# p.title.text_color = "orange"
# p.title.text_font_size = "25px"
# p.title.background_fill_color = "#aaaaee"

# add extra titles with add_layout(...)
# from bokeh.models import Title
# p.add_layout(Title(text="Bottom Centered Title", align="center"), "below")


show(p)
