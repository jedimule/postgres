import psycopg2

# layer to save the data too
pointLayer = QgsVectorLayer('Point?crs=ESPG:4326', 'points', 'memory')

# postgres connection details
host = 'localhost'
database = 'andy'
port = '5432'
user = 'andy'
password = ''

try:
    # opening a connection to the database
    connection = psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port)
    print 'I can connect'
    cur = connection.cursor()
    cur.execute("select * from test;")
    result = cur.fetchall()

    for item in result:
        x = item[2]
        y = item[3]

        # creating geometry from lat and lon values
        lyr = pointLayer.dataProvider()
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(x, y)))

        # adding features to the QGS layer
        lyr.addFeatures([feat])
        pointLayer.updateExtents()

    cur.close()
    connection.close()
except:
    print 'I can not connect'

# adding layer to the map canvas
QgsMapLayerRegistry.instance().addMapLayers([pointLayer])
