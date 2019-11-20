class TextImg:
    def __init__(self):
        raise NotImplementedError("Do not create raw TextImg objects.")

    def __str__(self):
        return self.name


class dungeon(TextImg):
    def __init__(self):
        self.name = """
╔═════════════════════════════════════════════════════════════╗
    You find yourself in a cave with a flickering torch
    on the wall. You can make out four paths, each equally
    as dark and foreboding.
╚═════════════════════════════════════════════════════════════╝
                    """

    # def print_dungeon():
    #     print()
    #     print("   _________________________________________________________")
    #     print(" /|     -_-                                             _-  |\ ")
    #     print("/ |_-_- _                                         -_- _-   -| \ ")
    #     print("  |                            _-  _--                      | ")
    #     print("  |                            ,                            |")
    #     print("  |      .-'````````'.        '(`        .-'```````'-.      |")
    #     print("  |    .` |           `.      `)'      .` |           `.    |")
    #     print("  |   /   |   ()        \      U      /   |    ()       \   |")
    #     print("  |  |    |    ;         | o   T   o |    |    ;         |  |")
    #     print("  |  |    |     ;        |  .  |  .  |    |    ;         |  |")
    #     print("  |  |    |     ;        |   . | .   |    |    ;         |  |")
    #     print("  |  |    |     ;        |    .|.    |    |    ;         |  |")
    #     print("  |  |    |____;_________|     |     |    |____;_________|  |")
    #     print("  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |")
    #     print("  |  |  / __  ()        -|        -  |  /  __--      -   |  |")
    #     print("  |  | /        __-- _   |   _- _ -  | /        __--_    |  |")
    #     print("  |__|/__________________|___________|/__________________|__|")
    #     print(" /                                             _ -        lc \ ")
    #     print("/   -_- _ -             _- _---                       -_-  -_ \ ")
    #     print()
