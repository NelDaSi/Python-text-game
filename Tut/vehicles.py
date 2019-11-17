class Vehicle():
    def __init__(self):
        raise NotImplementedError("Do not create raw Vehicle objects.")

    def __str__(self):
        return str(self.name) + ' ' + str(self.wheels) + ' ' + 'wheels'


class Motorcycle(Vehicle):

    def __init__(self):
        self.name = 'Honda CBR'
        self.wheels = 2


class car(Vehicle):

    def __init__(self):
        self.name = 'Tesla'
        self.wheels = 4


def show_vehicles():
    vehicles_list = [car(), Motorcycle()]
    for vehicle in vehicles_list:
        print('*' + str(vehicle))


show_vehicles()
