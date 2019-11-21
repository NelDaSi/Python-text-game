class TextImg:
    def __init__(self):
        raise NotImplementedError("Do not create raw TextImg objects.")

    def __str__(self):
        return self.textimg


class StartTile(TextImg):
    def __init__(self):
        self.textimg = ""


class TrasderTile(TextImg):
    def __init__(self):
        self.textimg = ""


class EnemyTile(TextImg):
    def __init__(self):
        self.textimg = ""


class FindGoldTile(TextImg):
    def __init__(self):
        self.textimg = ""


class EmptytTile(TextImg):
    def __init__(self):
        self.textimg = ""


class VictoryTile(TextImg):
    def __init__(self):
        self.textimg = ""
