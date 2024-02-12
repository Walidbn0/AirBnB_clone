#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
            'Review': Review,
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
        objects = storage.all()
        obj_list = []
        for obj_id, obj in objects.items():
            if not line or obj.__class__.__name__ == line:
                obj_list.append(obj.__str__())
        print(obj_list) if obj_list else print("** class doesn't exist **" if line and line not in self.class_dict else "[]")

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not line:
            print("** class name missing **")
            return
        try:
            if line not in self.class_dict:
                raise NameError
            new_obj = self.class_dict[line]()
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Shows the string representation of an instance based on class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.all().get(f"{args[0]}.{args[1]}", None)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
