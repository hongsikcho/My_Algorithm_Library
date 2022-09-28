def solution(s):
    answer = -1
    result = [s[0]]
    for i in s[1:]:
        result.append(i)
        if len(result)>= 2:
            if result[-1] == result[-2]:
                result.pop()
                result.pop()
            
    if len(result) == 0:
        return 1
    else:
        return 0
