from server.db import get_db_connection


class BrandRepository:

    @staticmethod
    def add_brand(name, description):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO brands (name, description) VALUES (%s, %s) RETURNING brand_id',
                     (name, description))
        brand_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return brand_id

    @staticmethod
    def get_brand(brand_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM brands WHERE brand_id = %s', (brand_id,))
        brand = cur.fetchone()
        cur.close()
        conn.close()
        return brand
