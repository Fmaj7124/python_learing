from pathlib import Path
#编写尝试读取读取文本并打印内容的方法
def read(path):
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Can not find file {filename}")
    else:
        print(contents)

#依次获得路径
filenames = ['Cats' , 'Dogs']
for filename in filenames:
    path = Path(filename)
    read(path)