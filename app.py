import os
from flask import Flask, render_template, request
from models.Image.image import image
from models.Text.text import text
from models.Video.video import video
import sqlite3

UPLOAD_IMAGE_FOLDER = 'models/Image/static'
IMAGE_CACHE_FOLDER = 'models/Image/__pycache__'
UPLOAD_TEXT_FOLDER = 'models/Text/static'
TEXT_CACHE_FOLDER = 'models/Text/__pycache__'
UPLOAD_VIDEO_FOLDER = 'models/Video/static'
VIDEO_CACHE_FOLDER = 'models/Video/__pycache__'


# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = "hello"
app.config['UPLOAD_IMAGE_FOLDER'] = UPLOAD_IMAGE_FOLDER
app.config['IMAGE_CACHE_FOLDER'] = IMAGE_CACHE_FOLDER
app.config['UPLOAD_TEXT_FOLDER'] = UPLOAD_TEXT_FOLDER
app.config['TEXT_CACHE_FOLDER'] = TEXT_CACHE_FOLDER
app.config['UPLOAD_VIDEO_FOLDER'] = UPLOAD_VIDEO_FOLDER
app.config['VIDEO_CACHE_FOLDER'] = VIDEO_CACHE_FOLDER

app.register_blueprint(image, url_prefix="/image")
app.register_blueprint(text, url_prefix="/text")
app.register_blueprint(video, url_prefix="/video")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route("/signup")
def signup():

    username = request.args.get('username','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('username','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("home.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("home.html")
    else:
        return render_template("signup.html")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/message")
def message():

    name = request.args.get('name','')
    email = request.args.get('email','')
    message = request.args.get('message','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `infos` (`user`,`email`, `message`) VALUES (?, ?, ?)",(name,email,message))
    data = cur.fetchone()
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)