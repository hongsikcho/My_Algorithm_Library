def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        rs = []
        for j in range(len(arr1[0])): 
            rs.append(arr1[i][j]+arr2[i][j])
        answer.append(rs)
    return answer
