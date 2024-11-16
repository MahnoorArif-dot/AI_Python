#python -m pip install pyodbc
#pip install pyodbc
#pyodbc

#===========================================================
print("This program may requires ODBC configuation to run")
#===========================================================

import pyodbc as dbms

#pw = getpass.getpass("Enter password: ")
#print(pw)

conn_str = r'DSN=Excel Files;DBQ=C:\data\students.xlsx'

con = dbms.connect(conn_str, autocommit=True)

print("Successfully connected to Excel Workbook")

cur = con.cursor()

#one time task
cur.execute("create table student (rollno text, stname text, semester int, phoneno text, deptno text)")
cur.execute("create table grade (rollno text, course text, marks real)")

cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M088', 3, 'Naveed')")
cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M065', 3, 'Bilawal')")
cur.execute("insert into student (rollno, stname, deptno) values ('BSDSF22M08818', 'Zafar', 'DS')")
con.commit()

cur.execute("SELECT rollno as rno, stname as name FROM student")
print(cur.description[0][0], cur.description[1][0])
for row in cur:
   print(row[1], row[0])

cur.close()
con.close()
