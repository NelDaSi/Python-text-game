# __Imports__
import os
from player import Player
import tiles
import world
from collections import OrderedDict


def play_intro():
    input("The Forgotten Morty."
          "\nPress Enter...")


def play():
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        os.system('cls')
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end!\n\n")
            print("Would you like to (R)estart or (Q)uit?")
            choose_action(room, player)


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: \n")
    if player.inventory and player.is_alive():
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, tiles.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, tiles.EnemyTile) and room.enemy.is_alive():
        if not player.is_alive():
            action_adder(actions, 'q', player.quit_game, "Quit game.")
            action_adder(actions, 'r', player.restart_game, "Restart game.")
        else:
            action_adder(actions, 'a', player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
        action_adder(actions, 'q', player.quit_game, "Quit game.")
    if player.hp < 100 and not player.hp <= 0:
        action_adder(actions, 'h', player.heal, "Heal")
    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("\nAction: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


play_intro()

play()
