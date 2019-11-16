class Weapon:
    def __str__(self):
        return str(self.name) + "(" + str(self.amount) + ")"

class PortalGun(Weapon):
    def __init__(self):
        self.name = "Portal Gun"
        self.description = "The Portal Gun is a gadget that allows the user(s) \n\tto travel between different universes/dimensions/realities."
        self.damage = 100
        self.amount = 1

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.amount = 1
        
class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. Somewhat more dangerous than a rock."
        self.damage = 10
        self.amount = 1
            
class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, but still has some fight in it."
        self.damage = 20
        self.amount = 1
        
class Gold:
    def __init__(self):
        self.name = "Gold"
        self.description = "Ingot made of gold."
        self.amount = 5
        
    def __str__(self):
        return str(self.name) + "(" + str(self.amount) + ")"
        
class CrustyBread:
    def __init__(self):
        self.name = "Crusty Bread"
        self.description = "Crusty Bread"
        self.amount = 3
        
    def __str__(self):
        return str(self.name) + "(" + str(self.amount) + ")"


def play():
    inventory = [Dagger(), PortalGun(), RustySword(), Rock(), Gold(), CrustyBread()]
    print("Escape from Cave Terror! ")
    while True:
        action_input =   get_player_command()  
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West!")
        elif action_input in ['i', 'I']:
            print("Inventory:")
            for item in inventory:
                print('*' + str(item))
        else:
            print("Invalid input!")
        

def get_player_command():
    return input('Action: ')
       
play()