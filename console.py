#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_list = ["BaseModel", "Amenity", "City", "Place", 
                  "Review", "State", "User"]

    def help_help(self):
        """ Prints the help command's description """
        print("Provides description of a given command")

    def do_EOF(self, line):
        """Exits the program with ^D
        """

        print("")
        return True

    def do_quit(self, line):
        """Exits the program with quit command
        """

        return True

    def emptyline(self):
        """Do nothing with empty line
        """

        pass
    def do_create(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            inst = eval(f"{cmds[0]}()")
            storage.save()
            print(inst.id)

    def do_show(self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.class_list:
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
        """
        Delete instance based on the class name.
        Usage: destroy
        """
        cmnds = shlex.split(arg)

        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(cmnds) < 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            k = "{}.{}".format(cmnds[0], cmnds[1])
            if k in obj:
                del obj[k]
                storage.save()
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

    def do_update(self, arg):
        cmnds = shlex.split(arg)

        if len(cmnds) == 0:
            print("** class name missing **")
        elif cmnds[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(cmnds) == 1:
            print("** instance id missing **")
        else:

            obj = storage.all()

            k = "{}.{}".format(cmnds[0], cmnds[1])
            if k not in obj:
                print("** no instance found **")
            elif len(cmnds) == 2:
                print("** attribute name missing **")
            elif len(cmnds) == 3:
                print("** value missing **")
            else:
                ob = obj[k]
                atname = cmnds[2]
                atvalue = cmnds[3]
                try:
                    atvalue = eval(atvalue)
                except Exception:
                    pass
                setattr(ob, atname, atvalue)

                ob.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
