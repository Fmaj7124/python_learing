from pathlib import Path

path = Path('Harry')
contents = path.read_text(encoding='utf-8')
words = contents.split()

print(f"这本书大约有 {len(words)} 个单词")
print(f"'the' 出现了 {words.count('the')} 次")