def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:])
        arr2_bin.append(bin(arr2[i])[2:])
        arr1_bin[i] = ('0' * (n-len(arr1_bin[i]))) + arr1_bin[i] # 크기가 n이 지도이므로 그에 맞게 앞에 0붙여줘야함
        arr2_bin[i] = ('0' * (n-len(arr2_bin[i]))) + arr2_bin[i]
    
        tmp = ''
        for p in range(n):
            if arr1_bin[i][p] == '1' or arr2_bin[i][p] == '1':
                tmp += '#'
            elif arr1_bin[i][p] == '0' and arr2_bin[i][p] == '0':
                tmp += ' '
        answer.append(tmp)
        
    return answer
  
  #bin은 10진수를 2진수로 바꾸는 함수
  #앞에 문자 0b가 붙기때문에 bin(num)[2:]로 해주어야 한다.
  #문자열고 배열을 적절히 사용할 것 !
