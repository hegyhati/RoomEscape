from typing import Tuple, Set

Position = Tuple[int, int]


class Map:

    FREE = " "
    OBSTACLE = "X"
    GOAL = "@"

    def __init__(self, filename: str) -> None:
        file = open(filename)
        self._map = tuple(row.rstrip() for row in file)
        file.close()
        if not self.is_valid():
            raise ValueError

    def is_valid(self) -> bool:
        # check for empty map
        self.height = len(self._map)
        if self.height == 0:
            return False

        # check for non-rectangle maps
        self.width = len(self._map[0])
        for row in self._map:
            if len(row) != self.width:
                return False
        symbols = {c for row in self._map for c in row}

        # check for foreign symbols
        if symbols != {self.FREE, self.OBSTACLE, self.GOAL}:
            return False
        if self.FREE in self._map[0] or self.FREE in self._map[-1]:
            return False
        for row in self._map:
            if row[0] == self.FREE or row[-1] == self.FREE:
                return False

        return True

    def free_fields(self) -> Set[Position]:
        return {
            (r, c)
            for r, row in enumerate(self._map)
            for c, field in enumerate(row)
            if field == self.FREE
        }

    def is_valid_position(self, position: Position) -> bool:
        return 0 <= position[0] < self.height and 0 <= position[1] < self.width

    def get_field(self, position: Position) -> str:
        if not self.is_valid_position(position):
            raise ValueError
        return self._map[position[0]][position[1]]
