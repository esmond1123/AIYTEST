import pymysql
import datetime
db = pymysql.connect(host = 'esshb.essh.kl.edu.tw', user ='aiyroot', passwd = 'aiy621', db = 'aiydb')
cur = db.cursor()
date = str(datetime.datetime.now().date())
cur.execute("select * from peoplecounting where date ='"+date+"'")
row = cur.fetchall()
if row:
    p = row[0][2] + 1 ;
    cur.execute("update peoplecounting set people ="+str(p)+" where sn =" + str(row[0][0]))
    db.commit()
    print(date + " 現在總人數： " + str(p))
else:
    r = "insert into peoplecounting(date,people)VALUES('"+date+"',1)"
    print(r)
    cur.execute(r)
    db.commit()
    print(date + " 現在總人數：  1")
db.close