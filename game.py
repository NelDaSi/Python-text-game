class Weapon:
    def __str__(self):
        return self.name


class PortalGun(Weapon):
    def __init__(self):
        self.name = "Portal Gun"
        self.description = "The Portal Gun is a gadget that allows the user(s) to travel between different universes/dimensions/realities."
        self.damage = 100


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. Somewhat more dangerous than a rock."
        self.damage = 10


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, but still has some fight in it."
        self.damage = 20


def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        if item.damage > max_damage:
            best_weapon = item
            max_damage = item.damage
    return best_weapon


def play():
    inventory = [Rock(), Dagger(), 'Gold(5)', 'Crusty Bread']
    print("Escape from Cave Terror! ")
    while True:
        action_input = get_player_command()
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
