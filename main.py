#!/usr/bin/python3

# D E P E N D E N C I E S

import os
from raylib import rl, colors
import importlib

# A P P

import draw

# M A I N
HOTRELOAD=os.path.isfile("./draw.py")
if HOTRELOAD:
    draw_last_mod = os.stat("./draw.py").st_mtime
    def draw_hotreload():
        global draw_last_mod
        draw_curr_mod = None
        try:
            draw_curr_mod = os.stat("./draw.py").st_mtime
        except: pass
        if draw_curr_mod and draw_curr_mod > draw_last_mod:
            importlib.reload(draw)
            draw_last_mod = draw_curr_mod 

def main():
    #rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE)
    rl.InitWindow(1600, 1200, b"Raylib Test")
    while not rl.WindowShouldClose():
        rl.DrawText(f"HOTRELOAD: {HOTRELOAD}".encode("utf-8"), 0, 0, 20, colors.BLACK)
        draw.loopdraw()
        if HOTRELOAD:
            draw_hotreload()
    rl.CloseWindow()

if __name__ == "__main__":
    main()
