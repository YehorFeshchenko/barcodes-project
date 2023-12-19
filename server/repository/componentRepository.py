from ..db import get_db_connection


class ComponentRepository:

    @staticmethod
    def get_all_components():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM components')
        components = cur.fetchall()
        cur.close()
        conn.close()
        return components

    @staticmethod
    def get_component(component_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM components WHERE component_id = %s', (component_id,))
        component = cur.fetchone()
        cur.close()
        conn.close()
        return component

    @staticmethod
    def add_component(name, category_id, brand_id, store_id, price, description, stock_quantity, barcode):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO components (name, category_id, brand_id, store_id, price, description, stock_quantity, '
            'barcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (name, category_id, brand_id, store_id, price, description, stock_quantity, barcode))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_component(component_id, name, category_id, brand_id, store_id, price, description, stock_quantity,
                         barcode):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'UPDATE components SET name = %s, category_id = %s, brand_id = %s, store_id = %s, price = %s, description '
            '= %s, stock_quantity = %s, barcode = %s WHERE component_id = %s',
            (name, category_id, brand_id, store_id, price, description, stock_quantity, barcode, component_id))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_component(component_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM components WHERE component_id = %s', (component_id,))
        conn.commit()
        cur.close()
        conn.close()
