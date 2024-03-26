#!/usr/bin/python3
"""Defines a module for HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """cmd line interpreter"""

    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "Amenity",
               "Place", "Review", "State", "City"]

    def do_quit(self, line):
        """Quit command to exist console"""
        return True

    def help_quit(self, line):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        tokens = line.split()
        if line == "" or line is None:
            print("** class name missing **")
            return
        elif tokens[0] != "BaseModel":
            print("** class doesn't exist **")

            obj = eval(tokens[0])()
            obj.save
            print(obj.id)

    def do_show(self, line):

        tokens = line.split()

        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            obj = storage.all()
            key = "{}.{}".format(tokens[0], tokens[1])

            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        if line != "" or None:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                n_list = [str(obj) for key, obj in storage.all()
                          if type(obj).__name__ == args[0]]
                print(n_list)
        else:
            new = [str(obj) for key, obj in storage.all()]
            print(new)

    def do_destroy(self, line):
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) < 2:
            print("** instance id missing **")
            return
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            key = "{}.{}".format(tokens[0], tokens[1])
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, args):
        storage.reload()
        args = line.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
            key = "{}.{}".format(tokens[0], tokens[1])
            dct = storage.all()
        try:
            obj_val = dct[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            att = type(getattr(obj_val, args[2]))
            args[3] = att(args[3])
        except AttributeError:
            pass
        setattr(obj_val, args[2], args[3])
        obj_val.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
