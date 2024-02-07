#!/usr/bin/python3
import json
import os

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)
    
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(self.__file_path) and os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as f:
                loaded_objects = json.load(f)
                self.__objects = {key: self.get_class(key.split(".")[0])(**value)
                                  for key, value in loaded_objects.items()}

