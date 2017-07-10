from flask import Flask, render_template, request
from mstranslator import Translator
translator = Translator("YOUR_ACCESS_KEY")
app = Flask(__name__)

import sqlite3 as sql


@app.route('/')
def translator_home():
    return render_template("translator.html")


@app.route('/forward/', methods = ['POST'])
def addrec():
    conn = sql.connect("database.db")
    cur = conn.cursor()
    if request.form['tl']=="英語に翻訳する":
        original = request.form['inputform']
        translated = translator.translate(original, lang_from='ja', lang_to='en')
        japanese = original
        english = translated
        cur.execute("INSERT INTO db (日本語,English) VALUES (?,?)", (japanese,english))
        conn.commit()
        conn.close()
        return render_template("translator.html", original=original, translated=translated)
    elif request.form['tl']=="Translate to Japanese":
        original = request.form['inputform']
        translated = translator.translate(original, lang_from='en', lang_to='ja')
        english = original
        japanese = translated
        cur.execute("INSERT INTO db (日本語,English) VALUES (?,?)", (japanese,english))
        conn.commit()
        conn.close()
        return render_template("translator.html", original=original, translated=translated)
    else:
        pass

@app.route('/db')
def db():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM db")

    rows = cur.fetchall();    
    return render_template("db.html", rows=rows)
    conn.close()


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
