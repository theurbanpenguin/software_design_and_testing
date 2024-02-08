from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class AllInOnePrinter(Printable, Scannable):
    def print(self):
        print("Print document.")

    def scan(self):
        print("Scan document.")

aio: AllInOnePrinter = AllInOnePrinter()
aio.print()
aio.scan()