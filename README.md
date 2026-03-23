Dodge the Obstacles Game

Description:
This is a simple terminal-based action game written in Python. The player is represented by 'P' and obstacles are represented by 'X'. The player must move left or right to avoid hitting the obstacles. The game continues until a collision occurs.

Theory:
The game is based on basic programming concepts like loops, conditions, and functions. A loop is used to keep the game running continuously. Random numbers are used to generate obstacle positions. Conditions are used to check player movement and collision. The concept of a simple control system can also be seen here, where the player continuously adjusts position based on incoming obstacles.

How to Play:
- Press 'a' to move left
- Press 'd' to move right
- Press Enter to stay in the same position
- Avoid the obstacle 'X'
- The game ends when the player hits an obstacle

Functions Used and Their Uses:

create_track():
Creates an empty track (list) where the game elements are placed.

place_player(track, position):
Places the player 'P' at the given position on the track.

place_obstacle(track):
Places an obstacle 'X' at a random position on the track and returns its position.

display(track, score):
Clears the screen and displays the current track and score.

get_move(player_pos):
Takes input from the user and updates the player position based on the move.

check_collision(player_pos, obstacle_pos):
Checks whether the player and obstacle are at the same position.

play_game():
Controls the entire game flow including movement, display, scoring, and collision detection.

Conclusion:
This project helps in understanding basic game logic, function usage, and control flow in Python. It is a good starting point for beginners to learn how simple games are built and can be further improved into more advanced graphical games.
