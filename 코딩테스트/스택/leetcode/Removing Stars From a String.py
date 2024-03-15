# Removing Stars From a String


# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.


# 문자열 s가 주어지는데, 이 문자열은 별표 *를 포함합니다.

# s에서 별표를 선택합니다.
# 해당 별표의 왼쪽에 있는 가장 가까운 별표가 아닌 문자를 제거하고, 별표 자체도 제거합니다.
# 모든 별표가 제거된 후의 문자열을 반환합니다.

# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"

# Example 2:
# Input: s = "erase*****"
# Output: ""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

sol = Solution()
print(sol.removeStars("leet**cod*e"))
print(sol.removeStars("erase*****"))