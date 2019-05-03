
class UserManager:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_user(self, login):
        return self.db_manager.get_user().objects(login=login)

    def change_user(self, user_info):
        user = self.db_manager.get_user().objects(login=user_info['login'])[0]
        user.name = user_info['name']
        user.surname = user_info['surname']
        user.age = user_info['age']
        user.email = user_info['email']
        user.password = user_info['password']
        user.save()