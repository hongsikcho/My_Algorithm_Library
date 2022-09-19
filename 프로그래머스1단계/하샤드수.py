def solution(x):
    x = str(x)
    rs = 0
    for i in x:
        rs += int(i)
        
    if int(x)%rs == 0:
        return True
    else:
        return False

