def solution(numbers, hand):
    left = '*'
    right = '#'
    answer = ''
    pad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
        '*': [3, 0],
        '#': [3, 2]
    } # 버튼별 정확한 위치를 통해 거리 계산
    l = [1, 4, 7]
    r = [3, 6, 9]

    for i in numbers:
        if i in l:
            left = i
            answer += 'L'
        elif i in r:
            right = i
            answer += 'R'
        else:
            gap_left = abs(pad[left][0] - pad[i][0]) + \
                abs(pad[left][1] - pad[i][1])
            gap_right = abs(pad[right][0] - pad[i][0]) + \
                abs(pad[right][1] - pad[i][1])
            if gap_right > gap_left:
                left = i
                answer += 'L'
            elif gap_right < gap_left:
                right = i
                answer += 'R'
            else:
                if hand == 'right':
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'

    return answer
  
  #처음에 해시를 떠올리지 못해서 못푼 문제
  #해시 없이 2,4,8,0이 나왔을때 경우의 수가 별로 없지만 코드 짜내려가면서 많아서 헷갈려짐
  #거리를 구해라 ? == > 해시 그래프가 맞는듯
