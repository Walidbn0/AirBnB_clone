#!/usr/bin/python3
"""Creates a unique FileStorage instance for the application"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User  # Ensure User is imported

storage = FileStorage()
storage.reload()
