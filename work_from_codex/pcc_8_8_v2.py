#定义借书系统
def lend_book(person , book , page):
    lend_book_list = {'Person' : person , 'Book' : book , 'Page' : page , }
    return lend_book_list
#询问用户信息
while True:
    person1 = input("What's your name?(Enter 'q' to end the program)： ")
    if person1 == 'q':
        break
    book1 = input("Which book would you like to lend?: ")
    if book1 == 'q':
        break
    page1 = input("How many page is this book?: ")
    if page1 == 'q':
        break
    page1 = int(page1)
    list_book = lend_book(person1 , book1 , page1 )
    print(list_book)