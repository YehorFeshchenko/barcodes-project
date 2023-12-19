from server.db import get_db_connection


class CategoryRepository:

    @staticmethod
    def add_category(name, description):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO categories (name, description) VALUES (%s, %s) RETURNING category_id',
                    (name, description))
        category_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return category_id

    @staticmethod
    def get_category(category_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM categories WHERE category_id = %s', (category_id,))
        category = cur.fetchone()
        cur.close()
        conn.close()
        return category
