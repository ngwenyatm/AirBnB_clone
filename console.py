#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
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

        if len(tokens) < 2:
            print("** class name missing **")
            return
        elif len(tokens) < 3:
            print("** instance id missing **")
            return

        class_name, id = tokens

        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        instance = storage.get(class_name, id)

        if not instance:
            print("no instance found")
        else:
            print(instance.to_dict())

    def do_all(self, line):
        if line != "":
            args = line.split(' ')
            if args[0] not in self.classes():
                print("** class doesn't exist **")
            else:
                n_list = [str(obj) for key, obj in storage.all()
                      if type(obj).__name__ == args[0]]
                print(n_list)
        else:
            new_list = [str(obj) for key, obj in storage.all()]
            print(new_list)

    def do_destroy(self, line):
        tokens = line.split()

        if len(tokens) < 2:
            print("** class name missing **")
            return
        elif len(tokens) < 3:
            print("** instance id missing **")
            return

        class_name, id = tokens

        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        instance = storage.get(class_name, id)

        if not instance:
            print("no instance found")
        else:
            storage.delete(instance)
            storage.save()
            print("Done")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
