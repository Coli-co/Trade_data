import pymysql
from highcharts import Highchart
import os
from dotenv import load_dotenv
load_dotenv()

# def connect_to_database():
# Connect to MySQL Database
conn = pymysql.connect(host=os.getenv("mysql_host"), port=int(os.getenv("mysql_port")), user=os.getenv("mysql_user"),
                       passwd=os.getenv("mysql_passwd"), db=os.getenv("mysql_db"), charset=os.getenv("mysql_charset"))

cursor = conn.cursor()
# call_data_selected
rows = cursor.execute(
    "SELECT * FROM %s.%s where date =20210428" % (os.getenv("mysql_db"), os.getenv("table_b")))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# confirm the data print
# for call
box = []
# for put
box1 = []
# call and put have the smae strike_price
strike_price = []
# call_open_interest
call_open_interest = []
# put_open_interest
put_open_interest = []

row = cursor.fetchmany(6)
# print(row)
for i in range(len(row)):
    temp = []
    for j in range(len(row[i])):
        temp.append(row[i][j])
        # print(temp)
    box.append(temp)

    strike_price.append(box[i][4])
    # print(strike_price)

    call_open_interest.append(box[i][5])
    # print(call_open_interest)


# put_data_selected
rows2 = cursor.execute(
    "SELECT * FROM trader_info.optionput_daily_trade where date =20210428")
row = cursor.fetchmany(6)
for k in range(len(row)):
    temp = []
    for j in range(len(row[k])):
        temp.append(row[k][j])
    box1.append(temp)
    put_open_interest.append(box1[k][5])
    # print(put_open_interest)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 縱軸分類區間(履約價)
categories = strike_price


# Strikeplace categories
categories = strike_place

Highcharts.chart('container', {
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Open Interest of Call and Put'
    },
    subtitle: {
        text: '20210428'
    },
    accessibility: {
        point: {
            valueDescriptionFormat: '{index}. strike_price {xDescription}, {value}%.'
        }
    },
    xAxis: [{
        categories: categories,
        reversed: false,
        labels: {
            step: 1
        },
        accessibility: {
            description: 'strike_price (put)'
        }
    }, {
        # // mirror axis on right side
        opposite: true,
        reversed: false,
        categories: categories,
        linkedTo: 0,
        labels: {
            step: 1
        },
        accessibility: {
            description: 'strike_price (call)'
        }
    }],
    yAxis: {
        title: {
            text: null
        },
        labels: {
            formatter: function() {return Math.abs(this.value)
                                   }
        },
        accessibility: {
            description: 'Range of Open Interest',
            rangeDescription: 'Range: -15000 to 15000'
        }
    },

    plotOptions: {
        series: {
            stacking: 'normal'
        }
    },

    tooltip: {
        formatter: function() {
            return '<b>' + this.series.name + ', strike_price ' + this.point.category + '</b><br/>' +
            'open_interest: ' +
            Highcharts.numberFormat(Math.abs(this.point.y), 1)
        }
    },

    series: [{
        name: 'Put',
        data: put_open_interest
    }, {
        name: 'Call',
        data: call_open_interest
    }]
})
