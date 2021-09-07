from actor import DeadActor, InfiniteLoop
from os.path import join
from map import Map
from actors_vasvill  import *

filename=join("maps","vasvill.txt")
try:
    test_map = Map(filename)
except OSError:
    print(f"File {filename} does not exist.")
except ValueError:
    print(f"{filename} does not contain a valid map.")

print("Free fields: ", test_map.free_fields())

for r in range(test_map.height):
    for c in range(test_map.width):
        print(test_map.get_field((r,c)), end='')
    print()


test_actor = VV_1()
test_actor.set_map(test_map)



SUCCESSFUL = "W"
STOPPED = "S"
DIED = "D"
INFINITE = "I"

results = {}
for start in test_map.free_fields():
    try:
        test_actor.set_position(start)
        test_actor.run()
        results[start] = SUCCESSFUL if test_actor.is_out() else STOPPED
    except InfiniteLoop:
        results[start] = INFINITE
    except DeadActor:
        results[start] = DIED

for r in range(test_map.height):
    for c in range(test_map.width):
        field = test_map.get_field((r,c))
        print("█" if field==Map.OBSTACLE else " " if field==Map.GOAL else results[(r,c)], end='')
    print()
