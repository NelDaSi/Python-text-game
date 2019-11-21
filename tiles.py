import random
import enemies
import npc
import textimg


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        # import from textimg
        return """
        {}
╔═════════════════════════════════════════════════════════════╗
                  This is your start position
           Walk around. Who knows what you might find!
╚═════════════════════════════════════════════════════════════╝
        """.format(textimg.StartTile())


class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
        return """
        {}
╔═════════════════════════════════════════════════════════════╗
   A frail not-quite-human, not-quite-creature squats in the
   corner clinking his gold coins together.
   He looks willing to trade.
╚═════════════════════════════════════════════════════════════╝
                """.format(textimg.TrasderTile())


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = """
╔═════════════════════════════════════════════════════════════╗
            A giant spider jumps down from
                its web in front of you!
╚═════════════════════════════════════════════════════════════╝
            """
            self.dead_text = """
╔═════════════════════════════════════════════════════════════╗
            The corpse of a dead spider "
            "rots on the ground.
╚═════════════════════════════════════════════════════════════╝
            """
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = """
╔═════════════════════════════════════════════════════════════╗
            An ogre is blocking your path!
╚═════════════════════════════════════════════════════════════╝
            """
            self.dead_text = """
╔═════════════════════════════════════════════════════════════╗
            A dead ogre reminds you of your triumph.
╚═════════════════════════════════════════════════════════════╝
            """
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = """
╔═════════════════════════════════════════════════════════════╗
            You hear a squeaking noise growing louder"
            "...suddenly you are lost in s swarm of bats!
╚═════════════════════════════════════════════════════════════╝
            """
            self.dead_text = """
╔═════════════════════════════════════════════════════════════╗
            Dozens of dead bats are scattered on the ground.
╚═════════════════════════════════════════════════════════════╝
            """
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = """
╔═════════════════════════════════════════════════════════════╗
            You've disturbed a rock monster "
            "from his slumber!
╚═════════════════════════════════════════════════════════════╝
            """
            self.dead_text = """
╔═════════════════════════════════════════════════════════════╗
            Defeated, the monster has reverted "
            "into an ordinary rock.
╚═════════════════════════════════════════════════════════════╝
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive()else self.dead_text
        return " {}".format(textimg.EnemyTile()) + text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining."
                  .format(self.enemy.damage, player.hp))


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
                    {}
╔═════════════════════════════════════════════════════════════╗
            Another unremarkable part of the cave.
                  You must forge onwards.
╚═════════════════════════════════════════════════════════════╝
                """.format(textimg.FindGoldTile())
        else:
            return """
                    {}
╔═════════════════════════════════════════════════════════════╗
           Someone dropped some gold. You pick it up.
╚═════════════════════════════════════════════════════════════╝
                """.format(textimg.FindGoldTile())


class EmptyTile(MapTile):
    def intro_text(self):
        return """
{}
╔═════════════════════════════════════════════════════════════╗
            This is a very boring part of the cave.
╚═════════════════════════════════════════════════════════════╝
                """.format(textimg.EmptytTile())


class VictoryTile(MapTile):

    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
{}
╔═════════════════════════════════════════════════════════════╗
   You see a bright light in the distance...
               ... it grows as you get closer! It's sunlight!
               Victory is yours!
╚═════════════════════════════════════════════════════════════╝
                """.format(textimg.VictoryTile())
