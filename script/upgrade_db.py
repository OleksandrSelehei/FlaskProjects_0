import sqlite3
from script import parser


def ongoing_update():
    data = parser.Parser_ongoing()
    db = sqlite3.connect('anim.db')
    c = db.cursor()
    for item in data:
        for content in item:
            c.execute("UPDATE content SET series = ? WHERE website = ? AND title = ?", (int(content[2]), content[0], content[1]))
    db.commit()
    db.close()
    return 'True'


def spot_update(veb_sait=str, title=str, series=int):
    db = sqlite3.connect('anim.db')
    c = db.cursor()
    c.execute("UPDATE content SET series = ? WHERE website = ? AND title = ?", (series, veb_sait, title))
    db.commit()
    db.close()
    return 'True'


if __name__ == '__main__':
    print(True)
    # print(spot_update("ANIMEVOST", "АДСКИЙ РАЙ", 5))
   #  conn = sqlite3.connect('anim.db')
   #  c = conn.cursor()
   #
   #  # Выполнить SQL-запрос для получения информации о столбцах
   #  table_name = 'content'  # Замените на имя вашей таблицы
   #  c.execute("PRAGMA table_info({})".format(table_name))
   #
   #  # Получить результат запроса
   #  columns = c.fetchall()
   #
   #  # Вывести имена столбцов
   #  for column in columns:
   #      print(column[1])
   #
   #  # Закрыть базу данных
   #  conn.close()
    conn = sqlite3.connect('../anim.db')
    c = conn.cursor()
    # c.execute("DELETE FROM content WHERE website = ?", ("JUT-SU.NET",))
    c.execute("SELECT * FROM content")
    result = c.fetchall()
    print(result)
    conn.commit()
    conn.close()