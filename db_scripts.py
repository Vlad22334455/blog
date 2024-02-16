<<<<<<< HEAD
import sqlite3

connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect('blog.db')
    cursor = connection.cursor()

def close():
    cursor.close()
    connection.close()

=======
import sqlite3

connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect('blog.db')
    cursor = connection.cursor()

def close():
    cursor.close()
    connection.close()

>>>>>>> 024623dd947361b8c6e2a93aef893f9e0babecab
