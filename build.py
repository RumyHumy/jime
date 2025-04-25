#!/usr/bin/python3

import PyInstaller.__main__

if __name__ == "__main__":
    PyInstaller.__main__.run([
        'main.py',
        'draw.py',
        '--onefile',
        '--name=Jime',
        '--clean'
    ])
