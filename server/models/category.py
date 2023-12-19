class Category:

    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description

    def as_dict(self):
        return {
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description
        }
