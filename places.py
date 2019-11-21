class Space:
    def __init__(self):
        raise NotImplementedError("Do not create raw Gadget objects.")

    def __str__(self):
        return self.name


class MortyRoom(Space):
    def __init__(self):
        self.name = str("""
|ET|  |EN|ET|ET|ET|  |VT|  |ET|
|ET|EN|EN|  |  |ET|  |ET|  |ET|
|  |EN|  |ET|  |ET|  |ET|  |ET|
|  |EN|  |ET|ET|ET|ET|ET|  |ET|
|ET|EN|  |ET|ET|ET|ET|  |ET|ET|
|  |EN|  |ET|ET|ET|ET|ET|ET|  |
|ET|EN|ET|  |ET|ET|  |  |ET|ET|
|  |TT|  |ET|ET|  |ET|ET|  |ET|
|ET|ST|ET|  |ET|  |ET|ET|ET|ET|
|  |ET|  |ET|ET|  |ET|ET|  |ET|
""")
