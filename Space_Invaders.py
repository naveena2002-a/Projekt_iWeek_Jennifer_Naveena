

import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)
snake_x = sw/4
snake_y = sh/2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]
food = [sh/2, sw/2]
w.addch(food[0], food[1], curses.ACS_PI)

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY.DOWN:
        new_head[0] += 1
    if key == curses.KEY.UP:
        new_head[0] -= 1
    if key == curses.KEY.LEFT:
        new_head[1] -= 1
    if key == curses.KEY.RIGHT:
        new_head[1] += 1





