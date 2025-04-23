# py-uni-practice
Simple editor in Python + Raylib

# How to run
## Linux
```bash
# In project directory
pip install raylib numpy
./main.py
```

## Linux (using venv)
```bash
# In project directory
python3 -m venv venv
./venv/bin/pip3 install raylib numpy
./main.py
```

## Windows
```shell
pip install raylib numpy
./main.py
```

# How to create binary
## Linux
```bash
# In project directory
pip install pyinstaller
pyinstaller --onefile main.py
# Result in dist
```

## Linux (using venv)
```bash
# In project directory
python3 -m venv venv
./venc/bin/pyinstaller --onefile main.py
# Result in dist
```

## Windows
```shell
```
