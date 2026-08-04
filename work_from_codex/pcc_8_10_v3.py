homework = ['小明', '小红', '小刚', '小明', '小丽']
graded = []
def marking(homework , graded):
    while homework:
        current_homework = homework.pop()
        print(current_homework)
        graded.append(current_homework)

marking(homework , graded)
print(homework)
print(graded)