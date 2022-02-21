import random
from .Grid import Tile, Position, Grid

class IGameState:  
  def getScore(self) -> int:
    """Returns the current score"""
    pass

  def isOver(self) -> bool:
    """Returns a boolean for whether the game is finished."""
    pass

  def getMoveCount(self) -> int:
    """Returns the number of moves performed"""
    pass

  def hasWon(self) -> bool:
    """Returns a boolean for whether the game is won."""
    pass

  def hasStopped(self) -> bool:
    """Returns a boolean for whether the game is stopped."""

class GameState (IGameState):
  def __init__(self, score, over, moves, won, killed):
    self.score = score
    self.over = over
    self.moves = moves
    self.won = won
    self.killed = killed
  
  def getScore(self) -> int:
    return self.score

  def isOver(self) -> bool:
    return self.over

  def getMoveCount(self) -> int:
    return self.moves

  def hasWon(self) -> bool:
    return self.won
  
  def hasStopped(self) -> bool:
    return self.killed

class GameManager:
  def __init__(self, watcher, size, seed):
    self.size = size
    self.seed = seed

    self.watcher = watcher

    self.startTiles = 2

  def restart(self): 
    self.setup()

  def isGameStop(self):
    return self.over or self.won

  def setup(self):
    self.grid = Grid(self.size)

    self.score = 0
    self.over = False
    self.won = False
    self.running = False
    self.moves = 0

    self.random = random.Random(self.seed)

    self.addStartTiles()

    self.update()

  def update(self):
    self.watcher.report(self.grid, GameState(self.score, self.over, self.moves, self.won, self.isGameStop()))

  def addStartTiles(self):
    for _ in range(self.startTiles): self.addRandomTile()
  
  def addRandomTile(self):
    if self.grid.areTilesFree():
      value = 2 if self.random.random() < 0.9 else 4
      tile = Tile(self.grid.randomFreeTile(self.random), value)

      self.grid.insertTile(tile)

  def savePosition(self):
    def _(tile: Tile):
      if (tile):
        tile.mergedFrom = None
        tile.savePosition()

    self.grid.each(lambda x,y,tile: _(tile))
  
  def getDirection(self, direction):
    map = {
      "up": Position(0, -1),
      "right": Position(1, 0),
      "down": Position(0, 1),
      "left": Position(-1, 0)
    }

    return map[direction]

  def moveTile(self, tile: Tile, newPosition):
    self.grid.removeTile(tile)
    tile.updatePosition(newPosition)
    self.grid.insertTile(tile)

  def move(self, direction) -> bool:
    if self.isGameStop(): return

    vector = self.getDirection(direction)
    trav = self.buildtraversal(vector)
    moved = False

    self.savePosition()

    for x in trav["x"]:
      for y in trav["y"]:
        pos = Position(x,y)
        tile = self.grid.getTile(pos)

        if (tile):
          possible = self.findFarthestPosition(tile, vector)
          next = possible["next"]

          if next and next.value == tile.value and not next.mergedFrom:
            merged = Tile(possible["next"], tile.value * 2)
            merged.mergedFrom = [tile, next]

            self.grid.insertTile(merged)
            self.grid.removeTile(tile)

            tile.updatePosition(possible["next"])

            self.score += merged.value

            if (merged.value == 2048): self.won = True
          
          else:
            self.moveTile(tile, possible["farthest"])
        if tile:
          if not pos == tile:
            moved = True
    
    if moved:
      self.moves += 1
      self.addRandomTile()

      if not self.movesAvailable():
        self.over = True

    self.update()
    return moved

  def buildtraversal(self, vector):
    trav = {"x": [], "y":[]}

    for i in range(self.size):
      trav["x"].append(i)
      trav["y"].append(i)

    if (vector.x == 1): trav["x"].reverse()
    if (vector.y == 1): trav["y"].reverse()

    return trav

  def findFarthestPosition(self, position, vector):
    prev = None
    while True:
      prev = position
      position = Position(position.x + vector.x, position.y + vector.y)

      if not (self.grid.isTileFree(position) and self.grid.inRange(position)): break
    
    return {
      "farthest": prev,
      "next": self.grid.getTile(position)
    }

  def movesAvailable(self):
    return self.grid.areTilesFree() or self.tileMatchAvailable()

  def tileMatchAvailable(self):
    for x in range(self.size):
      for y in range(self.size):
        tile = self.grid.tileData(x,y)

        if (tile):
          for direction in ["up", "right", "down", "left"]:
            vector = self.getDirection(direction)
            other = self.grid.getTile(x + vector.x, y + vector.y)

            if (other.value == tile.value): return True

    return False