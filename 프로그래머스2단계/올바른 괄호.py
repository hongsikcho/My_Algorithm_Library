def solution(s):
    answer = True
    array = ''
    
    for i in s:
        array+=i
        if array[-2:] == '()':
            array = array[:-2]
            
    if array:
        return False
    else:
        return True
    

    return True
