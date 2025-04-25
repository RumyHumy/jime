#!/usr/bin/python3

# D E P E N D E N C I E S

import os
from raylib import rl, colors
import importlib

BINARY_BUILD=False
try:
    import PyInstaller
    BINARY_BUILD=True
except ImportError:
    pass

# A P P

import draw

# M A I N

if not BINARY_BUILD: # "draw.py" hotreloading
    draw_last_mod = os.stat("./draw.py").st_mtime
    def draw_hotreload():
        global draw_last_mod
        draw_curr_mod = os.stat("./draw.py").st_mtime
        if draw_curr_mod > draw_last_mod:
            importlib.reload(draw)
            draw_last_mod = draw_curr_mod 

def main():
    rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
    rl.InitWindow(800, 600, b"Raylib Test")
    while not rl.WindowShouldClose():
        draw.loopdraw()
        if not BINARY_BUILD:
            draw_hotreload(draw_lat_mod)
    rl.CloseWindow()

if __name__ == "__main__":
    main()
