import psycopg2


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            "postgresql://myuser:mypassword@localhost:5432/mydatabase"
        )

    def query(self, sql, params=None):
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            if cur.description:
                return cur.fetchall()
            self.conn.commit()


db = Database()
