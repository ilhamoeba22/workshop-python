from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors
app = Flask(_name_)
 
conn = cursor = None
#fungsi koneksi database
def openDb():
   global conn, cursor
   conn =   conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "",
        db='db_esotechno',
        )
      
   cursor = conn.cursor()	
#fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()
   
@app.route('/')
def index():
    openDb()``
    container = []
    sql = "SELECT * FROM tb_anggota"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
      container.append(data)
    closeDb()
    return render_template('index.html', container=container)