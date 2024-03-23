#!/usr/bin/python3
"""
This is a program that contains the entry point
of the command interpreter.
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
    """Entry point of command interpreter"""

    prompt = "(hbnb) "

    class_ls = ['User', 'City', 'Amenity', 'State',
                'Review', 'Place', 'BaseModel']

    classes = {'User': {'email': str, 'password': str, 'first_name': str,
                        'last_name': str},
               'City': {'state_id': str, 'name': str},
               'Amenity': {'name': str},
               'State': {'name': str},
               'Review': {'place_id': str, 'user_id': str, 'text': str},
               'Place': {'city_id': str, 'user_id': str, 'name': str,
                         'description': str, 'number_rooms': int,
                         'number_bathrooms': int, 'max_guest': int,
                         'price_by_night': int, 'latitude': float,
                         'longitude': float, 'amenity_ids': eval},
               'BaseModel': {'id': str, 'created_at': datetime,
                             'updated_at': datetime}}

    commands = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """Parses the input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            cnd[1] = cnd[1].replace("'", '"')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.class_ls \
                    and cnd[0] in HBNBCommand.commands:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

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

    def do_count(self, cls_name):
        """Counts the number of instances of a given class"""
        count = 0
        all_objects = storage.all()
        for k, v in all_objects.items():
            cls_nm = k.split('.')
            if cls_nm[0] == cls_name:
                count = count + 1
        print(count)

    def do_create(self, model_type):
        """creates an instance of a given class
        """

        if not model_type:
            print("** class name missing **")
        elif model_type not in HBNBCommand.class_ls:
            print("** class doesn't exist **")
        else:
            dic = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'Amenity': Amenity, 'Review': Review,
                   'City': City}
            obj = dic[model_type]()
            print(obj.id)
            obj.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.class_ls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.class_ls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """

        all_objects = storage.all()
        if not arg:
            object_ls = []
            for k in all_objects.keys():
                object_ls.append(str(all_objects[k]))
            print(object_ls)
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.class_ls:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            object_ls = []
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                if obj_name == args[0]:
                    object_ls += [v.__str__()]
            print(object_ls)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a += argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.class_ls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                obj_name = v.__class__.__name__
                obj_id = v.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(v, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")


def get_value(args):
    """ gets attribute's value passed inside double quotes """

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