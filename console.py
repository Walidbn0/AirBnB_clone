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
if __name__ == '__main__':
    # Create an instance of HBNBCommand and start the command loop
    HBNBCommand().cmdloop()
