def multiplication(r):
    for i in range(2,6):
        print(f"{i}X{r}={i*r:3d}{' '*5}",end='')
    print(' ',end='\n')


def multiplication2(s):
    for t in range(6,10):
        print(f"{t}X{s}={t*s:3d}{' '*5}",end='')
    print(' ',end='\n')
    
        
for r in range(1,10):
    multiplication(r)

print(' ',end='\n')

for s in range(1,10):
    multiplication2(s)
