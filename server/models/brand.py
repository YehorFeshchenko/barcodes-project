class Brand:

    def __init__(self, brand_id, name, description):
        self.brand_id = brand_id
        self.name = name
        self.description = description

    def as_dict(self):
        return {
            'brand_id': self.brand_id,
            'name': self.name,
            'description': self.description
        }
