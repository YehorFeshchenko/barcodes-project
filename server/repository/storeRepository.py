from server.db import get_db_connection


class StoreRepository:

    @staticmethod
    def add_store(name, address_id, phone, email):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO stores (name, address_id, phone, email) VALUES (%s, %s, %s, %s) RETURNING store_id',
                     (name, address_id, phone, email))
        store_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return store_id

    @staticmethod
    def get_store(store_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM stores WHERE store_id = %s', (store_id,))
        store = cur.fetchone()
        cur.close()
        conn.close()
        return store
