import psycopg2

hostname = 'localhost'
database = 'SelfServiceCashier'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = None
cur = None


def close_cursor():
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

def updateID():
    # This extract a MAX id and adding +1 into it to then deploy in the sql
    cur.execute('SELECT MAX(id) FROM data_customer')
    recordID = cur.fetchone()
    id = recordID[0]
    id = id + 1
    return id

def show_list_of_customer():
    cur.execute('SELECT * FROM data_customer')
    print('No, Nama Customer, Nama Item, Jumlah Item, Harga/Item, Total Harga')
    for record in cur.fetchall():
        print(f'{record[0]}, {record[1]}, {record[2]}, {record[3]}, {record[4]}, {record[5]}')

def save_data_to_database(nama_customer, nama_item, jumlah_item, harga_item, total_harga):
    # on progress
    
    insert_script = ('''INSERT INTO data_customer (
                        id,
                        nama_customer,
                        nama_item,
                        jumlah_item,
                        harga_item,
                        total_harga)
                VALUES (%s, %s, %s, %s, %s, %s)''')
    insert_values = 'a'
    cur.execute(insert_script, insert_values)

    
try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

    cur = conn.cursor()


    


except Exception as error:
    print(error)

finally:
    close_cursor()

## def id_assignments():
