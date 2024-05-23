import sqlite3


class SqlConnector:

    cursor = None
    conn = None
    @staticmethod
    def init():
        SqlConnector.conn = sqlite3.connect('db/data.db')
        SqlConnector.cursor = SqlConnector.conn.cursor()
        SqlConnector.create_permanent_table()
        SqlConnector.create_records_table()

    @staticmethod
    def create_permanent_table():
        query = '''CREATE TABLE IF NOT EXISTS permanent(
                        id        INTEGER PRIMARY KEY AUTOINCREMENT,
                        tg_id     TEXT    UNIQUE NOT NULL,
                        user_name TEXT,
                        attack    INTEGER,
                        hp        INTEGER
                    );'''
        SqlConnector.cursor.execute(query)

    @staticmethod
    def create_records_table():
        query = '''CREATE TABLE IF NOT EXISTS records(
                    id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    tg_id      INTEGER NOT NULL REFERENCES permanent (tg_id),
                    room_count INTEGER NOT NULL,
                    kill_count INTEGER NOT NULL,
                    points     INTEGER NOT NULL,
                    run_count  INTEGER NOT NULL
                );'''
        SqlConnector.cursor.execute(query)

    @staticmethod
    def add_user(tg_id, name):
        query = f'''INSERT INTO permanent('tg_id', 'user_name', 'attack', 'hp')
                    VALUES ('{tg_id}', '{name}', 0, 0)'''
        SqlConnector.cursor.execute(query)
        SqlConnector.conn.commit()

    @staticmethod
    def update_user(tg_id, attack, hp):
        query = f'''UPDATE permanent
                    SET attack = {attack}, 
                        hp = {hp}
                    WHERE tg_id = '{tg_id}' '''
        SqlConnector.cursor.execute(query)
        SqlConnector.conn.commit()

    @staticmethod
    def read_user(tg_id):
        query = f'''SELECT user_name, attack, hp
                    FROM permanent
                    WHERE tg_id = '{tg_id}' '''
        response = SqlConnector.cursor.execute(query).fetchone()
        return response

    @staticmethod
    def add_record(tg_id, r_c, k_c, p, runs):
        query = f'''INSERT INTO records('tg_id', 'room_count', 'kill_count', 'points', 'run_count')
                    VALUES ('{tg_id}', '{r_c}', '{k_c}', '{p}','{runs}')'''
        SqlConnector.cursor.execute(query)
        SqlConnector.conn.commit()

    @staticmethod
    def read_stat_for_user(tg_id):
        query = f'''SELECT (SELECT user_name FROM permanent WHERE tg_id='{tg_id}') as user_name, 
                            room_count, kill_count, points, run_count
                    FROM records
                    WHERE tg_id = '{tg_id}' 
                    ORDER BY points DESC'''
        response = SqlConnector.cursor.execute(query).fetchmany(10)
        return response

    @staticmethod
    def read_stat_by_points():
        query = f'''SELECT (SELECT user_name FROM permanent WHERE tg_id=r.tg_id) as user_name, 
                            room_count, kill_count, MAX(points), run_count
                    FROM records r 
                    GROUP BY tg_id
                    ORDER BY points DESC'''
        response = SqlConnector.cursor.execute(query).fetchmany(10)
        return response


if __name__ == '__main__':
    SqlConnector.init()
    # a.add_user('12234', 'Vasya')
    # a.update_user('Vasya', 5, 10)
    # my_print(SqlConnector.read_stat_by_points())
    # a.add_record('12234', 55, 16, 352, 3)
    # a.add_user('OLEG', 'OLEG')
    # a.add_user('123', '123')
    # a.add_user('r', 'r')
    # a.add_record('r', 51, 1412346, 5, 31)
    # a.add_record('r', 52142, 11231, 14, 31)
    # my_print(SqlConnector.read_stat_by_points())
