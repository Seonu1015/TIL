# There are n kids with candies.
# You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


# 아이들이 각각 사탕을 가지고 있습니다.
# candies는 정수 배열로, 각 candies[i]는 i번째 아이가 가지고 있는 사탕의 개수를 나타내며,
# extraCandies는 당신이 가지고 있는 추가 사탕의 개수를 나타냅니다.

# 모든 extraCandies를 i번째 아이에게 주고 나서, 해당 아이가 모든 아이 중 가장 많은 사탕을 가질 경우,
# 해당 아이가 모든 아이 중 가장 많은 사탕을 가지고 있는지 여부를 나타내는 길이가 n인 부울 배열 result를 반환합니다.
# 그렇지 않은 경우 false가 됩니다.

# 여러 아이가 가장 많은 사탕을 가질 수 있음에 유의하십시오.

# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false] 
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        for i in range(len(candies)):
            plusCandies = candies[i] + extraCandies
            if max(candies) <= plusCandies:
                result[i] = True
        return result

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for i in candies:
            if max_candies <= i + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
    
sol = Solution()

print(sol.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3))  # Output: [true,true,true,false,true] 
print(sol.kidsWithCandies([4,2,1,1,2], 1))  # Output: [true,false,false,false,false] 
print(sol.kidsWithCandies([12,1,12], 10))   # Output: [true,false,true]

# 첫 번째 코드
# 모든 아이에 대해 추가 사탕을 더한 후에 비교를 수행하기 때문에 추가적인 반복이 필요

# 두 번째 코드
# 최대 사탕 개수를 한 번만 계산하고 각 아이의 사탕 개수를 순회하면서 추가 사탕을 더해 비교하기 때문에 조금 더 효율적

# 두 코드 모두 시간 복잡도가 O(n)으로 동일, but 두 번째 코드가 조금 더 간결하고 효율적