import json
import os
from models.base_model import BaseModel
from models.user import User  # Ensure User is imported

class FileStorage:
    """FileStorage is a class that serializes instances to a JSON file and deserializes JSON file to instances:"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    """ def save(self):
        Serializes __objects to a JSON file
        srz_objects = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(srz_objects, file)"""
    
    def save(self, obj=None):
        """Serializes __objects to a JSON file. Optionally updates a single object."""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj
        srz_objects = {key: val.to_dict() for key, val in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(srz_objects, file)

    """def reload(self):
        Deserialize the JSON file __file_path to an __objects, if it exists.
        if os.path.isfile(self.__file_path) and os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as file:
                ld_objects = json.load(file)
                self.__objects = {key: self.get_class(key.split(".")[0])(**val)
                                  for key, val in ld_objects.items()}"""
    
    def reload(self):
        """Deserializes the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(self.__file_path) and os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as file:
                ld_objects = json.load(file)
                for key, value in ld_objects.items():
                    if key not in self.__objects:  # Prevent duplicate objects
                        class_name = key.split(".")[0]
                        cls = self.get_class(class_name)  # Dynamically get the class
                        self.__objects[key] = cls(**value)

    def get_class(self, class_name):
        """Dynamically returns a class based on the class name."""
        if class_name in globals():
            return globals()[class_name]
        else:
            raise Exception(f"Class {class_name} not found.")