#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """cmd line interpreter"""

    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def do_quit(self, line):
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
