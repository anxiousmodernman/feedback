import pyodbc
cnxn = pyodbc.connect('DSN=alchemyqa;UID=livelookup;PWD=temporary_horses123')
cursor = cnxn.cursor()
cursor.execute("select top 5 brief_name, briefid from brief")
rows = cursor.fetchall()
for row in rows:
    print row.brief_name, row.briefid

cursor.close()
