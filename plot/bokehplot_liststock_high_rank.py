from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import dodge
from bokeh.palettes import GnBu3, OrRd3
import pymysql


def liststock_high_rank():
    # Connect to MySQL Database
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           passwd='1qaz2wsx', db='store', charset='utf8')

    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM trader_info.sector_of_liststock_high")

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

    # Filling colors
    # assign the name of the color column to the color argument of vbar
    output_file("liststock_high_rank.html")

    source = ColumnDataSource(data=dict(stock_name=stock_name,
                                        high_and_low=high_and_low, color=Spectral6))

    # p = figure(x_range=stock_name, y_range=(0, 15), plot_height=250, title="Sector of Liststock High Rank",
    #            toolbar_location=None, tools="")
    p = figure(x_range=stock_name, y_range=(0, 15), plot_height=250, title="Sector of Liststock High Rank",
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
p1 = liststock_high_rank()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def liststock_high_and_low_stack_bars_by_sector():
    output_file("liststock_high_and_low_stack_barsby_sector.html")

    sector = ['電零組', '電腦週邊', '電機', '電器電纜', '鋼鐵', '通信網路',
              '航運', '紡織', '玻璃', '橡膠', '半導體', '其它電子', '食品',
              '化學', '貿易百貨', '光電', '營建']
    date = ['20210426', '20210427', '20210428']

    high = {'sector': sector,
            '20210426': [2.25, 0, 3.95, 0, 0, 0, 5.43, 0, 0, 33.00, 2.23, 6.25, 0, 0],
            '20210427': [1.30, 2.45, 0, 2.00, 5.10, 1.40, 3.85, 4.70, 1.55, 0, 21.15, 0, 0, 0],
            '20210428': [3.15, 0, 0, 0, 0, 4.25, 0, 3.25, 1.45, 0, 46.00, 1.95,  15.00, 1.15]}
    low = {'sector': sector,
           '20210426': [-7.27, 0, 0, 0, 0, -7.27, 0, 0, 0, 0, 0, 0, 0, 0, -100, -3.45, -1.15],
           '20210427': [-2.85, -0.24, 0, 0, 0, 0, 0, -1.30, 0, -32.00, -5.50, 0, 0, 0, 0, -0.73, -0.64],
           '20210428': [0, 0, -2.25, 0, 0, 0, 0, -1.10, 0, -19.25, -8.62, 0, 0, 0, 0, -0.30, -1.35]
           }
    # p = figure(y_range=sector, plot_height=250, x_range=(-50, 50), title="Liststock high/low by sector",
    #            toolbar_location=None)

    p = figure(y_range='sector', plot_height=250, x_range=(-50, 50), title="Liststock high/low by sector",
               sizing_mode="scale_width")

    p.hbar_stack(date, y='sector', height=0.9, color=GnBu3, source=ColumnDataSource(low),
                 legend_label=["%s width_of_low" % x for x in date])

    p.hbar_stack(date, y='sector', height=0.9, color=OrRd3, source=ColumnDataSource(high),
                 legend_label=["%s width_of_high" % x for x in date])

    p.y_range.range_padding = 0.05
    p.ygrid.grid_line_color = None
    p.legend.location = "top_left"
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None

    show(p)


"""
stack bars that represent liststock_high(positive) and 
liststock_low (negative) values.
"""

# p3 = liststock_high_and_low_stack_bars_by_sector()

# sliders = column(amp, freq, phase, offset)

# layout([
#     [bollinger],
#     [sliders, plot],
#     [p1, p2, p3],
# ])
