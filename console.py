#!/usr/bin/python3
"""
airbnb console
Functions and Classes:
    class HBNBCommand(cmd.Cmd):
"""


import cmd
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    list_class = ['User', 'City', 'Amenity', 'State',
                'Review', 'Place', 'BaseModel']

    cmnds = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """Parses the input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            cnd[1] = cnd[1].replace("'", '"')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.list_class \
                    and cnd[0] in HBNBCommand.cmnds:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Print helps"""
        print("Provides description of a given command")

    def do_quit(self, line):
        """Exits with quit command"""
        return True

    def do_EOF(self, line):
        """Exits the program with EOF"""
        print("")
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_count(self, arg):
        """Counts the number of instances"""
        count = 0
        all_obj = storage.all()
        for key, value in all_obj.items():
            cls_nm = key.split('.')
            if cls_nm[0] == arg:
                count = count + 1
        print(count)

    def do_create(self, arg):
        """creates an instance"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            disc = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'Amenity': Amenity, 'Review': Review,
                   'City': City}
            obj = disc[arg]()
            print(obj.id)
            obj.save()

    def do_show(self, arg):
        """Prints the string representation"""
        if not arg:
            print("** class name missing **")
            return

        arguments = arg.split(' ')

        if arguments[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == arguments[0] and obj_id == arguments[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        if not arg:
            print("** class name missing **")
            return

        arguments = arg.split(' ')

        if arguments[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            for key, Value in objs.items():
                obj_name = Value.__class__.__name__
                obj_id = Value.id
                if obj_name == arguments[0] and obj_id == arguments[1].strip('"'):
                    del Value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation"""
        all_obj = storage.all()
        if not arg:
            obj_ls = []
            for k in all_obj.keys():
                obj_ls.append(str(all_obj[k]))
            print(obj_ls)
            return

        arguments = arg.split(' ')

        if arguments[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            obj_ls = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == arguments[0]:
                    obj_ls += [value.__str__()]
            print(obj_ls)

    def do_update(self, arg):
        """Updates an instance"""
        if not arg:
            print("** class name missing **")
            return
        empty = ""
        for argv in arg.split(','):
            empty += argv

        args = shlex.split(empty)

        if args[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")


    def get_value(args):
        """ gets attribute's value"""

        if args:
            if args[0].startswith('"'):
                tmp = ' '.join(args)
                my_l = tmp.split('"')
                for i in my_l:
                    if i != "":
                        return i
            else:
                return args[0]


if __name__ == '__main__':
    HBNBCommand().cmdloop()