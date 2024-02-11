#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Command to exit the program when Ctrl-D is pressed."""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()