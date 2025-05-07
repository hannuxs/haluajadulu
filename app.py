import os
import uuid
from flask import Flask, request, render_template, redirect, flash
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  
app.secret_key = os.getenv('SECRET_KEY')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')


mysql = MySQL(app)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Fungsi cek ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'

# Simulasi login (sementara)
CURRENT_USER_ID = 1

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')

        if not file or file.filename == '':
            flash('Tidak ada file yang dipilih')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('Hanya file CSV yang diperbolehkan')
            return redirect(request.url)

        # Simpan file ke folder
        filename = f"{uuid.uuid4()}.csv"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Simpan ke DB
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO upload (id_user, file) VALUES (%s, %s)", (CURRENT_USER_ID, filename))
        mysql.connection.commit()
        cursor.close()

        flash('File berhasil di-upload')
        return redirect(request.url)

    # Ambil file yang diupload oleh user
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT file FROM upload WHERE id_user = %s", (CURRENT_USER_ID,))
    files = cursor.fetchall()
    cursor.close()

    return render_template('index.html', files=files)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    # Hapus file dari folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)

    # Hapus dari database
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM upload WHERE file = %s", (filename,))
    mysql.connection.commit()
    cursor.close()

    flash('File berhasil dihapus')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
