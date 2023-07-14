from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# koneksi ke database mySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="anilist"
)
cursor = db.cursor()

@app.route('/')
def index():
    # Mengambil semua list data dari tabel list
    cursor.execute("SELECT * FROM list")
    data = cursor.fetchall()

    return render_template('index.html', list=data)

if __name__ == '__main__':
    app.run(debug=True)
