from flask import Flask, render_template

from modules import MySQLConnector

app = Flask(__name__)
mySQLConnector = MySQLConnector('root', 'cbr600rr', 'localhost', 3306, 'POKEMON')

@app.route('/')
def index():
  rows = mySQLConnector.get_monsters()
  monsters = []
  for row in rows:
    monster = { 'id': row[0], 'name': row[1] }
    monsters.append(monster)

  return render_template(
    'index.html',
    monsters=monsters,
  )

if __name__ == '__main__':
    app.run()
    mySQLConnector.disconnect()
