# 주식 가격 ★★

# 초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않는 기간은 몇 초인지를 반환하도록 solution() 구현

# prices = [1, 2, 3, 2, 3] → [4, 3, 1, 1, 0]

# 가격이 처음으로 떨어지는 지점까지의 길이를 구하면?
# 인덱스 사용?
# prices[2]가 처음 떨어지는 지점은 prices[3] → 길이는 1 → 1초 반환

def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([1, 6,  9, 5, 3, 2, 7]))