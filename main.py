from os.path import join
from map import Map
from actor import Actor

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


test_actor = Actor()
test_actor.set_map(test_map)
test_actor.set_position((4,8))
for direction in Actor.MOVES:
    print(f"Direction {direction} is {'free' if test_actor.can_move(direction) else 'unavailable'}")