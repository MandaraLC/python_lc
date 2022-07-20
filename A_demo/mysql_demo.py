import pymysql
import time

dbhost='127.0.0.1'
dbuser='root'
dbpass='123456'
dbname='bandai'

db = pymysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
'''
#查询
cursor = db.cursor()
sql = "SELECT * FROM b_cookie WHERE status=0 limit 1"
try:
    # 执行SQL语句
	cursor.execute(sql)
	results = cursor.fetchall()
	print(results)
	for row in results:
		lname = row[0]
		print(lname)
except Exception as e:
   print(e)
finally:
	if db:
		db.close()
'''
#插入数据
cursor = db.cursor()
create = int(time.time())
sql = "INSERT INTO b_cookie(cookie, status, creattime) VALUES('sdgsdgsgsgsg', 0, %d)" %(create)
print(sql)
try:
	cursor.execute(sql)
	db.commit()
	print('commit......')
except Exception as e:
	print(e)
	db.rollback()
finally:
	if db:
		db.close()

'''
#删除数据
cursor = db.cursor()
sql = "DELETE FROM b_cookie WHERE id = %d" % (1)
try:
   # 执行SQL语句
	cursor.execute(sql)
   # 提交修改
	db.commit()
	print('删除成功')
except:
   # 发生错误时回滚
	db.rollback()
	print('rollback')
finally:
	if db:
		db.close()
'''


cursor = db.cursor()
sql = "UPDATE b_user SET `data`=1323,status=0 WHERE account='king'"
try:
	cursor.execute(sql)
   # 提交到数据库执行
	db.commit()
except:
   # 发生错误时回滚
	db.rollback()
