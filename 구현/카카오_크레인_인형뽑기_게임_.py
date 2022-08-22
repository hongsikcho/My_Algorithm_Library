def solution(board, moves):
    answer = []
    result = 0

    for m in moves: #뽑은 열 순서대로 확인 
        for i in range(len(board)): #인형이 해당 행렬에 없으면 행을 +1 씩하며 크레인이 밑으로 들어감
            if board[i][m-1] != 0:
                answer.append(board[i][m-1])
                board[i][m-1] = 0 # 인형을 뽑은 뒤 인형이 없으므로 0 처리
                break
        if len(answer) >= 2 and answer[-2] == answer[-1]: # 스택에 들어올때 마지막것과 같으면 둘다 제거
            answer.pop()
            answer.pop()
            result += 2

    return result
  
  #구현문제는 문제가 시키는대로 하나씩 구현하기
  #처음에 문제를 잘못 읽어서 오래걸렸던 문제
  
