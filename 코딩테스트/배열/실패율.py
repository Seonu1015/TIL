# 실패율 ★★

# 신규 사용자 수 급감 → 원인: 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것
# 게임 시간을 늘려서 난이도를 조절하기로
# 실패율을 구하는 코드를 완성해보자
# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 개수가 N, 게임을 이용하는 사용자가 현재 멈춰 있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨 있는 배열을 반환하도록

# 제약조건
# 1 <= N <= 500
# 1 <= len(stages) <= 200,000
# stages에는 1 이상 N+1의 자연수 → N+1 은 N까지 클리어한 사용자
# 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
# 스테이지에 도달한 유저가 없는 경우 스테이지 실패율은 0

# N = 5 stages [2, 1, 2, 6, 2, 4, 3, 3] → [3, 4, 2, 1, 5]
# N = 4 stages [4, 4, 4, 4, 4] → [4, 1, 2, 3]

def solution(N, stages):
    challenger = [0] * (N+2)
    for i in stages:
        challenger[i] += 1
    
    fails = {}
    users = len(stages)

    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / users
            users -= challenger[i]

    result = sorted(fails, key=lambda x : fails[x], reverse=True)

    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))