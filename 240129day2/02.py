def count_times(N): 
#경우의 수를 세기 위한 변수
    count = 0
# hour, minutes, second에 대한 for 반복문
# 0부터 N까지 hour
    for hour in range(N + 1):
# 0부터 59까지 minute
        for minute in range(60):
# 0부터 59까지 second
            for second in range(60):
# 만약, hour, minutes, second 중에서 하나라도 3을 포함하면 값 반환
                if ‘3’ in str(hour) or ‘3’ in str(minute) or ‘3’ in str(second):
                    count = count + 1
# 총 회수 반환
                    return count
# 결과 출력
                result = count_times(N)
                print(result)