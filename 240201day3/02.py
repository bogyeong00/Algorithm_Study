'''
CHAP6. 정렬
2. 위에서 아래로
문제:
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다.
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램
을 만드시오.
입력 조건:
첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1<=N<=500)
둘째 줄부터 N+1 번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의
자연수이다.
'''

n = int(input()) # 숫자의 개수 n 입력받기
total_numlist = [0] * n # 리스트 변수 생성
# 입력받은 수열을 입력받아 리스트에 저장
for i in range(n):
  num = int(input())
  total_numlist[i] = num
# 입력받은 수열을 내림차순으로 정렬
for i in range(n -1):
   for j in range(i +1, n):
    if total_numlist[i] < total_numlist[j]:
 # swap
      total_numlist[i], total_numlist[j] = total_numlist[j], total_numlist[i]
# 결과 출력
for num in total_numlist:
 print(num, end='')
