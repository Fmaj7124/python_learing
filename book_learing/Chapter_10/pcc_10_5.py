from pathlib import Path

path = Path('guest')

prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# 退出循环后，统一把名单拼成一个字符串
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)