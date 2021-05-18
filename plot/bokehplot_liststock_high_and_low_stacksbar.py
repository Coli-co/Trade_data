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


def sector_count():
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

    print("sector_categories is :")
    print(sector_categories)
    return sector_categories


sectories_totalcount = sector_count()


def high_data1(sectories_totalcount):
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

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

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub1:
            hub1[sectories_totalcount[r]] = {}
            hub1[sectories_totalcount[r]]["Total"] = 0
            hub1[sectories_totalcount[r]]["count"] = 0
            hub1[sectories_totalcount[r]]["Ave"] = 0

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


val = high_data1(sectories_totalcount)
# hub1
# print(val[0])
# print()
# # data1
# print(val[1])
# print()


def high_data1_sectorvalue_sort(sectories_totalcount, val):
    extra = []
    for i in range(len(sectories_totalcount)):
        finalvalue = val[0][sectories_totalcount[i]]["Ave"]
        extra.append(finalvalue)
    return extra


a = high_data1_sectorvalue_sort(sectories_totalcount, val)
print("a is :")
print(a)


def high_data2(sectories_totalcount):
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

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

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub2:
            hub2[sectories_totalcount[r]] = {}
            hub2[sectories_totalcount[r]]["Total"] = 0
            hub2[sectories_totalcount[r]]["count"] = 0
            hub2[sectories_totalcount[r]]["Ave"] = 0

    keysList = list(hub2.keys())
    valuesList = list(hub2.values())
    # print(hub1)

    for y in range(len(keysList)):
        index = keysList[y]
        b = hub2[index]["Ave"]

        data2.append(b)
    # del data2[15:]

    return hub2, data2


val2 = high_data2(sectories_totalcount)
# hub2
# print(val2[0])
# data2
# print(val2[1])
# print()


def high_data2_sectorvalue_sort(sectories_totalcount, val2):
    extra2 = []
    for j in range(len(sectories_totalcount)):
        finalvalue2 = val2[0][sectories_totalcount[j]]["Ave"]
        extra2.append(finalvalue2)
    return extra2


b = high_data2_sectorvalue_sort(sectories_totalcount, val2)
# print("b is :")
# print(b)


def high_data3(sectories_totalcount):
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

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
    # print(hub1)

    for z in range(len(keysList)):
        index = keysList[z]
        b = hub3[index]["Ave"]

        data3.append(b)
    # del data3[15:]
    return hub3, data3


val3 = high_data3(sectories_totalcount)
# hub3
# print(val3[0])
# data3
# print(val3[1])
# print()


def high_data3_sectorvalue_sort(sectories_totalcount, val3):
    extra3 = []
    for k in range(len(sectories_totalcount)):
        finalvalue3 = val3[0][sectories_totalcount[k]]["Ave"]
        extra3.append(finalvalue3)
    return extra3


c = high_data3_sectorvalue_sort(sectories_totalcount, val3)
# print("c is :")
# print(c)


def low_data1(sectories_totalcount):
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210503 "
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

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub4:
            hub4[sectories_totalcount[r]] = {}
            hub4[sectories_totalcount[r]]["Total"] = 0
            hub4[sectories_totalcount[r]]["count"] = 0
            hub4[sectories_totalcount[r]]["Ave"] = 0

    keysList = list(hub4.keys())
    valuesList = list(hub4.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub4[index]["Ave"]

        data4.append(b)
    return hub4, data4


val4 = low_data1(sectories_totalcount)
# hub4
# print(val4[0])
# # data4
# print(val4[1])


def low_data1_sectorvalue_sort(sectories_totalcount, val4):
    extra4 = []
    for l in range(len(sectories_totalcount)):
        finalvalue4 = val4[0][sectories_totalcount[l]]["Ave"]
        extra4.append(finalvalue4)
    return extra4


d = low_data1_sectorvalue_sort(sectories_totalcount, val4)
# print("d is :")
# print(d)


def low_data2(sectories_totalcount):
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210514 "
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

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub5:
            hub5[sectories_totalcount[r]] = {}
            hub5[sectories_totalcount[r]]["Total"] = 0
            hub5[sectories_totalcount[r]]["count"] = 0
            hub5[sectories_totalcount[r]]["Ave"] = 0

    keysList = list(hub5.keys())
    valuesList = list(hub5.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub5[index]["Ave"]

        data5.append(b)
    return hub5, data5


val5 = low_data2(sectories_totalcount)
# hub5
# print(val5[0])
# # data5
# print(val5[1])
# print()


def low_data2_sectorvalue_sort(sectories_totalcount, val5):
    extra5 = []
    for m in range(len(sectories_totalcount)):
        finalvalue5 = val5[0][sectories_totalcount[m]]["Ave"]
        extra5.append(finalvalue5)
    return extra5


e = low_data2_sectorvalue_sort(sectories_totalcount, val5)
# print("e is :")
# print(e)


def low_data3(sectories_totalcount):
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset")
                           )

    cursor = conn.cursor()

    rows = cursor.execute(
        "SELECT * FROM %s.%s where date = 20210517 "
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

    for r in range(len(sectories_totalcount)):
        if sectories_totalcount[r] not in hub6:
            hub6[sectories_totalcount[r]] = {}
            hub6[sectories_totalcount[r]]["Total"] = 0
            hub6[sectories_totalcount[r]]["count"] = 0
            hub6[sectories_totalcount[r]]["Ave"] = 0

    keysList = list(hub6.keys())
    valuesList = list(hub6.values())
    # print(hub1)

    for x in range(len(keysList)):
        index = keysList[x]
        b = hub6[index]["Ave"]

        data6.append(b)
    return hub6, data6


val6 = low_data3(sectories_totalcount)
# hub1
# print(val6[0])
# # data1
# print(val6[1])
# print()


def low_data3_sectorvalue_sort(sectories_totalcount, val6):
    extra6 = []
    for n in range(len(sectories_totalcount)):
        finalvalue6 = val6[0][sectories_totalcount[n]]["Ave"]
        extra6.append(finalvalue6)
    return extra6


f = low_data3_sectorvalue_sort(sectories_totalcount, val6)
# print("f is :")
# print(f)


def plot(sectories_totalcount, a, b, c, d, e, f):

    # def liststock_high_and_low_stack_bars_by_sector():
    output_file("liststock_high_and_low_stack_barsby_sector.html")

    sector = sectories_totalcount
    date = ['20210503', '20210514', '20210517']

    high = {'sector': sectories_totalcount,
            '20210503': a,
            '20210514': b,
            '20210517': c}
    low = {'sector': sectories_totalcount,
           '20210503': d,
           '20210514': e,
           '20210517': f
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


show = plot(sectories_totalcount, a, b, c, d, e, f)
