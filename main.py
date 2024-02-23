from flask import Flask, url_for, redirect, render_template
import settings as stg 

import db_scripts as db

app = Flask(__name__, static_folder=stg.PATH_STATIC)
app.config['SECRET_KEY'] = stg.SECRET_KEY 

@app.route('/')
@app.route('/index')
def index ():
    return render_template('index.html')

@app.route('/post/category')
def post_category():
    return 'Categories of posts'

@app.route('/post/view')
def post_view():
    return 'here will be post'

@app.route('/about')
def about():
    user = db.getUser()
    print(user)
    return render_template('about.html', user=user)

app.run(debug=True)
