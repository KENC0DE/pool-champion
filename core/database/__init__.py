""" Initialize the database """
from core.database.storage import Storage

storage = Storage()
storage.load()
