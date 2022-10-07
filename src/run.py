from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/new_monster')
def new_monster():
  _id = request.args.get('id')
  name = request.args.get('name')
  mySQLConnector.set_monster(_id, name)
  return redirect(url_for('index'))

@app.route('/update_monster')
def update_monster():
  _id = request.args.get('id')
  name = request.args.get('name')
  mySQLConnector.update_monster(_id, name)
  return redirect(url_for('index'))

@app.route('/delete_monster')
def delete_monster():
  _id = request.args.get('id')
  mySQLConnector.delete_monster(_id)
  return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
    mySQLConnector.disconnect()
