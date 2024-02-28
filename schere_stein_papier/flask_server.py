from flask import Flask, request
import sqlite3

app = Flask(__name__)


def create_table():
    connection = sqlite3.connect("stein_schere.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT, "
                   "value INTEGER)")
    connection.commit()
    connection.close()


def insert_data(key, value):
    connection = sqlite3.connect("stein_schere.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data (key, value) VALUES (?, ?)", (key, value))
    connection.commit()
    connection.close()


@app.route('/', methods=['POST'])
def handle_json():
    data = request.json
    print(data)

    count_player = data.get("count_Player")
    count_comp = data.get("count_Comp")
    symbol_counts = data.get("symbol_counts")

    # Daten in die Datenbank einfügen
    insert_data("count_Player", count_player)
    insert_data("count_Comp", count_comp)
    for symbol, count in symbol_counts.items():
        insert_data(symbol, count)

    return "Daten erfolgreich in die Datenbank eingefügt."


if __name__ == '__main__':
    create_table()
    app.run()

