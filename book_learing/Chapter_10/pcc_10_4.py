from pathlib import Path
while True:
    name  = input('Enter your name(Enter q to end the program): ')
    if name =='q':
        break
    path = Path('guest')
    path.write_text(name)