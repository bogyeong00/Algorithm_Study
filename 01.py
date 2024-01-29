# 정사각형의 크기 n을 입력
n = int(input())
# 이동 경로
moves = list(map(str, input().split()))
# 여행가 A의 현재 위치
x = 1
y = 1
# L, R, U, D에 따른 이동 방향
direction = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 이동 경로를 확인하여 최종 위치 찾기
for move in moves:
    for i in range(len(direction)):
       if move == direction[i]:
         nx = x + dx[i]
         ny = y + dy[i]
# 공간을 벗어나지 않는지 확인하기 (벗어나면 현재 위치를 새로운 위치로 업데이트)
         if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
            x = nx
            y = ny
            print(x, y)