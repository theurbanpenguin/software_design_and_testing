class Bird:
    def fly(self):
        print("The bird is flying.")

class Duck(Bird):
    def fly(self):
        print("The duck flaps its wings.")

class Ostrich(Bird):
    def fly(self):
        print("Ostriches cannot fly, but run well.")

duck: Duck = Duck()
duck.fly()

ostrich: Ostrich = Ostrich()
ostrich.fly()