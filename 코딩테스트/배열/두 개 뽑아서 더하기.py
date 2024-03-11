# 두 개 뽑아서 더하기 ★

# 정수 배열 numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를
# 배열에 오름차순으로 담아 반환하는 solution() 함수를 구현

# 제약조건
# - numbers의 길이는 2 이상 100 이하
# - numbers의 모든 수는 0 이상 100 이하

# [2, 1, 3, 4, 1] → [2, 3, 4, 5, 6, 7]
# [5, 0, 2, 7] → [2, 5, 7, 9, 12]

def solution(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            res.append(arr[i] + arr[j])

    res = sorted(set(res))
    return res

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))