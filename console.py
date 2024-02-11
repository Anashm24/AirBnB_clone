#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import ast
from models.base_model import BaseModel
<<<<<<< HEAD
from models import storage
import ast
=======
from models.engine.file_storage import FileStorage
from models import storage

>>>>>>> 5ed7f9613e0312cf833b6d7b40560ad24ee54dd8

class HBNBCommand(cmd.Cmd):
    """Represent the command interpreter"""

    prompt = "(hbnb) "
<<<<<<< HEAD
    
    

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
        elif not args:
            print(["{}".format(str(obj)) for obj in storage.all().values()])
        else:
            class_name = args[0]
            print(["{}".format(str(obj)) for key, obj in storage.all().items() if key.startswith(class_name)])
            
    
    def handle_custom_commands(self, class_name, action):
        """Handle custom commands like <class name>.all()
        or <class name>.count()."""
        parts = action.split("(")
        if len(parts) == 2 and parts[1].endswith(')'):
            action_name = parts[0]
            action_args = parts[1][:-1].split(',')

            # Remove surrounding quotes if present
            action_args = [arg.strip('\"') for arg in action_args]

            if action_name == 'show':
                key = f"{class_name}.{action_args[0]}"
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif action_name == 'all':
                instances = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(instances)
            elif action_name == 'count':
                count = sum(
                    1 for key in storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            else:
                print(f"Unrecognized action: {action_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {action}.\
            Type 'help' for assistance.\n")

    def default(self, line):
        """Handle unrecognized commands."""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action = parts
            self.handle_custom_commands(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")
            
=======
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
            else:
                print("** no instance found **")

>>>>>>> 5ed7f9613e0312cf833b6d7b40560ad24ee54dd8
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
<<<<<<< HEAD
        elif args[0] not in storage.CLASSES:
=======
        elif args[0] not in self.name_classes:
>>>>>>> 5ed7f9613e0312cf833b6d7b40560ad24ee54dd8
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
                key_att = args[2]
                val_att = args[3]

                val_att = ast.literal_eval(val_att)
                setattr(obj, key_att, val_att)
                storage.save()

<<<<<<< HEAD

    def do_EOF(self, line):
        """EOF command to exit the program"""
=======
    def do_EOF(self, line):
        """
        EOF: Also exits the program when receiving the EOF signal (Ctrl+D).
        Usage: (EOF signal)
        """
>>>>>>> 5ed7f9613e0312cf833b6d7b40560ad24ee54dd8
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
