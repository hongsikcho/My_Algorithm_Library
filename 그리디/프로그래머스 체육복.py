def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    for reserve_person in reserve_set: 
        if reserve_person-1 in lost_set: 
            lost_set.remove(reserve_person-1) 
        elif reserve_person+1 in lost_set: 
            lost_set.remove(reserve_person+1) 
    
    return n-len(lost_set)
  
  #리스트끼리는 차이를 구할 수 없으므로 set을 쓴다면 편리하게 구할 수 잇음
  #set에는 리스트가 안담김, 단 튜플은 담김
  #set도 for문 돌아감
