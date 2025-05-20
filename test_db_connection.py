import  psycopg2

try:
    conn = psycopg2.connect(
        dbname='tasks.db',
        user='tim',
        password='4200',
        host='localhost',
        port='5432'
    )
    print('Connecting is successfully')
    conn.close()
except Exception as e:
    print('Connection is unsuccessfully:', e)