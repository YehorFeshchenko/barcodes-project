from ..db import get_db_connection


class ComponentRepository:

    @staticmethod
    def get_all_components():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM components')
        columns = [col[0] for col in cur.description]
        components = [dict(zip(columns, row)) for row in cur.fetchall()]
        cur.close()
        conn.close()
        return components

    @staticmethod
    def get_all_components_with_details():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            SELECT 
                c.component_id, c.name AS component_name, c.price, c.description AS component_description, 
                c.stock_quantity, c.barcode, c.category_id, c.brand_id, c.store_id,
                cat.category_id, cat.name AS category_name, cat.description AS category_description,
                br.brand_id, br.name AS brand_name, br.description AS brand_description,
                st.store_id, st.name AS store_name, st.phone AS store_phone, st.email AS store_email, st.address_id,
                ad.address_id, ad.street, ad.city, ad.state, ad.zip_code, ad.country
            FROM components c
            JOIN categories cat ON c.category_id = cat.category_id
            JOIN brands br ON c.brand_id = br.brand_id
            JOIN stores st ON c.store_id = st.store_id
            JOIN addresses ad ON st.address_id = ad.address_id
        ''')
        columns = [col[0] for col in cur.description]
        components = [dict(zip(columns, row)) for row in cur.fetchall()]
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
            'barcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING component_id',
            (name, category_id, brand_id, store_id, price, description, stock_quantity, barcode))
        component_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return component_id

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
