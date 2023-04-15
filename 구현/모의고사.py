def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []


    for idx, ans in enumerate(answers):
        if ans == p1[idx % len(p1)]:
            score[0] += 1
        if ans == p2[idx % len(p2)]:
            score[1] += 1
        if ans == p3[idx % len(p3)]:
            score[2] += 1

    for a, b in enumerate(score):
        if b == max(score):
            result.append(a+1)
    return result
  
  #인덱스를 최대한 활용해보려 할 것!
