#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


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
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
            inst.save()
            print(inst.id)

    def do_show(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] is not self.class_list:
            print("** class doesn't exist **")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            value = "{}.{}".format(cmds[0], cmds[1])
            if value in obj:
                print(obj[value])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] is not self.class_list:
            print("** class doesn't exist **")
        elif cmds[1] == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            value = "{}.{}".format(cmds[0], cmds[1])
            if value in obj:
                print(obj[value])
            else:
                print("** no instance found **")

    
    def do_all(self, arg):
        
        obj = storage.all()      
        cmnds = shlex.split(arg)
        
        if len(cmnds) == 0:
            for k, v in obj.items():
                print(str(v))
        elif cmnds[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            for k, v in obj.items():
                if k.split('.')[0] == cmnds[0]:
                    print(str(v))



            

if __name__ == '__main__':
    HBNBCommand().cmdloop()