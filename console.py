#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, args):
        """Exit on end-of-file (Ctrl-D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty lines."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
