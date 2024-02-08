import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

def do_quit(self, arg):
     """Command to exit the program."""
     return True

def do_EOF(self, arg):
    """Command to exit the program when Ctrl-D is pressed."""
    print()
    return True
def do_create(self, line):
    """Create a new object and save it.

    Args:
        line (str): The input line containing the class name.

    This method handles the 'create' command. It creates a new object of the specified
    class, saves it to the JSON file, and prints the id of the created object.
    If the class name is missing or doesn't exist, appropriate messages are printed.
    """

    """Check if the class name is missing"""
    if not line:
        print("** class name missing **")
        return

    """Get the class from the input line"""
    obj_cls = self.get_class_from_input(line)

    """Check if the class doesn't exist"""
    if obj_cls is None:
        print("** class doesn't exist **")
        return

    """Create a new object, save it, and print its id"""
    new_obj = obj_cls()
    new_obj.save()
    print(new_obj.id)

def do_show(self, line):
    """Print the string representation of an instance based on name and id."""
    class_name, obj_id = self.get_class_and_id_from_input(line)

    if not class_name:
        print("** class name missing **")
    elif not self.class_exists(class_name):
        print("** class doesn't exist **")
    elif not obj_id:
        print("** instance id missing **")
    else:
        key = "{}.{}".format(class_name, obj_id)
        saved_obj = storage.all().get(key, None)
        print("** aucune instance trouvée **" if saved_obj is None else saved_obj)

def do_destroy(self, line):
    """Deletes an instance based on the class name and id (save the change into the JSON file)."""
    """Extract the key from the command input"""
    key = self.get_obj_key_from_input(line)

    """Check if the key is missing, and return early if so"""
    if key is None:
        return

    """Retrieve the dictionary of all objects from storage"""
    obj_dict = storage.all()

    """Check if the key exists in the dictionary"""
    if key not in obj_dict:
        """Print message if the instance is not found"""
        print("** no instance found **")
    else:
        """Delete the entry corresponding to the key from the dictionary"""
        del obj_dict[key]
        """Save the changes to the JSON file"""
        storage.save()
