#!/usr/bin/python3

from raylib import *

InitWindow(800, 600, b"Raylib Test")
while not WindowShouldClose():
    BeginDrawing()
    ClearBackground(RAYWHITE)
    DrawText(b"Hello, Raylib!", 350, 300, 20, BLACK)
    EndDrawing()
CloseWindow()
