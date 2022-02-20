import  sqlite3 as db 

conn = db.connect('src/db.sqlite')

cur = conn.cursor()

# init 

def db (name):
    if name == "all":
        #main
        cur.execute(
        """create table main(
        id  integer
            primary key autoincrement,
        hello text,
        about text,
        img_me text
        );"""
        )
        cur.execute("""insert into main (hello, about, img_me) values ('АВТОР: Сергеев Алексей' , 'Привет ,меня зовут Лёша, мне 11 лет. Я живу в Санкт-Петербурге. Я хочу стать python 🐍 и web разаботчиком', '"../static/img/Web_site_author.jpg"')""")

        #blog
        cur.execute(
        """create table blog(
        id  integer
            primary key autoincrement,
        stori1_img text,
        stori1 text,
        stori2_img text,
        stori2 text,
        fact1 text,
        fact2 text,
        fact3 text,
        fact4 text
        );"""
        )

        cur.execute("""insert into blog (stori1_img, stori1, stori2_img, stori2, fact1, fact2, fact3, fact4) values 
        ('../static/img/stori1.jpg',
         'Первый Macintosh',
         '../static/img/stori2.jpg',
         'Скоько у пиявок мозгов? если думали что 1 мозг ,то это миф',
         'macintoch 128k',
         'был представлен 24 января 1984 года.',
         'На клавиатуре macintoch 128k небыло стрелок',
         'Первый mac стоил 2495 $'
        )""")

        conn.commit()
        conn.close()

    elif name == "blog":
        cur.execute(
        """create table blog(
        id  integer
            primary key autoincrement,
        stori1_img text,
        stori1 text,
        stori2_img text,
        stori2 text,
        fact1 text,
        fact2 text,
        fact3 text,
        fact4 text
        );"""
        )

        cur.execute("""insert into blog (stori1_img, stori1, stori2_img, stori2, fact1, fact2, fact3, fact4) values 
        ('../static/img/stori1.jpg',
         'Первый Macintosh',
         '../static/img/stori2.jpg',
         'Скоько у пиявок мозгов? если думали что 1 мозг ,то это миф',
         'macintoch 128k',
         'был представлен 24 января 1984 года.',
         'На клавиатуре macintoch 128k небыло стрелок',
         'Первый mac стоил 2495 $'
        )""")

        conn.commit()
        conn.close()
        
    elif name == "main":
        cur.execute(
        """create table main(
        id  integer
            primary key autoincrement,
        hello text,
        about text,
        img_me text
        );"""
        )
        cur.execute("""insert into main (hello, about, img_me) values ('АВТОР: Сергеев Алексей' , 'Привет ,меня зовут Лёша, мне 11 лет. Я живу в Санкт-Петербурге. Я хочу стать python 🐍 и web разаботчиком', '"../static/img/Web_site_author.jpg"')""")

        conn.commit()
        conn.close()

r_n= input("that table you need recover?   blog/main/all:  ")

if r_n == "all":
    db(r_n)
elif r_n == "blog":
    db(r_n)
elif r_n == "main":
    db(r_n)


