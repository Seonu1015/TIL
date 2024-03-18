# Asteroid Collision

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size,
# and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.

# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

# 주어진 정수 배열 asteroids는 한 줄에 있는 소행성을 나타냅니다.

# 각 소행성에 대해 절대값은 크기를 나타내고,
# 부호는 방향을 나타냅니다(양수는 오른쪽으로, 음수는 왼쪽으로).
# 모든 소행성은 동일한 속도로 이동합니다.

# 모든 충돌 후 소행성의 상태를 찾으세요.
# 두 개의 소행성이 만나면 더 작은 것이 폭발합니다.
# 두 소행성의 크기가 같으면 둘 다 폭발합니다.
# 같은 방향으로 이동하는 두 소행성은 결코 만나지 않습니다.

from typing import List

class Solution:
    def astroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
    
sol = Solution()

print(sol.astroidCollision([5, 10, -5]))   # [5, 10]
print(sol.astroidCollision([8, -8]))       # []
print(sol.astroidCollision([10, 2, -5]))   # [10]