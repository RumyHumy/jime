#!/usr/bin/python3

# D E P E N D E N C I E S

import os
from raylib import rl, colors
import importlib

# A P P

import draw

# M A I N

def main():
    rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
    rl.InitWindow(800, 600, b"Raylib Test")
    draw_last_mod = os.stat("./draw.py").st_mtime
    while not rl.WindowShouldClose():
        draw.loopdraw()
        # Hotreload
        draw_curr_mod = os.stat("./draw.py").st_mtime
        if draw_curr_mod > draw_last_mod:
            importlib.reload(draw)
            draw_last_mod = draw_curr_mod 
    rl.CloseWindow()

if __name__ == "__main__":
    main()
