# main.py (Optimized & Safe Version)

from flask import Flask, render_template, Response, redirect, request, url_for
from camera import VideoCamera
import cv2
import numpy as np
import os
import time
import shutil
import imagehash
from PIL import Image
import webbrowser
import mysql.connector

# ============================
# Database Connection
# ============================

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        charset="utf8",
        database="nox_eye"
    )
except Exception as e:
    print("DATABASE CONNECTION ERROR:", str(e))
    exit()

app = Flask(__name__)
app.secret_key = 'abcdef'


# ============================
# Utility — Safe file writer
# ============================

def safe_write(filename, data):
    with open(filename, "w") as f:
        f.write(str(data))


def safe_read(filename, default=""):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    return default


# ============================
# ROUTES
# ============================

@app.route('/', methods=['POST', 'GET'])
def index():
    safe_write("note.txt", "1")
    safe_write("det.txt", "1")
    safe_write("photo.txt", "1")
    safe_write("img.txt", "1")
    safe_write("person.txt", "")

    msg = ""

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pass']
        cursor = mydb.cursor()

        cursor.execute(
            "SELECT count(*) FROM admin WHERE username=%s AND password=%s",
            (username, password)
        )
        result = cursor.fetchone()[0]

        if result > 0:
            return redirect(url_for('admin1'))
        else:
            msg = "Login Failed!"

    return render_template('index.html', msg=msg)


# -------------------------------------------


@app.route('/login', methods=['POST', 'GET'])
def login():
    safe_write("photo.txt", "1")
    result = ""

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pass']
        cursor = mydb.cursor()

        cursor.execute(
            "SELECT count(*) FROM admin WHERE username=%s AND password=%s",
            (username, password)
        )
        if cursor.fetchone()[0] > 0:
            return redirect(url_for('admin'))
        else:
            result = "Login Failed!"

    return render_template('login.html', result=result)


# -------------------------------------------

@app.route('/login_user', methods=['POST', 'GET'])
def login_user():
    safe_write("photo.txt", "1")
    result = ""

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pass']
        cursor = mydb.cursor()

        cursor.execute(
            "SELECT count(*) FROM user_details WHERE uname=%s AND pass=%s",
            (username, password)
        )
        if cursor.fetchone()[0] > 0:
            return redirect(url_for('userhome'))
        else:
            result = "Login Failed!"

    return render_template('login_user.html', result=result)


# -------------------------------------------

@app.route('/monitor')
def monitor():
    return render_template('monitor.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


# -------------------------------------------

@app.route('/userhome', methods=['POST', 'GET'])
def userhome():
    cursor = mydb.cursor()

    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        location = request.form['location']

        cursor.execute(
            "UPDATE user_details SET name=%s, mobile=%s, email=%s, location=%s WHERE id=1",
            (name, mobile, email, location)
        )
        mydb.commit()
        return redirect(url_for('userhome', act='success'))

    cursor.execute("SELECT * FROM user_details")
    data = cursor.fetchone()

    return render_template('userhome.html', data=data)


# -------------------------------------------

@app.route('/detect')
def detect():
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM detect_info ORDER BY id DESC")
    detect_logs = cursor.fetchall()

    cursor.execute("SELECT * FROM user_details")
    user = cursor.fetchone()

    return render_template('detect.html', data=user, data2=detect_logs)


# -------------------------------------------

@app.route('/add_contact', methods=['POST', 'GET'])
def add_contact():
    cursor = mydb.cursor()

    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        location = request.form['location']

        cursor.execute(
            "UPDATE admin SET name=%s, mobile=%s, email=%s, location=%s WHERE username='admin'",
            (name, mobile, email, location)
        )
        mydb.commit()
        return redirect(url_for('add_contact', act='success'))

    cursor.execute("SELECT * FROM admin")
    data = cursor.fetchone()

    return render_template('add_contact.html', data=data)


# -------------------------------------------

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    safe_write("photo.txt", "2")
    cursor = mydb.cursor()

    if request.method == 'POST':
        name = request.form['name']

        cursor.execute("SELECT max(id) + 1 FROM register")
        maxid = cursor.fetchone()[0] or 1

        cursor.execute("INSERT INTO register(id, name) VALUES (%s, %s)", (maxid, name))
        mydb.commit()

        return redirect(url_for('add_photo', vid=maxid))

    cursor.execute("SELECT * FROM register")
    data = cursor.fetchall()

    return render_template('admin.html', data=data)


# -------------------------------------------

@app.route('/add_photo', methods=['POST', 'GET'])
def add_photo():
    safe_write("photo.txt", "2")
    cursor = mydb.cursor()

    vid = request.args.get('vid') if request.method == 'GET' else ""

    if request.method == 'GET':
        safe_write("user.txt", vid)

    if request.method == 'POST':
        vid = request.form['vid']

        cursor.execute("DELETE FROM vt_face WHERE vid=%s", (vid,))
        mydb.commit()

        det = int(safe_read("det.txt", 1))
        for i in range(2, det):
            cursor.execute("SELECT max(id) + 1 FROM vt_face")
            maxid = cursor.fetchone()[0] or 1

            file_name = f"{vid}_{i}.jpg"
            cursor.execute(
                "INSERT INTO vt_face(id, vid, vface) VALUES (%s, %s, %s)",
                (maxid, vid, file_name)
            )
            mydb.commit()

        return redirect(url_for('view_photo', vid=vid, act='success'))

    cursor.execute("SELECT * FROM register")
    data = cursor.fetchall()

    return render_template('add_photo.html', data=data, vid=vid)


# -------------------------------------------

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n\r\n'
        )


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


# -------------------------------------------

@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# ============================
# Run Application
# ============================

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)
