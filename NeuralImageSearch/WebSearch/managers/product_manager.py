
class ProductManager:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_product(self, id):
        return self.db_manager.get_product().objects(id=id)

    def change_product(self, product_info):
        product = self.db_manager.get_product().objects(id=product_info['id'])[0]
        product.name = product_info['name']
        product.url = product_info['url']
        product.image = product_info['image']
        product.encoding = product_info['encoding']
        product.save()

    def delete_product(self, id):
        product = self.db_manager.get_product().objects(id=id)[0]
        product.delete()

    def create_product(self, **product_info):
        #warning
        product = self.db_manager.get_product()(**product_info)
        product.save()
