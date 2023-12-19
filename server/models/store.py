class Store:

    def __init__(self, store_id, name, address_id, phone, email):
        self.store_id = store_id
        self.name = name
        self.address_id = address_id
        self.phone = phone
        self.email = email

    def as_dict(self):
        return {
            'store_id': self.store_id,
            'name': self.name,
            'address_id': self.address_id,
            'phone': self.phone,
            'email': self.email
        }
