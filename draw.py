from raylib import rl, colors

def loopdraw():
    rl.BeginDrawing()
    rl.ClearBackground(colors.RAYWHITE)
    rl.DrawText(b"KEKEK", 350, 300, 20, colors.BLACK)
    rl.EndDrawing()
