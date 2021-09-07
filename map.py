class Map:

    FREE = " "
    OBSTACLE = "X"
    GOAL = "@"

    def __init__(self, filename:str) -> None:
        file = open(filename)
        self._map = []
        for row in file:
            self._map.append(row.rstrip())
        file.close()
        if not self.is_valid():
            raise ValueError
    
    def is_valid(self) -> bool:
        # check for empty map
        height=len(self._map)
        if height==0: return False        
        
        # check for non-rectangle maps
        width=len(self._map[0])
        for row in self._map:
            if len(row) != width: return False 
        symbols = {c for row in self._map for c in row}

        # check for foreign symbols
        if symbols != {self.FREE, self.OBSTACLE, self.GOAL}: return False
        if self.FREE in self._map[0] or self.FREE in self._map[-1]: return False
        for row in self._map:
            if row[0] == self.FREE or row[-1] == self.FREE: return False
        
        return True


        






