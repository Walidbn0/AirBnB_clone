#!/usr/bin/python3
import cmd
import importlib
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.class_dict = {
            'BaseModel': BaseModel,
            'User': User, 
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review, # Add User to the class dictionary
        }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def do_all(self, line):
        """Prints all string representations of instances based or not on the class name."""
        if line and line not in self.class_dict:  # Check if class exists
            print("** class doesn't exist **")
            return
        objects = storage.all()
        for obj_id, obj in objects.items():
            if not line or obj.__class__.__name__ == line:
                print(obj)

    def do_create(self, line):
        """Creates a new instance of BaseModel or User, saves it to the JSON file, and prints the id."""
        if line not in self.class_dict:
            print("** class doesn't exist **" if line else "** class name missing **")
            return
        new_obj = self.class_dict[line]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        if len(cls_and_id) == 0:
            print("** class name missing **")
            return
        elif len(cls_and_id.split(' ')) == 1:
            print("** instance id missing **")
            return
        elif cls_and_id.split(' ')[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        # create a key of the form <class name>.<id> to search in the storage
        user_key = cls_and_id.split(' ')[0] + '.' + cls_and_id.split(' ')[1]

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()

        # if the user input key is found in the storage, then print the object
        if user_key in all_objects.keys():
            print(all_objects[user_key])
            return

        # if we reach here, then the object is not found.
        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on class name and id."""
        args = line.split()
        if len(args) < 2 or args[0] not in self.class_dict:
            print("** class name missing **" if len(args) == 0 else "** class doesn't exist **" if args[0] not in self.class_dict else "** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
    def do_all(self, cls):
        if not line:
            result = storage.all().values()
        else:
            obj_cls = self.get_class_from_input(line)
            result = filter(lambda item: isinstance(item, obj_cls), storage.all().values())
            print([str(item) for item in result])

    def do_update(self, line):
        """Updates an instance based on class name and id by adding or updating an attribute."""
        args = line.split()
        if len(args) < 4 or args[0] not in self.class_dict:
            print("** class name missing **" if len(args) == 0 else "** class doesn't exist **" if args[0] not in self.class_dict else "** instance id missing **" if len(args) < 2 else "** attribute name missing **" if len(args) < 3 else "** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key, None)
        if obj:
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        else:
            print("** no instance found **")
    def do_count(self, line):
        """Counts the number of instances of a given class.
        """
        args = line.split()

        """Check if class name is missing"""
        if not args:
            print("** class name missing **")
            return

        """Extract class name from the input"""
        class_name = args[0]

        """Check if the class exists"""
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        """Get instances of the specified class from storage"""
        instances = storage.all().get(class_name, [])

        """Count the number of instances"""
        count = len(instances)

        """Print the count of instances"""
        print(count)
    def get_obj_key_from_input(self, line):
        """Parses and returns object key from input."""
        obj_cls = self.get_class_from_input(line)
        id_value = self.get_id_from_input(line)

        if obj_cls is None or id_value is None:
            return None

        return f"{obj_cls.__name__}.{id_value}"

    def get_class_from_input(self, line):
        """Parses and returns class from input."""
        cmds = line.split()

        if not cmds or len(cmds) < 1:
            print("** class name missing **")
            return None

        return self.get_class(cmds[0])

    def get_id_from_input(self, line):
        """Parses and returns id from input."""
        cmds = line.split()

        if len(cmds) < 2:
            print("** instance id missing **")
            return None

        return cmds[1]

    def get_attribute_name_value_pair(self, line):
        """Parses and returns a tuple of attribute name and value."""
        cmds = line.split()

        attr_name = cmds[2].strip('"') if len(cmds) > 2 else None
        if attr_name is None:
            print("** attribute name missing **")
            return None, None

        attr_val = cmds[3].strip('"') if len(cmds) > 3 else None
        if attr_val is None:
            print("** value missing **")
            return attr_name, None

        return attr_name, attr_val

    def get_class(self, name):
        """Returns a class from models module using its name."""
        try:
            sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
            module = importlib.import_module(f"models.{sub_module}")
            return getattr(module, name)
        except Exception:
            print("** class doesn't exist **")
            return None
    def default(self, line):
        if '.' not in line:
            return super().default(line)
        cls_name, func_name, id, args = self.parse_input(line)
        if cls_name is None:
            print("** class name missing **")
            return
        if func_name is None:
            print("** incorrect function (all, count, show, destroy & update) **")
            return
        id = id if id is not None else ""
        if func_name == "count":
            self.do_count(f"{cls_name} {id}")
        elif func_name == "all":
            self.do_all(line)  # Pass the original line
        elif func_name == "show":
            self.do_show(f"{cls_name} {id}")
        elif func_name == "destroy":
            self.do_destroy(f"{cls_name} {id}")
        elif func_name == "update":
            self.do_update(f"{cls_name} {id} {args}")
    def parse_input(self, input):
        args = input.split('.')
        if len(args) != 2:
            return None, None, None, None

        cls_name = args[0]
        valid_commands = ["all", "count", "show", "destroy", "update"]
        if '(' not in args[1] or ')' not in args[1]:
            return cls_name, None, None, None

        func_w_args = args[1].split("(")
        if len(func_w_args) == 0 or func_w_args[0] not in valid_commands:
            return cls_name, None, None, None
        func_name = func_w_args[0]
        f_args = func_w_args[1].strip(')')

        id_match = re.match(r'(^\"[\w-]+\")', f_args)
        if len(f_args) == 0 or id_match is None:
            return cls_name, func_name, None, None

        id = id_match.group()
        f_args = f_args.replace(id, "")
        id = id.strip('"')

        if len(f_args) == 0:
            return cls_name, func_name, id, ''

        dict_match = re.match(r'(\{.*\})', f_args.strip(", "))
        if dict_match is not None:
            dict_str = dict_match.group().replace("'", '"')
            return cls_name, func_name, id, json.loads(dict_str)

        f_args = f_args.replace(',', ' ')
        return cls_name, func_name, id, str(f_args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
