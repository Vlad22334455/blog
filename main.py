<<<<<<< HEAD
from flask import Flask, url_for, redirect
import settings as stg 

app = Flask(__name__, static_folder=stg.PATH_STATIC)
app.config['SECRET_KEY'] = stg.SECRET_KEY 

@app.route('/')
def index ():
    url = url_for('static','templates/index.html') 
    return redirect(url)

@app.route('/post/category')
def post_category():
    return 'Categories of posts'

@app.route('/post/view')
def post_view():
    return 'here will be post'

@app.route('/about')
def about():
    return 'information about Athor'

app.run(debug=True)
=======
from flask import Flask, url_for, redirect
import settings as stg 

app = Flask(__name__, static_folder=stg.PATH_STATIC)
app.config['SECRET_KEY'] = stg.SECRET_KEY 

@app.route('/')
def index ():
    url = url_for('static','templates/index.html') 
    return redirect(url)

@app.route('/post/category')
def post_category():
    return 'Categories of posts'

@app.route('/post/view')
def post_view():
    return 'here will be post'

@app.route('/about')
def about():
    return 'information about Athor'

app.run(debug=True)
>>>>>>> 024623dd947361b8c6e2a93aef893f9e0babecab
