import pymysql

# 建立連線
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1qaz2wsx', db='store', charset='utf8')
# 建立操作遊標, 查詢資料預設為元組型別
cursor = conn.cursor()

sq0 = "SELECT product_id, \
    quantity * unit_price AS total_price\
    from order_items\
    RIGHT JOIN orders on order_items.order_id = orders.order_id \
    ORDER BY product_id"

cursor.execute(sq0)

result = cursor.fetchall()

for x in result:
    print(x)



# 關閉遊標
cursor.close()
# 關閉連線
conn.close()
        
# sql = "insert into customers(first_name, last_name, address, city, state) values('Timothy','Lee', 'home', 'Taipei', 'Taiwan')" 
# sq2 = "UPDATE customers set  points = points + 100 where state = '%s'" % ('VA')
# sq3 = "Select * from customers where points > %s" %(1000)
# sq4 = "Delete from customers where points = %s" %(0)

# try:
#     cursor.execute(sq4)
#     conn.commit()



# sql語句若要跳下一行，記得加上\
# Rollback in case there is any error
