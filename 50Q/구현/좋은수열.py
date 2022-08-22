##내코드 --시간초과
import sys
sys.setrecursionlimit(10**6)
n = int(input())
basic = [1, 2, 3]
comm = []


def dfs(pick):
    global comm ## 전역변수 선언 .. 블로그에 정리해둠
    if len(pick) == n:
        for i in range(1, n//2+1):
            gap = i
            last = pick[0:gap]
            for j in range(gap, n, gap):
                if pick[j:j+gap] == last:
                    return
                last = pick[j:j+gap]

        comm.append(int("".join(str(p) for p in pick)))

    else:
        for i in range(1, 4):
            pick.append(i)
            dfs(pick)
            pick.pop()


dfs([])
print(min(comm))
##다른 사람 풀이 섞어서
import sys
sys.setrecursionlimit(10**6)
n = int(input())


def dfs(pick):
    for i in range(1, len(pick)//2 + 1):
        if pick[-i:] == pick[-i-i:-i]:
            return
    if len(pick) == n:
        print((int("".join(str(p) for p in pick))))
        exit(0)
    for i in range(1, 4):
        pick.append(i)
        dfs(pick)
        pick.pop()


dfs([])
