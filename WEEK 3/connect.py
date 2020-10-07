# import mysql.connector
# from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='aerobic_penjadwalan',
#                                          user='root',
#                                          password='')

#     sql_select_Query = "select * from admin"
#     sql_insert_Query = "INSERT INTO `admin`(`id`, `username`, `email`, `password`) VALUES (21,'usernameku','asd@gmail.com','asd123')"
#     cursor = connection.cursor()
#     cursor.execute(sql_insert_Query)
#     # records = cursor.fetchall()

#     # for row in records:
#     #     print("Id = ", row[0], )
#     #     print("username = ", row[1])
#     #     print("email  = ", row[2])
#     #     print("password = ", row[3], "\n")
#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into Laptop table")
#     cursor.close()

# except Error as e:
#     print("Error reading data from MySQL table", e)
# finally:
#     if (connection.is_connected()):
#         connection.close()
#         cursor.close()
#         print("MySQL connection is closed")


from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

import pandas as pd

# dd/mm/YY
# dt_string = now.strftime("%Y-%m-%d")
# url = 'https://asd.com/' + dt_string
# # print("date and time =", dt_string)
# print(url)

all = pd.read_csv('4okt.csv')
content = all["content"]
sub = content.head()

print(sub)