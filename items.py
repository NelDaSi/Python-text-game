class Gadget:
    def __init__(self):
        raise NotImplementedError("Do not create raw Gadget objects.")

    def __str__(self):
        return self.name


class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return "{} (+{} DMG)".format(self.name, self.damage)


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class Portal_gun(Gadget):
    def __init__(self):
        self.name = "Portal Gun"
        self.description = "Makes portals, duhh!!"
        self.damage = 100
        self.value = 200


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. " \
            "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword  o==[]::::::::::::::::>"
        self.description = "This sword is showing its age, " \
            "but still has some fight in it."
        self.damage = 20
        self.value = 100
