class Component:

    def __init__(self, component_id, name, category_id, brand_id, store_id, price, description, stock_quantity, barcode):
        self.component_id = component_id
        self.name = name
        self.category_id = category_id
        self.brand_id = brand_id
        self.store_id = store_id
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity
        self.barcode = barcode

    def as_dict(self):
        return {
            'component_id': self.component_id,
            'name': self.name,
            'category_id': self.category_id,
            'brand_id': self.brand_id,
            'store_id': self.store_id,
            'price': self.price,
            'description': self.description,
            'stock_quantity': self.stock_quantity,
            'barcode': self.barcode
        }
