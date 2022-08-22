from collections import OrderedDict


def solution(survey, choices):
    answer = ''
    c = [0, 3, 2, 1, 0, 1, 2, 3, 0] #인덱스별 점수를 저장받는 배열
    kinds = ["R", "T", "C", "F", "J", "M", "A", "N"] #각각의 타입을 배열로
    score = OrderedDict() #순서가 있는 dict을 사용하여 나중에 합산할 때 편리하게
    for k in kinds:
        score[k] = 0

    for idx in range(len(survey)):
        cnt = c[choices[idx]]

        if choices[idx] <= 4: # 점수가 인덱스4이하면 앞에 것 + 1 아니면 뒤에 것 + 1
            score[survey[idx][0]] += cnt
        else:
            score[survey[idx][1]] += cnt

    for i in range(0, 7, 2):
        if score[s[i]] >= score[s[i+1]]:
            answer += s[i]
        else:
            answer += s[i+1]

    return answer
    


#파이썬 OrderedDict
#순서를 유지하는 dict이며 저장한 순서대로 출력이 된다.
#선언 => from collection import OrderedDict
# d = OrderedDict() , d["a"] = 3 ...

#해시문제는 자료구조 생각도 중요하지만 문제에서 주어진대로 일단 해보는게 좋을 듯
