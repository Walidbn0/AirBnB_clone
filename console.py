#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        """Prints all string representations of instances."""
        if not line:
            objects = storage.all().values()
        else:
            if line not in ['BaseModel']:  # Add additional model names here
                print("** class doesn't exist **")
                return
            objects = [obj for obj in storage.all().values() if obj.__class__.__name__ == line]

        print([str(obj) for obj in objects])

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not line:
            print("** class name missing **")
            return
        if line != 'BaseModel':  # Extend this condition for other models
            print("** class doesn't exist **")
            return
        new_obj = BaseModel()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Shows the string representation of an instance based on class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1 or args[0] != 'BaseModel':  # Extend condition for other models
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
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1 or args[0] != 'BaseModel':  # Extend condition for other models
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
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
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] != 'BaseModel':  # Extend condition for other models
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
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
