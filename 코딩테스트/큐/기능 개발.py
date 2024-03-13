# 기능 개발 ★★

# 각 기능은 진도가 100%일 때 서비스에 반영
# 각 기능의 개발속도는 모두 다름
# 뒤의 기능이 앞의 기능보다 먼저 개발 될 경우 뒤의 기능은 앞의 기능이 배포될 때 함께 배포

# 배포 순서대로 작업 진도가 적힌 정수 배열 progresses
# 개발 속도가 적힌 정수 배열 speeds
# 이 때, 각 배포마다 몇개의 기능이 배포되는지 반환

# progresses = [93, 30, 55] speeds = [1, 30, 5] → [2, 1]
# progresses = [95, 90, 99, 99, 80, 99] speeds = [1, 1, 1, 1, 1, 1] → [1, 3, 2]

from collections import deque
import math

def solution(progresses, speeds):
    days = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))]
    max_day = days[0]
    answer = []
    count = 0
    for i in range(len(days)):
        if days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days[i]
    answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))   # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))   # [1, 3, 2]