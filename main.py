from os.path import join
from map import Map

filename=join("maps","vasvill.txt")
try:
    test_map = Map(filename)
except OSError:
    print(f"File {filename} does not exist.")
except ValueError:
    print(f"{filename} does not contain a valid map.")