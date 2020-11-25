
#implementation loosely based on GeeksforGeeks Python command implementation

class Command(object):
    def execute(self):
        pass

class Receiver(object):
    def __init__(self):
        self.setup="Is a reciever"

    def do_something(self):
        return

    def do_something_else(self):
        return


class simpleCommand(Command):
    def __init__(self):
        self._reciever=None

    def execute(self):
        return None


class ComplexCommand(Command):

    def __init__(self, Receiver, a):
        self._receiver = Receiver
        self._a = a
        #self._b = b

    def execute(self):
        if self._a==True:
            return self._receiver.do_something()
        else:
            return self._receiver.do_something_else()



class Controller:

    cmdOne = None
    cmdTwo = None

    def setcmdOne(self, Command):
        self.cmdOne = command

    def setcmdTwo(self, Command):
        self.cmdTwo = command

    def invoke(self):

        if isinstance(self.cmdOne, Command):
            return self.cmdOne.execute()

        if isinstance(self.cmdTwo, Command):
            return self.cmdTwo.execute()