# 카드 뭉치 ★★

# 영어 단어가 적힌 카드 뭉치 2개
# - 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용
# - 한 번 사용한 카드는 다시 사용할 수 없음
# - 카드를 사용하지 않고 다음 카드로 넘어갈 수 없음
# - 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없음

# ["i", "drink", "water"], ["want", "to"] → ["i", "want", "to", "drink", "water"] -> "Yes"
# ["i", "water", "drink"], ["want", "to"] → ["i", "want", "to", "drink", "water"] -> "No"

from collections import deque

def solution(card1, card2, goal):
    card1 = deque(card1)
    card2 = deque(card2)
    goal = deque(goal)
    while goal:
        if card1 and goal[0] == card1[0]:
            card1.popleft()
            goal.popleft()
        elif card2 and goal[0] == card2[0]:
            card2.popleft()
            goal.popleft()
        else:
            break
    return "Yes" if len(goal) == 0 else "No"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
