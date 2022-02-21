# Documentation
This will mainly go through what is available to you.

## Examples
There is an example of how you can control the game through the interfaces in [example_user_input.py](example_user_input.py)

## Structures
### Position
`game_2048/Grid.py`
- `Position.x`: The x co-ordinate of a position on the grid.
- `Position.y`: The y co-ordinate of a position on the grid.
- `Position.equals(other)`: Compares two positions to see if they are the same location or not. Usage: `posA == posB`

### Tile
`game_2048/Grid.py`
**Note**: Incomplete, please make an interface for this because there's functions there.
Inherits: Position
- `Tile.value`: The value assigned to that tile.

## Interfaces
### IGrid
`game_2048/Grid.py`
- `IGrid.areTilesFree()`: Are there any free tiles on the board?
- `IGrid.isTileFree(position)`: Is a certain tile free?
- `IGrid.isTileTaken(position)`: Is a certain tile taken?
- `IGrid.getTile(position)`: Get a particular tile at a position.
- `IGrid.getMap()`: Get the raw current map state

### IGameState
`game_2048/GameManager.py`
- `IGameState.getScore()`: Returns the current score.
- `IGameState.isOver()`: Returns a boolean for whether the game is finished.
- `IGameState.getMoveCount()`: Returns the number of moves performed successfully.
- `IGameState.hasWon()`: Returns a boolean for whether the game is won.
- `hasStopped()`: Returns a boolean for whether the game is stopped.

### IAIGameControl
`game_2048/APIControl.py`
- `IAIGameControl.start()`: Start the game
- `IAIGameControl.reset()`: Reset the game
- `IAIGameControl.getStatus()`: Get the current state of the game
- `IAIGameControl.getMap()`: Get the current state of the map
- `IAIGameControl.up()`: Shift the grid up. Returns a boolean if the move changed the board.
- `IAIGameControl.left()`: Shift the grid left. Returns a boolean if the move changed the board.
- ... you get the idea :\
