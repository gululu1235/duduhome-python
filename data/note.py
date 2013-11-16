import MySQLdb


class NoteDao(object):
    def __init__(self, config):
        self.table_name = 'notes'
        self.database_name = config.DATABASE_NAME
        self.database_user = config.DATABASE_USER
        self.database_pass = config.DATABASE_PASS
        self.database_host = config.DATABASE_HOST
        self.__connect()

    def __connect(self):
        self.db = MySQLdb.connect(host=self.database_host, user=self.database_user, passwd=self.database_pass,
                                  db=self.database_name, charset='utf8')

    def query(self, query, args=None):
        try:
            cursor = self.db.cursor()
            cursor.execute(query, args)
        except (AttributeError, MySQLdb.OperationalError):
            self.__connect()
            cursor = self.db.cursor()
            cursor.execute(query, args)
        return cursor

    def get_notes(self, id_from=None):
        if id_from == None:
            cursor = self.query('SELECT id, author, content, time FROM {0} ORDER BY time DESC LIMIT 20'.format(self.table_name))
        else:
            cursor = self.query('SELECT id, author, content, time FROM {0} WHERE id < {1} ORDER BY time DESC LIMIT 20'.format(self.table_name, id_from))
        result = []
        for row in cursor:
            result.append({
                'id': row[0],
                'author': row[1],
                'content': row[2],
                'time': row[3]
            })
        return result

    def put_note(self, note):
        self.query('INSERT INTO {0} (author, content) VALUES (%s, %s)'
                   .format(self.table_name), (note.get('author', ''), note.get('content', '')))
