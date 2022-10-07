from flask import Flask, render_template, request, redirect, url_for

from modules import MySQLConnector

app = Flask(__name__)
mySQLConnector = MySQLConnector('root', 'cbr600rr', 'localhost', 3306, 'POKEMON')

@app.route('/')
def index():
  count = 10
  offset = request.args.get('offset')
  if offset:
    offset = int(offset)
  else:
    offset = 0
  rows = mySQLConnector.get_monsters(count=count, offset=offset)
  monsters = []
  for row in rows:
    monster = { 'id': row[0], 'name': row[1] }
    monsters.append(monster)

  return render_template(
    'index.html',
    monsters=monsters,
    count=count,
    offset=offset,
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
