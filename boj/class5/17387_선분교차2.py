# 직선의 방정식 : 무한으로 확장이 아니므로 cut

# 1. 직선 겹치는지 확인
# 2. 직선이 겹친다면 교점 찾기
# 3. 교점이 두 선분 위에 있는지를 확인
# x1 <= <= x2, y1<= <=y2

# 굳이 복잡하게 할 필요있나?

x1, y1, x2, y2 = [int(x) for x in input().split()]
x3, y3, x4, y4 = [int(x) for x in input().split()]

if x2 <= x1 : 
    x1, y1, x2, y2 = x2, y2, x1, y1
if x4 <= x3 : 
    x3, y3, x4, y4 = x4, y4, x3, y3

if x3 > x2 :
    print(0)
elif x4 < x1 :
    print(0)
elif x2==x1 and x4 != x3:
    a2 = (y4-y3)/(x4-x3)
    b2 = y3 - a2*x3
    if min(y1,y2)-0.001<=a2*x1+b2<=max(y1,y2)+0.001 :
        print(1)
    else: 
        print(0)
elif x4==x3 and x1 != x2:
    a1 = (y2-y1)/(x2-x1)
    b1 = y1 - a1*x1
    if min(y3,y4)-0.001<=a1*x3+b1<=max(y3,y4)+0.001:
        print(1)
    else: 
        print(0)
elif x1==x2 and x3==x4 :
    y1, y2 = min(y1, y2), max(y1, y2)
    y3, y4 = min(y3, y4), max(y3, y4)
    if max(y1, y2) < min(y3, y4) : 
        print(0)
    elif min(y1, y2) > max(y3, y4) :
        print(0)
    else :
        print(1)
else :
    a1 = (y2-y1)/(x2-x1)
    a2 = (y4-y3)/(x4-x3)
    b1 = y1 - a1*x1
    b2 = y3 - a2*x3
    
    if (a1*x3+b1-y3)*(a1*x4+b1-y4)<=0.001 and (a2*x1+b2-y1)*(a2*x2+b2-y2) <= 0.001 : 
        print(1)
    else : 
        print(0)