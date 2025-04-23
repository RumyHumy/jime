#!/usr/bin/python3

import raylib as rl

if __name__ == "__main__":
    rl.InitWindow(800, 600, b"Raylib Test")
    while not rl.WindowShouldClose():
        rl.BeginDrawing()
        rl.ClearBackground(rl.RAYWHITE)
        rl.DrawText(b"Hello, Raylib!", 350, 300, 20, rl.BLACK)
        rl.EndDrawing()
    rl.CloseWindow()
