# Example - User input
# This demonstrates how the API controls the game by using a front-end console.
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

  while not controller.getStatus().isOver():
    t = input("Choose a direction: ")
    if t == "left":
      controller.left()
    elif t == "up":
      controller.up()
    elif t == "right":
      controller.right()
    elif t == "down":
      controller.down()
    elif t == "stop":
      break

  print("Game ended")
  print("Moves: ", controller.getStatus().getMoveCount())
  print("Score: ", controller.getStatus().getScore())