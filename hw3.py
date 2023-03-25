def get_fixed_price(product,sale,sale_price):
    real_price=int(sale_price/(1-sale*0.01))
    print(product,'상품의 정가는',real_price,'원')

    
sale=int(input('할인율은?'))
A_price=int(input('A 상품 할인된 가격은?'))
B_price=int(input('B 상품 할인된 가격은?'))
get_fixed_price('A상품',sale,A_price)
get_fixed_price('B상품',sale,B_price)
