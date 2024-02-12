'''
음료수 얼려 먹기
N * M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.
입력 조건
    첫 번째 줄에 얼음 틀의 새로 길이 N과 가로 길이 M이 주어진다.( 1<=N, M <= 1000)
    두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
    이때 구멍이 뚫여있는 부분은 0, 그렇지 않은 부분은 1이다.
출력 조건
    한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
'''

n, m = map(int,input().split())

# 2차원 리스트 생성
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
 
answer = 0 
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m: # 만약 범위를 벗어난다면 종료, 가지 않음
        return False
    
    if graph[x][y] == 0:  # 현재 노드가 방문하지 않은 곳이면
        graph[x][y] = 1  # 해당 노드에 방문한 표시
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
    return False  # 범위 안인데 이미 방문한 곳이라면? 의 조건을 주어야 함

# 상 하 좌 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:  # dfs가 1번 끝나면
            answer+=1  # answer에 1 추가, 연결된 0들은 모든 숫자가 바뀌었는지
 
print(answer)
