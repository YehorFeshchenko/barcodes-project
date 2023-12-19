from server.db import get_db_connection


class AddressRepository:

    @staticmethod
    def add_address(street, city, state, zip_code, country):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO addresses (street, city, state, zip_code, country) VALUES (%s, %s, %s, %s, %s) RETURNING address_id',
                     (street, city, state, zip_code, country))
        address_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return address_id

    @staticmethod
    def get_address(address_id):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM addresses WHERE address_id = %s', (address_id,))
        address = cur.fetchone()
        cur.close()
        conn.close()
        return address
