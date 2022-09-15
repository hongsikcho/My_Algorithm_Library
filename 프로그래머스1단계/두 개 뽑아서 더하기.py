from itertools import combinations
def solution(numbers):
    rs = set()
    num = combinations(numbers,2)
    for i in list(num):
        rs.add(sum(i))
        
    return sorted(rs)
  
  #실제 테스트에서는 정답창에서만 코드르 짜야할 수 있기 때문에 import잘 알아둘것 !
  #from itertools import combinations
  #from itertools import permutaions
  
