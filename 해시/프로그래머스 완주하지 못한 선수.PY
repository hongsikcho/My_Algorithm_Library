def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for num in range(len(completion)):
        if participant[num] != completion[num]:
            return participant[num]
        
    return participant[-1]
  
  # 정확성에서는 정답이지만 효율성에서 맞추지 자꾸 틀린 문제
  # 첫 코드에는 for p in participant : 
  #                   if c in completion: 을 사용하여 하나하나 찾아내는 코드를 작성했지만 느렸음.
  # 각 리스트를 정렬 후 같은 인덱스끼리 비교하며 진행하면 리스트를 다 돌 필요가 없으므로 빠름.
                          
