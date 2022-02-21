from flask import Flask as flask
from flask import render_template as html
import sqlite3 as db

app = flask(__name__)



@app.route('/')
def index():
     conn = db.connect('dist/db.sqlite')
     cur = conn.cursor()


     cur.execute("""select hello , about ,img_me from main""")
     my = []
     for hi, me, pic_me in cur.fetchall():
        my.append(
            {
            'hello':hi,
            'about':me,
            'pic_me':pic_me
            }
        )

     context = {'stori': my}


     conn.close()

     return html('index.html', **context)


@app.route('/open_sorce/')
def new():
    return html('git.html')

@app.route('/blog/')
def blog():
    conn = db.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("""select stori1_img, stori1, stori2_img, stori2, fact1, fact2, fact3, fact4  from blog;""")
    stories = []
    for storis1_img, storis1, storis2_img, storis2, facts1, facts2, facts3, facts4 in cur.fetchall():
        stories.append({'stori1_pic':storis1_img, 'stori1':storis1, 'stori2_pic':storis2_img, 'stori2':storis2,'fact1':facts1, 'fact2':facts2, 'fact3':facts3, 'fact4':facts4 })

    context = {'stori':  stories}

    conn.close()



    return html('my_blog.html', **context)


if __name__ == '__main__':
    app.run()


