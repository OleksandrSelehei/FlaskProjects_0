import sqlite3


def search_series(title=str, series=int):
    db = sqlite3.connect('anim.db')
    c = db.cursor()
    title = title.upper()
    query = "SELECT * FROM content WHERE title LIKE '%' || ? || '%' AND series >= ?"
    c.execute(query, (title, series))
    content = c.fetchall()
    db.commit()
    db.close()
    return content


def search_voice(title=str, voice=str):
    db = sqlite3.connect('anim.db')
    c = db.cursor()
    title = title.upper()
    query = "SELECT * FROM content WHERE title LIKE '%' || ? || '%' AND voice LIKE '%' || ? || '%'"
    c.execute(query, (title, voice))
    content = c.fetchall()
    db.commit()
    db.close()
    return content


def search_none_voice(title=str):
    db = sqlite3.connect('anim.db')
    c = db.cursor()
    title = title.upper()
    query = "SELECT * FROM content WHERE title LIKE '%' || ? || '%'"
    c.execute(query, (title,))
    content = c.fetchall()
    db.commit()
    db.close()
    return content


if __name__ == '__main__':
    print(True)
