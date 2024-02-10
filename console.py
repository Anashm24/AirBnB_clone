#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
import models.engine.file_storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    
    def do_all(self, line):
        if line == "BaseModel" or line == None:
            print(eval(line).FileStorage.all())
        else:
            print("** class doesn't exist **")
        
    def do_create(self, line):
        if line == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        elif not line:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    
    def do_quit(self, line):
        """quit command to exit the program"""
        return True
    
    def emptyline(self):
        """an empty line + ENTER should not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
