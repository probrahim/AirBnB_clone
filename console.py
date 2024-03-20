#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel"]
    
    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print(" ")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("")

    def emptyline(self):
        pass

    def do_create(self, arg):
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()