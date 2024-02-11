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

        """
        all [class_name]: Prints all instances of a specified class,
        or all known instances if no class is specified.

        Usage: all or all ClassName

        """
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
        """
        create [class_name]: Creates a new instance of a specified class,
        saves it to the file storage, and prints the new instance's id.
        Currently, it creates instances of BaseModel by default.
        Usage: create ClassName
        """
        if line in self.name_classes:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        show [class_name] [instance_id]: Prints the string
        representation of an instance based on the class name and id.
        Usage: show ClassName instance_id
        """
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
        """
        destroy [class_name] [instance_id]: Deletes an instance based
        on the class name and id, and saves the change into the file storage.
        Usage: destroy ClassName instance_id
        """
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
        """
        update [class_name] [instance_id] [attribute_name] [attribute_value]:
        Updates an instance by adding or updating an attribute
        (with the attribute's value) and saves the change to the file storage.
        Usage: update ClassName instance_id attribute_name attribute_value
        """
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
        """
        EOF: Also exits the program when receiving the EOF signal (Ctrl+D).
        Usage: (EOF signal)
        """
        print()
        return True

    def do_quit(self, line):
        """
        quit: Exits the program.

        Usage: quit
        """
        return True

    def emptyline(self):
        """
        Empty line: Entering an empty line followed
        by ENTER does not execute anything.
        Usage: (just press ENTER on an empty line)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
