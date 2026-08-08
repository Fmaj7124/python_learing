from pathlib import Path
from shlex import split

path = Path('learning_python')
context = path.read_text(encoding='utf-8')
print(context)

lines = context.splitlines()
print(lines)