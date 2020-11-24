
#implementation based on GeeksforGeeks Python command implementation

class Command(object):
    def execute(self):
        pass

class Receiver():
    def do_something(self, str):
        return

    def do_something_else(self, str):
        return

class simpleCommand(Command):
    def __init__(self):
        self._reciever=None


class ComplexCommand(Command):

    def __init__(self, Receiver, a, b):

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)



class Controller:

    cmdOne = None
    cmdTwo = None

    def setcmdOne(self, Command):
        self.cmdOne = command

    def setcmdTwo(self, Command):
        self.cmdTwo = command

    def invoke(self):

        if isinstance(self.cmdOne, Command):
            self.cmdOne.execute()

        if isinstance(self.cmdTwo, Command):
            self.cmdTwo.execute()