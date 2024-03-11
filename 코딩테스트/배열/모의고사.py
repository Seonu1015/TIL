# 모의고사 ★

# 수포자는 삼인방은 모의고사에 수학 문제를 전부 찍으려고 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 1번 수포자: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 1번 수포자: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정담이 순서대로 저장된 배열 answers가 주어졌을 때
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환하도록 solution() 함수를 구현

# 제약조건
# - 시험은 10,000 문제로 구성
# - 문제의 정답은 1, 2, 3, 4, 5 중 하나
# - 가장 높은 점수를 맏은 사람이 여럿이라면 반환하는 값을 오름차순으로 정렬

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0] * 3

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                # 문제가 10번까지 있을 경우 패턴이 반복되는 상황을 체크하기 위해 pattern의 인덱스를 i % len(pattern)로 계산
                scores[j] += 1

    max_score = max(scores)

    highest = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest.append(i+1)

    return highest

print(solution([1, 3, 2, 4, 2]))
print(solution([1, 4, 2, 4, 2]))
print(solution([1, 3, 2, 1, 5]))