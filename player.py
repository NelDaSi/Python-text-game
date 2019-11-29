# _______Imports_______
# import textimg
import items
import world_check
# from time import sleep
# _______Player Class_______


class Player:
    def __init__(self):
        # self.name = None
        self.inventory = [items.Rock(),
                          items.CrustyBread()]
        self.inv_open = False
        self.x = world_check.start_tile_location[0]
        self.y = world_check.start_tile_location[1]
        self.hp = 100
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    # def get_player_name(self):
    #     while not self.name:
    #         temp_name = input("What's your name? > ")
    #         answer = input("Your name is {}, is that correct? [Y|N] > ".format(temp_name))
    #         if answer.lower() in ["y", "yes"]:
    #             self.name = temp_name
    #             print("You are fun, {}! Let's begin our adventure!".format(self.name))
    #             sleep(5.0)
    #         elif answer.lower() in ["n", "no"]:
    #             pass
    #         else:
    #             print("({}) is invalid".format(answer))
    #
    #     return self.name

# _______Show inventory_______
    def print_inventory(self):
        self.inv_open = True
        print("\nInventory:\n")
        for item in self.inventory:
            print('*' + str(item))
        print("Gold: {}".format(self.gold))

        input("\nPress enter...")

# _______Display best weapon in inventory_______

#        best_weapon = self.most_powerful_weapon()
#        print("Your best weapon is your {}".format(best_weapon))

# _______Best weapon_______

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

# _______Movement_______

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

# _______Consumables_______

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            input("You dont`t have any items to heal you!"
                  "Press Enter to proceed.")
            return
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choise, try again.")

# _______Attack_______

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world_check.tile_at(self.x, self.y)
        enemy = room.enemy
        print("\nYou use {} against {}!.".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            input("""\nYou killed {}!
                  \nPress enter...""".format(enemy.name))
        else:
            input("""\n{} HP is {}.
                  \nPress enter...""".format(enemy.name, enemy.hp))

    def trade(self):
        room = world_check.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def quit_game(self):
        quit()

    def restart_game(self):
        print("W.I.P.")
        quit()
