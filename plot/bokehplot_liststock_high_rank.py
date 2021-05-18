from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import dodge
from bokeh.palettes import GnBu3, OrRd3
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


def liststock_high_rank_data():
    # Connect to MySQL Database
    conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                           passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM %s.%s where date = 20210518"
                          % (os.getenv("mysql_db"), os.getenv("table_d")))

    # confirm the data print and store in box, stock_name
    #  and wodth_of_high
    box = []
    stock_name = []
    width_of_high = []
    high_and_low = []
    # sector = []
    rows = cursor.fetchmany(6)
    # print(row)
    for i in range(len(rows)):
        temp = []
        for j in range(len(rows[i])):
            temp.append(rows[i][j])
        box.append(temp)
    # print(box)

    # store in stock_name list so that can be plot figure
        stock_name.append(box[i][3])

    # store in width_of_high list so that can be plot figure

        width_of_high.append(box[i][7])

    # store in high_and_low list so that can be plot figure
        high_and_low.append((box[i][6].replace("▲", "")))
        # print(high_and_low)
    return stock_name, high_and_low


a = liststock_high_rank_data()


def plot(a):
    # Filling colors
    # assign the name of the color column to the color argument of vbar
    output_file("liststock_high_rank.html")

    source = ColumnDataSource(data=dict(stock_name=a[0],
                                        high_and_low=a[1], color=Spectral6))

    # p = figure(x_range=stock_name, y_range=(0, 15), plot_height=250, title="Sector of Liststock High Rank",
    #            toolbar_location=None, tools="")
    p = figure(x_range=a[0], y_range=(0, 15), plot_height=250, title="Sector of Liststock High Rank",
               sizing_mode="scale_width")

    p.vbar(x='stock_name', top='high_and_low', width=0.5, color='color',
           legend_field="stock_name", source=source)

    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p.title.text = "Sector of Liststock High Rank"
    p.title.align = "left"
    p.title.text_color = "orange"
    p.title.text_font_size = "25px"
    p.title.background_fill_color = "#aaaaee"
    show(p)


"""
Firstly, connect to MySQL， call the data which wanted and stored in,
then plot figure of liststock ranking name.
plot params category:
stock_name & high_and_low 
"""
p1 = plot(a)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
