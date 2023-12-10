#!/usr/bin/python3
"""This is the Module  for the command interpreter"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing if empty input."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program.
            params:
                arg(args): the argument for quiting
        """
        return True

    def help_quit(self):
        """the help message for the quit command."""

        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the program."""
        print()
        return True

    def help_EOF(self):
        """Help message for EOF."""
        print("EOF to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel.
            params:
                arg(args): argument rep the class name
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance.
            params:
                arg(args): argument alongside command
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = eval(args[0]).__name__
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        objects = models.storage.all()

        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
            params:
                arg(args): argument to be used with cmd
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = eval(args[0]).__name__
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        objects = models.storage.all()

        if key in objects:
            del objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        objects = models.storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = eval(args[0]).__name__
                print([
                    str(obj)
                    for k, obj in objects.items() if k.startswith(class_name)
                    ])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        objects = models.storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')

        obj = models.storage.all()[key]
        setattr(obj, attribute_name, attribute_value)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
