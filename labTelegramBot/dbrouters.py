from .models import Lab, Student


class BotRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model != Lab and model != Student:
            return 'default'
        return 'telegramBot'

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model != Lab and model != Student:
            return 'default'
        return 'telegramBot'
