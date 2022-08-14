from collections import defaultdict
def solution(id_list, report, k):
    report = list(set(report)) #한사람이 다른 사람을 중복되게 신고한 상황을 제거
    result = [] # 결과를 넣을 result
    user = defaultdict(set) # 누가 누굴 신고했는지 저장할 딕셔너리
    cnt = defaultdict(int) # 누가 얼마나 신고당했는지 저장할 딕셔너리
    
    for r in report:
        a,b = r.split()
        
        user[a].add(b)
        cnt[b] += 1
        
    for i in id_list: #id_list에 저장된 순서대로 출력해야하므로 ... 이게 생각이 왜 안났지 ?
        answer = 0
        for u in user[i]:
            if cnt[u] >= k:
                answer += 1
        result.append(answer)
    return result
  
  # 해시를 사용하는 기본적인 문제
  # 해시에 대한 부담감이 있는데 기본적인 메소드를 사용하여 해결할 수 있음 쫄지 말 것
  # defaultdict을 사용하면 기본값을 저장할 수 있음
