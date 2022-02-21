import random

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __eq__(self, other) -> bool:
    return self.x == other.x and self.y == other.y

class Tile (Position):
  def __init__(self, position: Position, value: int):
    self.x = position.x
    self.y = position.y
    self.value = value

    self.previousPosition = None
    self.mergedFrom = None

  def savePosition(self) -> None:
    self.previousPosition = Position(self.x, self.y)
  
  def updatePosition(self, position: Position) -> None:
    self.x = position.x
    self.y = position.y

class IGrid:
  def areTilesFree(self) -> bool:
    """Are there any free tiles on the board?"""
    pass

  def isTileFree(self, position: Position) -> bool:
    """Is a certain tile free?"""
    pass

  def isTileTaken(self, position: Position) -> bool:
    """Is a certain tile taken?"""
    pass

  def getTile(self, position: Position) -> Tile:
    """Get a particular tile at a position"""
    pass
  
  def getMap(self):
    """Get the current map state"""
    pass

class Grid (IGrid):
  def __init__(self, size: int):
    self.size = size
    self._map = []
    self._build()

  def _build(self) -> None:
    self._map = [[None for _ in range(self.size)] for _ in range(self.size)]

  def areTilesFree(self) -> bool:
    return not not self._freeTiles()
  
  def isTileFree(self, position: Position) -> bool:
    return not self.isTileTaken(position)
  
  def isTileTaken(self, position: Position) -> bool:
    return not not self.getTile(position)

  def randomFreeTile(self, random: random.Random) -> Tile:
    """Get a random tile"""
    tile = self._freeTiles()
    if len(tile):
      return tile[random.randint(0, self.size)]

  def getTile(self, position: Position) -> Tile:
    return self._map[position.x][position.y] if self.inRange(position) else None

  def getMap(self):
    return self._map

  def _freeTiles(self):
    tiles = []
    self.each(lambda x,y,tile: tiles.append(Position(x,y)) if not tile else None)
    return tiles

  def each(self, callback):
    for x in range(0, self.size):
      for y in range(0, self.size):
        callback(x, y, self._map[x][y])

  def insertTile(self, tile: Tile):
    self._map[tile.x][tile.y] = tile
  
  def removeTile(self, tile: Tile):
    self._map[tile.x][tile.y] = None
  
  def inRange(self, position: Position):
    return 0 <= position.x < self.size and 0 <= position.y < self.size