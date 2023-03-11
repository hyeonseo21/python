def get_radius(prompt) :
    r=int(input(prompt))
    return r

def get_circle_area(radius_) :
    area= (radius_*radius_*3.14)
    return area
    

    
radius=get_radius('넓이를구하고자 하는 원의 반지름은?')
real_area=get_circle_area(radius)
print('반지름', str(radius)+'인 원의 넓이 = 3.14X'+str(radius)+'X'+str(radius),'=',str(real_area)+'입니다.')
