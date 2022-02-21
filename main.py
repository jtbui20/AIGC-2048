import sys
import random
from game_2048.Grid import IGrid, Position, Tile
from game_2048.APIControl import IAIGameControl, APIController
from game_2048.GameManager import IGameState

if __name__ == "__main__":
  seed = sys.argv[0] if sys.argv[0] else random.randint(0, 999999)
  controller: IAIGameControl = APIController(seed, True)
  gameState: IGameState

  # Write your program here
  controller.start()