def solution(people, limit):
    answer = 0
    people.sort()
    start , end = 0 , len(people)-1
    while start <= end:
        
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        
        answer +=1

    return answer
  
#투포인터를 활용하 풀이방법
#투포인터 언제 사용하는지 어떻게 사용하는지 공부할 것
