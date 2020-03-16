from django.db import connection

cursor = connection.cursor()
cursor.close()