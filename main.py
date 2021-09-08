from actor import DeadActor, InfiniteLoop
from os.path import join
from map import Map
from actors_vasvill import *


SUCCESSFUL = "W"
STOPPED = "S"
DIED = "D"
INFINITE = "I"
test_map_names = ["vasvill_01", "vasvill_02"]
test_actors = [VVA_1(),VVA_2()]


# Open maps
maps = {}
for map_name in test_map_names:
    filename = join("maps", f"{map_name}.txt")
    try:
        maps[map_name] = Map(filename)
    except OSError:
        print(f"File {filename} does not exist.")
    except ValueError:
        print(f"{filename} does not contain a valid map.")


for actor in test_actors:
    print(f"Actor {actor.__class__.__name__}")
    for mapname, map in maps.items():
        print(f" Map {mapname}")
        actor.set_map(map)
        results = {}
        for start in map.free_fields():
            try:
                actor.set_position(start)
                actor.run()
                results[start] = SUCCESSFUL if actor.is_out() else STOPPED
            except InfiniteLoop:
                results[start] = INFINITE
            except DeadActor:
                results[start] = DIED

        for r in range(map.height):
            print("  ", end="")
            for c in range(map.width):
                field = map.get_field((r, c))
                print(
                    "█"
                    if field == Map.OBSTACLE
                    else " "
                    if field == Map.GOAL
                    else results[(r, c)],
                    end="",
                )
            print()
