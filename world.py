import tiles
# import places


world_dsl = """
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
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


tile_type_dict = {"VT": tiles.VictoryTile,
                  "EN": tiles.EnemyTile,
                  "ST": tiles.StartTile,
                  "FG": tiles.FindGoldTile,
                  "TT": tiles.TraderTile,
                  "ET": tiles.EmptyTile,
                  "  ": None}


world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == tiles.StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
