#!/usr/bin/python3
import cmd
import shlex
import ast
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Amenity", 
                  "Place", "Review", "State", "City"]
    
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
                    
    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objs = storage.all()

        cmnd = shlex.split(arg)

        if arg:
            cls = cmnd[0]

        count = 0

        if cmnd:
            if cls in self.class_list:
                for obj in objs.values():
                    if obj.__class__.__name__ == cls:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")


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
                curly_braces = re.search(r"\{(.*?)\}", arg)
                if curly_braces:
                    try:
                        str_data = curly_braces.group(1)

                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(arg_dict.k())
                        attribute_values = list(arg_dict.v())
                        try:
                            attr_name1 = attribute_names[0]
                            attr_value1 = attribute_values[0]
                            setattr(obj, attr_name1, attr_value1)
                        except Exception:
                            pass
                        try:
                            attr_name2 = attribute_names[1]
                            attr_value2 = attribute_values[1]
                            setattr(obj, attr_name2, attr_value2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attr_name = cmnds[2]
                    attr_value = cmnds[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(obj, attr_name, attr_value)

                ob.save()
                
if __name__ == '__main__':
    HBNBCommand().cmdloop()
