from pathlib import Path
path = Path('learning_python')
context = path.read_text(encoding='utf-8')
print(context.replace('Python' , 'C'))