import os
filename='data/score.bin'

score=[]

def writescore():
    print('[점수 입력]')
    i=0
    while True:
        i+=1    
        n=int(input(f'#{i}?'))
        if n<0:
            break
        score.append(n)

def printscore():
    print('[점수 출력]')
    print('개인점수:',end='')
    k=0
    for i in range(len(score)):        
        print(f'{score[i]} ',end='')
        k+=score[i]
    print(f'평균: {k/len(score)}')

    
def savescore():
    import pickle
    with open(filename,'wb') as file:
        for i in range(len(score)):
            pickle.dump(score[i],file)
            
def loadscore():
    print('[파일 읽기]')
    import pickle
    print(f'\n[점수 출력]')
    print('개인점수:',end='')
    summ=0
    with open(filename,'rb') as file:
        a=pickle.load(file)
        b=pickle.load(file)
        print(f'{a} {b}')
        score.append(a)
        score.append(b)
        summ=a+b
    average=summ/len(score)
    print(f'평균: {average}')
    
            

if os.path.exists(filename):
    loadscore()

    
else:
    writescore()
    printscore()
    savescore()


