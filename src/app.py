from flask import Flask 
from flask import render_template as html
import sqlite3 as db

app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
     conn = db.connect('dist/db.sqlite')
=======
     conn = db.connect('./dist/db.sqlite')
>>>>>>> 1e40c2a1de5971d2dbfab03c202d04720cac147d
     cur = conn.cursor()


     cur.execute("""select hello , about from main""")
     my = []
     for hi, me in cur.fetchall():
        my.append({'hello':hi, 'about':me})

     context = {'stori': my}


     conn.close()

     return html('index.html', **context)


<<<<<<< HEAD
@app.route('/open_sorce/')
def new():
    return html('git.html')

=======
>>>>>>> 1e40c2a1de5971d2dbfab03c202d04720cac147d
@app.route('/blog/')
def blog():
    conn = db.connect('./dist/db.sqlite')
    cur = conn.cursor()
    cur.execute("""select stori1, stori2, fact1, fact2, fact3, fact4  from blog where visible == ?;""", (True,))
    stories = []
    for storis1, storis2, facts1, facts2, facts3, facts4 in cur.fetchall():
        stories.append({'stori1':storis1, 'stori2': storis2 ,'fact1': facts1, 'fact2':facts2, 'fact3':facts3, 'fact4':facts4})

    context = {'stori':  stories}

    conn.close()



    return html('my_blog.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
