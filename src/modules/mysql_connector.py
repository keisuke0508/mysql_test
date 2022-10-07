import mysql.connector

class MySQLConnector:

  conn = None
  cursor = None

  def __init__(self, user, password, host, port, database):
    self.conn = self.connect(user, password, host, port, database)
    if self.is_connected:
      self.conn.ping(reconnect=True)
      self.cursor = self.conn.cursor()

  def is_connected(self):
    return self.conn is not None and self.conn.is_connected()

  def connect(self, user, password, host, port, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
        return conn
    except Exception as e:
        print(e)

  def disconnect(self):
    if self.is_connected():
      self.cursor.close()
      self.conn.close()

  def get(self, sql):
    if self.cursor is not None:
      self.cursor.execute(sql)
      return self.cursor.fetchall()

  def set(self, sql, data):
    if self.cursor is not None:
      self.cursor.executemany(sql, data)
      self.conn.commit()
  
  def udpate(self, sql, data):
    if self.cursor is not None:
      self.cursor.executemany(sql, data)
      self.conn.commit()
  
  def delete(self, sql):
    if self.cursor is not None:
      self.cursor.execute(sql)
      self.conn.commit()
    
  def get_monsters(self, count=10, offset=10):
    print(count, offset)
    sql = 'SELECT * FROM monsters ORDER BY id ASC LIMIT {count} OFFSET {offset}'.format(count=count, offset=offset)
    return self.get(sql)

  def set_monster(self, _id, name):
    sql = 'INSERT INTO monsters (id, name) VALUES (%s, %s)'
    data = [(_id, name)]
    self.set(sql, data)
  
  def update_monster(self, _id, name):
    sql = 'UPDATE monsters set name=%s WHERE id=%s'
    data = [(name, _id)]
    self.udpate(sql, data)

  def delete_monster(self, _id):
    sql = 'DELETE FROM monsters WHERE id = {id}'.format(id=_id)
    self.delete(sql)
    