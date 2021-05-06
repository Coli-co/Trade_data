import pymysql

from bokeh.io import output_file, show
from bokeh.models import FactorRange
from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot

# Remember tp adjust the expire_date and open_interest of
# call and pur before plotting


def call_info():
    # def connect_to_database():
    # Connect to MySQL Database
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='1qaz2wsx', db='trader_info', charset='utf8')

    cursor = conn.cursor()
    # call_data_selected
    row1 = cursor.execute(
        "SELECT * FROM trader_info.optioncall_daily_trade where date =20210506")

    # confirm the data print
    # for call
    box = []
    strike_price = []
    call_open_interest = []
    expire_date = []
    container = []
    # row = cursor.fetchmany(6)
    row1 = cursor.fetchall()
    # print(row)

    for i in range(len(row1)):
        temp = []
        for j in range(len(row1[i])):
            temp.append(row1[i][j])
        box.append(temp)
        # print(box)

        expire_date.append(box[i][3])
        strike_price.append(box[i][4])
        call_open_interest.append(int(box[i][5]))
    for k in range(len(expire_date)):
        print(expire_date[k])
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # strike_price.append(box[i][4])
    for l in range(len(strike_price)):
        print(strike_price[l])
    for m in range(40):
        factor = ()
        factor += (expire_date[m], strike_price[m])
        print(factor)
        container.append(factor)
    print(container)

    for n in range(len(call_open_interest)):
        print(call_open_interest[n])

    # open_interest
    x = call_open_interest
    # print(x)
    output_file("call_open_interest.html")
    p = figure(x_range=FactorRange(*container), plot_height=150, title="Open Interest of Call",
               sizing_mode="scale_width")

    # p = figure(x_range=FactorRange(*container), plot_height=150, title="Open Interest of Call",
    #            toolbar_location=None, tools="")

    p.vbar(x=container, top=x, width=0.9, alpha=0.5)
    # biggest of call open interest
    p.line(x=["202105W2", "202105", "202106"],
           y=[4132, 8962, 696], color="red", line_width=2)

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None

    # show(p)

    return p


"""Connect to database to get option call data and plot"""

a = call_info()


def put():

    conn2 = pymysql.connect(host='localhost', port=3306, user='root',
                            passwd='1qaz2wsx', db='trader_info', charset='utf8')

    cursor = conn2.cursor()

    rows2 = cursor.execute(
        "SELECT * FROM trader_info.optionput_daily_trade where date =20210506")
    # for put
    box1 = []
    strike_price1 = []
    put_open_interest = []
    expire_date1 = []
    container1 = []
    # row = cursor.fetchmany(6)

    row2 = cursor.fetchall()

    for i in range(len(row2)):
        temp1 = []
        for j in range(len(row2[i])):
            temp1.append(row2[i][j])
        box1.append(temp1)
        # print(box)

        expire_date1.append(box1[i][3])
        strike_price1.append(box1[i][4])
        put_open_interest.append(int(box1[i][5]))
    for k in range(len(expire_date1)):
        print(expire_date1[k])

    for l in range(len(strike_price1)):
        print(strike_price1[l])
    for m in range(40):
        factor1 = ()
        factor1 += (expire_date1[m], strike_price1[m])
        print(factor1)
        container1.append(factor1)
    print(container1)

    for n in range(len(put_open_interest)):
        print(put_open_interest[n])

    # open_interest
    x = put_open_interest
    # print(x)

    output_file("put_open_interest.html")
    p1 = figure(x_range=FactorRange(*container1), plot_height=150, title="Open Interest of Put",
                sizing_mode="scale_width")

    # p = figure(x_range=FactorRange(*container), plot_height=150, title="Open Interest of Call",
    #            toolbar_location=None, tools="")

    p1.vbar(x=container1, top=x, width=0.9, alpha=0.5)
    # biggest of call interest
    p1.line(x=["202105W2", "202105", "202106"],
            y=[2673, 12802, 5559], color="red", line_width=2)

    p1.y_range.start = 0
    p1.x_range.range_padding = 0.1
    p1.xaxis.major_label_orientation = 1
    p1.xgrid.grid_line_color = None

    # show(p1)
    return p1


"""Connect to database to get option put data and plot"""

b = put()


def call_and_put_combining_plots(a, b):
    # show(row(a, b))

    grid = gridplot([[a, b]], plot_width=850, plot_height=550)
    show(grid)


call_and_put_combining_plots(a, b)
