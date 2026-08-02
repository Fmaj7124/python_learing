#定义make_shirt
def make_shirt(size , words = 'I love python'):
    print(F"The size is {size},and the words is '{words}'")

#制作一件默认字样的大号T
make_shirt(180 ,)

#制作一件默认字样的中号T
make_shirt(170 ,)

#制作一件其他字样的T
make_shirt(175 , '告诉过你')