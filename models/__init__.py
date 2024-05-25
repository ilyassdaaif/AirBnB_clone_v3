#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import models only after Base is defined to avoid circular imports
def initialize_models():
    from models.city import City
    from models.place import Place

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

initialize_models()
