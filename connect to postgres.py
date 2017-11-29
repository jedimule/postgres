import psycopg2
import ogr

#test comment for github

host = 'localhost'
database = 'andy'
port = '5432'
user = ''
password = ''

try:
    connection = psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port)
    print connection
    print 'I can connect'

    cur = connection.cursor()

    cur.execute("select * from test;")
    result = cur.fetchall()
    print 'ID' + ' ' + 'Coordinates'
    for item in result:
        x = item[2]
        y = item[3]

        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(x, y)

        print item[0], point

    cur.close()
    connection.close()
except:
    print 'I can not connect'
