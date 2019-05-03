
class HistoryManager:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_user_history(self, user_login):
        return self.db_manager.get_history().objects(user_login=user_login)

    def get_all_history(self):
        return self.db_manager.get_history().objects

    def add(self, **history_info):
        #warning
        history = self.db_manager.get_history()(**history_info)
        history.save()
