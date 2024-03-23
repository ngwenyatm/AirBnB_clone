#!/usr/bin/python3
import cmd
import json

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
       " ""do nothing"""
        pass

    def do_quit(self, line):
        """exits the program"""
        return True

    def do_EOF(self, line):
        """handles EOF"""
        return True

    def do_help(self, line):
        """keep this updated"""
        pass
   """ 
    def do_create(self, line):
        tokens = line.split()
        
        if len(tokens) < 2:
            print("** class name missing **")
            return
        elif line not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            model_class = models.BaseModel
            all_objects = storage.all()
            new_id = 1

        while str(new_id) in all_objects:
            new_id += 1

        new_instance = model_class(id=new_id)
        storage.save()
        print(new_instance.id)

    def do_show(self,line):
        args = line.split()
        
        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 3:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[2]
            try:
                instance = storage.get(class_name, instance_id)
                print(instance)
            except KeyError:
                print("** no instance found **")
    """
    if __name__ == "__main__":
        HBNBCommand().cmdloop()
