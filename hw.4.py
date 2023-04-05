def rep_char():
    print('-'*length)

def 인사메시지(name) :
    length=len(name)
    rep_char(length)
    print(f'hello {name}/n welcome to seoul')
    rep_char(length)

name=input('input her/his name')
인사메시지(name)
