'''
팀 결성
학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다. 처음에는 모든 학생이 서로 다른 팀으로 구분되어,
총 N + 1개의 팀이 존재한다. 이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.
1. '팀 합치기' 연산은 두 팀을 합치는 연산이다.
2. '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.
[입력 조건]
1. 첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다. (1 <= N, M <= 100,000)
2. 다음 M개의 줄에는 각각의 연산이 주어진다.
3. '팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
4. '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
5. a와 b는 N 이하의 양의 정수이다.
[출력 조건]
'같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.
'''

# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:  # 만약 현재 노드의 부모가 자기 자신이 아니라면
        parent[x] = find_parent(parent, parent[x])  # 부모 노드를 찾을 때까지 재귀적으로 호출하며 경로 압축을 수행
    return parent[x]  # 최종 부모 노드를 리턴

# 두 팀을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)  # a의 부모
    b = find_parent(parent,  b)  # b의 부모
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)  # 각 학생의 부모 노드를 저장할 리스트를 초기화

# 초기에는 각 학생이 자신의 팀이므로 자기 자신을 부모로 초기화
for i in range(0, n + 1):
    parent[i] = i

# 연산을 수행
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:  # 합집합(union) 연산인 경우
        union_parent(parent, a, b)
    elif oper == 1:  # 찾기(find) 연산인 경우
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
