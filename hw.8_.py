def buy(sb):
    p=input('상품명은?')
    if p=='':
        return False
    
    n=input('수량은?')
    sb[p]=n
    print(f'장바구니에 {p}가 {n}개 담겼습니다.')


def show(sb):
    print('>>장바구니 보기:{',end='')
    for key in sb:
        print(f'\'{key}\':{sb[key]},',end=' ')
    print('}')
    print( )

def find(sb):
    product=input('찾고자 하는 상품은?')
    if product in sb:
        print(f'{product}는 {sb[product]}개 있습니다.')
    else:
        print(f'장바구니에 {product}는 없습니다.')
    


shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break

show(shopping_bag)
find(shopping_bag)




    
