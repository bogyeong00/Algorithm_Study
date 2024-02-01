'''
CHAP6. 정렬
3. 성적이 낮은 순서로 학생 출력하기
문제:
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프
로그램을 작성하시오.
입력 조건:
첫 번째 줄에 학생 수 N이 입력된다. (1 ≤ N ≤ 100,000)
두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타
내는 정수B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.
'''

n = int(input()) # 학생의 수 n 입력받기
student_list = [] # 리스트 변수 생성
# 학생 정보를 입력받아 리스트에 저장
for i in range(n):
  student_info = list(input(). split()) # 리스트???????
  name = student_info[0] # 학생 이름 변수 생성, 인덱스 0번
  score = int(student_info[1]) # 학생 점수 변수 생성, 인덱스 1번
  student_list += [(name, score)]
# 성적이 낮은 순서대로 정렬 (선택 정렬)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
    if student_list[j][1] < student_list[min_index][1]:
      min_index = j
 # swap
      student_list[i], student_list[min_index] = student_list[min_index], student_list[i]
# 결과 출력
for student in student_list:
  print(student[0], end = '')
