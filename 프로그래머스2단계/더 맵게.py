import heapq

def solution(scov, K):
    heapq.heapify(scov)
    answer = 0
    while scov[0] <= K:
        mix = heapq.heappop(scov) + (heapq.heappop(scov)*2)
        heapq.heappush(scov,mix)
        answer += 1
        if len(scov) == 1 and scov[0] <= K:
            return -1
        
#sort를 사용했었지만 반복문마다 sort를 진행하므로 n * nlogn의 시간복잡도가 나왔다.
#그래서 힙큐를 사용
