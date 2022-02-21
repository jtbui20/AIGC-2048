from .GameManager import GameManager
from .Grid import IGrid, Grid
from .GameManager import IGameState

class IAIGameControl:
  def start(self):
    """Start the game"""
    pass
  def reset(self):
    """Reset the game"""
  def getStatus(self) -> IGameState:
    """Get the current state of the game"""
    pass
  def getMap(self) -> IGrid:
    """Get the current state of the map"""
    pass
  def up(self) -> bool:
    """Shift the grid up. Returns a boolean if the move changed the board."""
    pass
  def left(self) -> bool:
    """Shift the grid left. Returns a boolean if the move changed the board."""
    pass
  def down(self) -> bool:
    """Shift the grid down. Returns a boolean if the move changed the board."""
    pass
  def right(self) -> bool:
    """Shift the grid right. Returns a boolean if the move changed the board."""
    pass

class APIController (IAIGameControl):
  def __init__(self, seed, doPrint = False):
    self.seed = seed
    self.status = None

    self.doPrint = doPrint

    self.game = GameManager(self, 4, self.seed)
  
  def start(self):
    self.game.setup()

  def report(self, grid: Grid, status):
    self.status = status

    if self.doPrint:
      self.printGameState()
      self.drawGrid(grid)
  
  def drawGrid(self, grid: Grid):
    # Rotate the grid from left: up, up: left
    # flip and 
    g = grid.getMap()
    for i in range(len(g[0])):
      print([x[i].value if x[i] else "" for x in g])

  def printGameState(self):
    print("Score: " + str(self.status.score))
    print("Running: " + str((not self.status.over)))
    print("Won: " + str(self.status.won))
    print("Moves: " + str(self.status.moves))

  def centerText(self, size: int, content):
    totalSpaces = len(content) - size
    left = round(totalSpaces / 2)
    right = totalSpaces - left

    return (" " * left) + content + (" " * right)

  def getStatus(self) -> IGameState:
    return self.status

  def getMap(self) -> IGrid:
    return self.game.grid.getMap()

  def up(self) -> bool:
    return self.game.move("up")
  def left(self) -> bool:
    return self.game.move("left")
  def down(self) -> bool:
    return self.game.move("down")
  def right(self) -> bool:
    return self.game.move("right")