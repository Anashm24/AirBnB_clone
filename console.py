#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    name_classes = {type(obj).__name__ for obj in storage.all().values()}

    def do_all(self, line):
        """Prints all instances of a specified class or all known instances if no class is specified."""

        objects = []

        if not line:
            for obj_id, obj in storage.all().items():
                objects.append(str(obj))
        elif line in self.name_classes:
            for obj_id, obj in storage.all().items():
                if obj.__class__.__name__ == line:
                    objects.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        print(objects)


    def do_create(self, line):
        """Creates a new instance of a specified class with optional attributes, saves it, and prints the id."""

        if line in self.name_classes:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.name_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = f"{args[0]}.{args[1]}" 
            if obj_key in storage.all():
                 print(storage.all()[obj_key])
            else:
                print("** no instance found **")
    
    def do_destroy(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in self.name_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = f"{args[0]}.{args[1]}" 
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
                print("** instance deleted successfully **")
            else:
                print("** no instance found **")

    def do_update(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.name_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            obj_key = f"{args[0]}.{args[1]}"
            if obj_key not in storage.all():
                print("** no instance found **")
                return
            else:
                obj = storage.all()[obj_key]
                setattr(obj, args[2], args[3])
                storage.save()


    def do_EOF(self, line):
        """EOF command to exit the program"""

        print()
        return True
    
    def do_quit(self, line):
        """quit command to exit the program"""

        return True
    
    def emptyline(self):
        """an empty line + ENTER should not execute anything"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
