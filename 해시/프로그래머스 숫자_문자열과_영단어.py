def solution(s):
    words = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    # words = dict{}
    # word = ["zero","one", . . . , "nine"]
    # for idx i in enumerate(word):
    #     words[i] = idx
      
    result = ""
    comm = ""
    question = list(s)
    
    for i in question:
        if i.isdigit():
            result += i
        else:
            comm += i
            if comm in words:
                result += str(words[comm])
                comm = ""
    return int(result)
  
  # isdigit : 주어진 문자열이 모두 숫자로만 이루어져 있는지 확인
  # isalpha : 주어진 문자열이 모두 문자로만 이루어져 있는지 확인
  # 문자열.replace(a,b) : 주어진 문자열의  a 부분을 b로 치환한다. (모두 바꿀땐 replaceAll(a,b)) 
  # 하지만 문자열은 변경불가하므로 s2 = s1.replace(a,b) 이렇게 사용해주어야함.
