n = int(input())
x,y = 1,1
plans = input().split()

direction = [L, R, U, D]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for plan in plans:
  for i in range(len(direction)):
    if plan == direction[i]
      nx = x + dx[plans[i]]
      ny = y + dy[plans[i]]
      
   if nx < 1 and ny <1 and nx > n and ny > n:
     continue;
      
     x = nx
     y = ny
      
print(x,y)

#입력 받은 계획서에서 하나씩 뽑아서 반복
#방향을 나타내는 리스트 생성후 리스트 길이만큼 반복
