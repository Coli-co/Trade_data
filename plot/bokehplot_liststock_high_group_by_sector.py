from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import dodge
from bokeh.palettes import GnBu3, OrRd3
from bokeh.layouts import row, column, gridplot
import pymysql
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()


def sectories_count():
    # Connect to MySQL Database
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rowshigh = cursor.execute(
        "SELECT * FROM %s.%s "
        % (os.getenv("mysql_db"), os.getenv("table_d")))
    rowshigh = cursor.fetchall()
    # print(rows)

    rowslow = cursor.execute(
        "SELECT * FROM %s.%s "
        % (os.getenv("mysql_db"), os.getenv("table_e")))
    rowslow = cursor.fetchall()

    box_high = []
    box_low = []
    sector_high = []
    sector_low = []
    sector_categories = []
    high = []
    low = []
    for i in range(len(rowshigh)):
        temp = []
        for j in range(len(rowshigh[i])):
            temp.append(rowshigh[i][j])
        box_high.append(temp)

        sector_high.append(box_high[i][4])
        # high digit transform
        high.append(float(box_high[i][6].replace("▲", "")))

    for k in range(len(rowslow)):
        temp = []
        for l in range(len(rowslow[k])):
            temp.append(rowslow[k][l])
        box_low.append(temp)

        sector_low.append(box_low[k][4])
        low.append(float(box_low[k][6].replace("▼", "")))

    # for plot: sector categories count
    for m in range(65):
        high_item = sector_high[m]
        if high_item not in sector_categories:
            sector_categories.append(high_item)
        else:
            pass
    for n in range(65):
        low_item = sector_low[n]
        if low_item not in sector_categories:
            sector_categories.append(low_item)
        else:
            pass
    # # adjust the length of sector name
    fixed_sector = pd.Series(sector_categories)
    fixed_sector[3] = "其它電"
    fixed_sector[17] = "生技"
    fixed_sector[21] = "資服"
    final_sector_name = fixed_sector.tolist()

    # print("sector_categories is :")
    # print(sector_categories)
    # print()
    # print("fixed_sector is :")
    # print(fixed_sector)
    # print("final_sector is :")
    # print(final_sector_name)
    return final_sector_name


sectories_totalcount = sectories_count()


def data1(sectories_totalcount):
    conn = pymysql.connect(
        host=os.getenv("mysql_host"),
        port=int(os.getenv("mysql_port")),
        user=os.getenv("mysql_user"),
        passwd=os.getenv("mysql_passwd"),
        db=os.getenv("mysql_db"),
        charset=os.getenv("mysql_charset")
    )

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210503 "
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

    # adjust the length of sector name
    for o in range(len(sector1)):
        if sector1[o] == "其它電子":
            sector1[o] = "其它電"
        elif sector1[o] == "生技醫療":
            sector1[o] = "生技"
        elif sector1[o] == "資訊服務":
            sector1[o] = "資務"
        else:
            pass

    # print("sector1 is :")
    # print(sector1)
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

    # print("hub1 is :")
    # print(hub1)

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub1:
            hub1[sectories_totalcount[r]] = {}
            hub1[sectories_totalcount[r]]["Total"] = 0
            hub1[sectories_totalcount[r]]["count"] = 0
            hub1[sectories_totalcount[r]]["Ave"] = 0
    # print("new hub1 is:")
    # print(hub1)

    keysList = list(hub1.keys())
    valuesList = list(hub1.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub1[index]["Ave"]
        data1.append(b)

    return hub1, data1


val = data1(sectories_totalcount)
# hub1
# print()
# print(val[0])
# print()
# data1
# print(val[1])


def date1_sector_value_sort(sectories_totalcount, val):
    extra = []
    for i in range(len(sectories_totalcount)):
        finalvalue = val[0][sectories_totalcount[i]]["Ave"]
        extra.append(finalvalue)
    return extra


a = date1_sector_value_sort(sectories_totalcount, val)
# print(a)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def data2(sectories_totalcount):
    conn = pymysql.connect(
        host=os.getenv("mysql_host"),
        port=int(os.getenv("mysql_port")),
        user=os.getenv("mysql_user"),
        passwd=os.getenv("mysql_passwd"),
        db=os.getenv("mysql_db"),
        charset=os.getenv("mysql_charset")
    )

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210514"
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

    # adjust the length of sector name
    for o in range(len(sector2)):
        if sector2[o] == "其它電子":
            sector2[o] = "其它電"
        elif sector2[o] == "生技醫療":
            sector2[o] = "生技"
        elif sector2[o] == "資訊服務":
            sector2[o] = "資務"
        else:
            pass
    # print("sector2 is :")
    # print(sector2)

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
    # print("hub2 is :")
    # print(hub2)

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub2:
            hub2[sectories_totalcount[r]] = {}
            hub2[sectories_totalcount[r]]["Total"] = 0
            hub2[sectories_totalcount[r]]["count"] = 0
            hub2[sectories_totalcount[r]]["Ave"] = 0

    # print("new hub2 is:")
    # print(hub2)

    keysList = list(hub2.keys())
    valuesList = list(hub2.values())
    # print(hub1)

    for y in range(len(keysList)):
        index = keysList[y]
        b = hub2[index]["Ave"]

        data2.append(b)
    # print(sector2)

    return hub2, data2


val2 = data2(sectories_totalcount)

# hub2
# print(val2[0])
# print()
# data2
# print(val2[1])
# print()


def date2_sector_value_sort(sectories_totalcount, val2):
    extra2 = []
    for j in range(len(sectories_totalcount)):
        finalvalue2 = val2[0][sectories_totalcount[j]]["Ave"]
        extra2.append(finalvalue2)
    return extra2


b = date2_sector_value_sort(sectories_totalcount, val2)
print(b)


def data3(sectories_totalcount):
    conn = pymysql.connect(
        host=os.getenv("mysql_host"),
        port=int(os.getenv("mysql_port")),
        user=os.getenv("mysql_user"),
        passwd=os.getenv("mysql_passwd"),
        db=os.getenv("mysql_db"),
        charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210517"
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

    # adjust the length of sector name
    for o in range(len(sector3)):
        if sector3[o] == "其它電子":
            sector3[o] = "其它電"
        elif sector3[o] == "生技醫療":
            sector3[o] = "生技"
        elif sector3[o] == "資訊服務":
            sector3[o] = "資務"
        else:
            pass

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
    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub3:
            hub3[sectories_totalcount[r]] = {}
            hub3[sectories_totalcount[r]]["Total"] = 0
            hub3[sectories_totalcount[r]]["count"] = 0
            hub3[sectories_totalcount[r]]["Ave"] = 0

    keysList = list(hub3.keys())
    valuesList = list(hub3.values())

    for z in range(len(keysList)):
        index = keysList[z]
        b = hub3[index]["Ave"]

        data3.append(b)

    return hub3, data3


val3 = data3(sectories_totalcount)
# hub3
# print(val3[0])
# data3
# print(val3[1])


def date3_sector_value_sort(sectories_totalcount, val3):
    extra3 = []
    for k in range(len(sectories_totalcount)):
        finalvalue3 = val3[0][sectories_totalcount[k]]["Ave"]
        extra3.append(finalvalue3)
    return extra3


c = date3_sector_value_sort(sectories_totalcount, val3)
print(c)


def plot(sectories_totalcount, a, b, c):
    output_file("liststock_high_group_by_sector.html")

    sector = sectories_totalcount

    date = ['20210503', '20210514', '20210517']

    width_of_high = {'sector': sectories_totalcount,
                     '20210503': a,
                     '20210514': b,
                     '20210517': c}
    source = ColumnDataSource(data=width_of_high)

    p = figure(x_range=sector, y_range=(0, 40), plot_height=250, title="Sector of Liststock High",
               sizing_mode="scale_width")

    p.vbar(x=dodge('sector', -0.25, range=p.x_range), top='20210503', width=0.2, source=source,
           color="#c9d9d3", legend_label="20210503")

    p.vbar(x=dodge('sector',  0.0,  range=p.x_range), top='20210514', width=0.2, source=source,
           color="#718dbf", legend_label="20210514")

    p.vbar(x=dodge('sector',  0.25, range=p.x_range), top='20210517', width=0.2, source=source,
           color="#e84d60", legend_label="20210517")

    p.x_range.range_padding = -0.02
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
    p.title.text_font_size = "30px"
    # show(p)
    grid = gridplot([[p]], plot_width=850, plot_height=550)

    show(grid)


"""
Plot figure by grouping the sector of liststock high.
dodge() : every bar in each group has the same category, to avoid the
bars will overlap, use the dodge().
"""

d = plot(sectories_totalcount, a, b, c)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
