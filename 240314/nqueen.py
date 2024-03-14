'''
3344
'''

# 사용자로부터 정수를 입력받음
n = int(input())

# 답을 저장할 변수 초기화
ans = 0

# 각 행에 퀸의 위치를 저장하는 리스트 초기화
row = [0] * n


# 해당 위치에 퀸을 놓을 수 있는지 확인하는 함수
def is_promising(x):
    # 현재 위치 x보다 앞에 있는 행들을 확인
    for i in range(x):
        # 같은 열에 퀸이 있는지 또는 대각선 상에 퀸이 있는지 확인
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False  # 불가능한 경우 False 반환

    return True  # 가능한 경우 True 반환


# n_queens 알고리즘을 재귀적으로 구현하는 함수
def n_queens(x):
    global ans  # 전역 변수 ans 사용

    # 모든 행에 퀸을 놓았다면
    if x == n:
        ans += 1  # 답의 개수를 증가시키고
        return  # 함수 종료

    else:
        # 현재 행에 대해 모든 열을 확인하면서 가능한 경우에만 진행
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            # 현재 위치에 퀸을 놓는 것이 유망한지 확인
            if is_promising(x):
                # 유망하다면 다음 행으로 진행
                n_queens(x + 1)


# n_queens 함수 호출하여 실행
n_queens(0)

# 답 출력
print(ans)