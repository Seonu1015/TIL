# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed
# without violating the no-adjacent-flowers rule and false otherwise.

# 일렬로 늘어선 꽃밭이 있습니다.
# 일부 plot에는 꽃이 심어져 있고, 일부 plot에는 비어 있습니다.
# 그러나 인접한 plot에는 꽃을 심을 수 없습니다.

# 0과 1로 이루어진 정수 배열 flowerbed가 주어집니다.
# 여기서 0은 비어 있음을 나타내고, 1은 비어 있지 않음을 나타냅니다.
# 또한 정수 n이 주어집니다.
# 인접한 꽃을 심지 않는 규칙을 위배하지 않고
# 꽃밭에 n개의 새로운 꽃을 심을 수 있는 경우 true를 반환하고, 그렇지 않으면 false를 반환합니다.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# 제한 조건:
# flowerbed.length는 1 이상 2 * 104 이하입니다.
# flowerbed[i]는 0 또는 1입니다.
# flowerbed에는 인접한 두 개의 꽃이 없습니다.
# 0 이상 flowerbed.length 이하인 정수 n입니다.

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0
    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0
        while i < length:
            if flowerbed[i] == 0:
                next = flowerbed[i+1] if i < length - 1 else 0  # flowerbed 배열의 맨 끝에 도달할 경우 다음 수로 0을 반영해두기 위해 추가

                if next == 0:
                    n -= 1
                    i += 2  # 0, 0 이므로 해당 i에 꽃을 심어서 1, 0이 되었으니 두칸 건너게끔 처리
                else:
                    i += 1  # 0, 1 이므로 해당 i에는 꽃을 심을 수 없으니 다음으로 넘김

                if n == 0:
                    return True
            else:
                i += 2
        return n <= 0
    
sol = Solution()

print(sol.canPlaceFlowers([1,0,0,0,1], 1))
print(sol.canPlaceFlowers([1,0,0,0,1], 2))
print(sol.canPlaceFlowers([0,0,1,0,0], 1))

# 시간 복잡도는 동일, O(n)

# 첫 번째 코드
# 리스트 슬라이싱을 사용하여 flowerbed 배열을 확장하고 수정 → 메모리를 더 사용할 수 있다

# 두 번째 코드
# while 루프를 사용하여 flowerbed 배열을 탐색하고, 현재 요소와 다음 요소를 검사하여 꽃을 심을 수 있는지 확인합니다.
# 인덱스를 직접 조작하여 flowerbed 배열을 수정하므로 메모리 사용량이 적을 수 있다