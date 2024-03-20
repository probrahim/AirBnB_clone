#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    
    """
    prompt = "(hbnb) "
    
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()