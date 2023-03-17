def get_integer() :
    money=int(input('동전으로 교환하고자 하는 금액은?'))
    return money

def exchange (money) :
    오백원=money//500
    money%=500
    백원=money//100
    money%=100
    오십원=money//50
    money%=50
    십원=money//10
    print('500원 동전의 개수', 오백원, '개')
    print('100원 동전의 개수', 백원, '개')
    print('50원 동전의 개수', 오십원, '개')
    print('10원 동전의 개수', 십원, '개')
    


money=get_integer()
exchange(money)

    
