import os
import sqlite3
import json
from time import gmtime, strftime

db_filename = "example.db"
schema_filename = "db_schema.sql"

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect('example.db') as conn:
    if db_is_new:
        #print "Creating schema"
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        #print "Inserting initial data"

        conn.execute("INSERT INTO employees VALUES('10167462','Paul Stallworth')")
        conn.execute("INSERT INTO keylog VALUES('master','154','M','10167462','Paul Stallworth','20018669','2013-10-04 16:00:00',null,null)")
        conn.commit()
        conn.close()

def add_employee(id_number, name):
    conn = sqlite3.connect('example.db')
    record = (id_number, name)
    conn.execute('INSERT INTO employees VALUES(?,?)', record)
    conn.commit()
    conn.close()

def add_record(params):
    conn = sqlite3.connect('example.db')
    name = lookup_employee_name(params.requestorID)
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    record = (params.keyName, params.keyNumber, params.keyType, params.requestorID,
                name, params.releaserID, now, None, None)
    conn.execute('INSERT INTO keylog VALUES(?,?,?,?,?,?,?,?,?)', record)
    conn.commit()
    conn.close()
    
def lookup_employee_name(id_number):
    conn = sqlite3.connect('example.db')
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT name from EMPLOYEES WHERE id = ?', [id_number])
    data = c.fetchone()
    conn.close()
    return data[0]

def source_table_json():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM keylog")
    data = c.fetchall()
    print data
    print "json:\n %s" % json.dumps(data)
    conn.close()
    return json.dumps(data)
 
def source_table_raw():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM keylog")
    data = c.fetchall()
    conn.close()
    return data
 
