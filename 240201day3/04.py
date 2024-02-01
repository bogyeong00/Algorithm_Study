'''
CHAP6. 정렬
4. 두 배열의 원소 교체
입력 조건:
첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1 <= N <= 100,000, 0<=K<=N)
두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보
다 작은 자연수이다.
세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보
다 작은 자연수이다.
출력 조건:
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출
력한다.
'''

N, K = map(int, input().split())
# 배열 A와 B 입력받기
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    # A에서 가장 작은 값의 인덱스 찾기
    minA_index = A.index(min(A))
    # B에서 가장 큰 값의 인덱스 찾기
    maxB_index = B.index(max(B))
    # swap
    A[minA_index], B[maxB_index] = B[maxB_index], A[minA_index]

# A의 합
result = sum(A)
print(result)
