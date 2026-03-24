import random
import time
import os

WIDTH = 7
HEIGHT = 5

def create_grid():
    return [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

def display(grid, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Score:", score)
    for row in grid:
        print("|" + "".join(row) + "|")

def get_move(pos):
    move = input("Move (a=left, d=right): ")
    if move == "a" and pos > 0:
        return pos - 1
    if move == "d" and pos < WIDTH - 1:
        return pos + 1
    return pos

def update_obstacles(obstacles):
    new_obs = []
    for r, c in obstacles:
        if r + 1 < HEIGHT:
            new_obs.append((r + 1, c))
    if random.random() < 0.6:
        new_obs.append((0, random.randint(0, WIDTH - 1)))
    return new_obs

def place_objects(grid, player_pos, obstacles):
    grid[HEIGHT - 1][player_pos] = "P"
    for r, c in obstacles:
        grid[r][c] = "X"

def check_collision(player_pos, obstacles):
    for r, c in obstacles:
        if r == HEIGHT - 1 and c == player_pos:
            return True
    return False

def play():
    player_pos = WIDTH // 2
    obstacles = []
    score = 0

    print("Falling Obstacles")
    time.sleep(1)

    while True:
        grid = create_grid()
        player_pos = get_move(player_pos)
        obstacles = update_obstacles(obstacles)
        place_objects(grid, player_pos, obstacles)
        display(grid, score)

        if check_collision(player_pos, obstacles):
            print("Game Over")
            print("Final Score:", score)
            break

        score += 1
        time.sleep(0.4)

play()