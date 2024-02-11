#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Represent the command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        new_instance = storage.CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{class_name}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{class_name}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""

        args = line.split()
        if args and args[0] not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if args:
            class_name = args[0]
            for key, obj in storage.all().items():
                if key.startswith(class_name):
                    print(obj)
        else:
            for obj in storage.all().values():
                print(obj)

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
