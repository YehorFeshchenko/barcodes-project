class Address:

    def __init__(self, address_id, street, city, state, zip_code, country):
        self.address_id = address_id
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def as_dict(self):
        return {
            'address_id': self.address_id,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'country': self.country
        }
