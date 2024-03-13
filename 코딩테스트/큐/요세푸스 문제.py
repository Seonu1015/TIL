# 요세푸스 문제 ★★

# N명의 사람이 원 형태로 서 있다
# 각 사람은 1부터 N까지 번호표를 가지고 있다
# 임의의 숫자 K가 주어졌을 때,
# - 1번 번호푤르 가진 사람을 기준으로 K번째 사람을 없앤다
# - 없앤 사람 다음 사람을 기준으로 하고 다시 K번째 사람을 없앤다
# N과 K가 주어질 때 마지막에 살아있는 사람의 번호를 반환하는 solution() 함수를 구현

# N = 5 K = 2 → 3

# [1, 2, 3, 4, 5] 2
# [3, 4, 5, 1] 4
# [5, 1, 3] 1
# [3, 5] 5

from collections import deque

def solution(N, K):
    dq = deque(range(1, N+1))
    while len(dq) > 1:
        for i in range(K-1):
            dq.append(dq.popleft()) # K번째 앞까지는 숫자를 다시 뒤에 붙여준다
            dq.popleft() # 제일 앞으로 밀려온 K번째 숫자는 제거
    return dq[0]

print(solution(5, 2))