
class InvalidOperationError(Exception): #this is a custom exception, all custom exceptions should end with Error, and be derived from the (Exception) class
    pass

class Stream:

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.open = False


class FileStream(Stream):
    def read(self):
        print("reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")

