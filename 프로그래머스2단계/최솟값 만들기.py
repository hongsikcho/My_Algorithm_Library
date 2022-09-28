def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    rs = 0
    for i in range(len(A)):
        rs += A[i]*B[i]
    
    return rs
