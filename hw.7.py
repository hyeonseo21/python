print('[구입]')

shopping_bag={}
while True:
    item=input('상품명?')
    if item=='':
        break
    num=int(input('수량은?'))
    print(f'{item}이 장바구니에 담겼습니다.')
    shopping_bag[item]=num

print(f'>>>장바구니 보기:{shopping_bag}')
print('[검색?]')
product=input('장바구니에서 확인하고자 하는 상품은?')
print(f'{product}는 {shopping_bag.get(product)}개 담겨 있습니다.')
    
