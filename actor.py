from map import Map, Position


class DeadActor(Exception):
    pass


class InfiniteLoop(Exception):
    pass


class Actor:

    MOVES = {"forward": (-1, 0), "backward": (1, 0), "left": (0, -1), "right": (0, 1)}

    map = None
    position = None

    def set_map(self, map: Map):
        self.map = map

    def set_position(self, position: Position, pathreset: bool = True):
        if self.map.get_field(position) in {Map.FREE, Map.GOAL}:
            self.position = position
            if pathreset:
                self.path = []
            self.path.append(position)
            if self.path.count(position) != 1:
                raise InfiniteLoop
        else:
            raise DeadActor

    def is_alive(self) -> bool:
        return self.map.get_field(self.position) in {Map.FREE, Map.GOAL}

    def is_out(self) -> bool:
        return self.map.get_field(self.position) == Map.GOAL

    def _neighbor_index(self, direction: str) -> Position:
        if direction not in self.MOVES.keys():
            raise ValueError
        return (
            self.position[0] + self.MOVES[direction][0],
            self.position[1] + self.MOVES[direction][1],
        )

    def move(self, direction: str) -> None:
        if self.is_alive():
            self.set_position(self._neighbor_index(direction), pathreset=False)

    def can_move(self, direction: str) -> bool:
        return (
            self.is_alive()
            and self.map.get_field(self._neighbor_index(direction)) == Map.FREE
        )

    def run(self):
        pass
