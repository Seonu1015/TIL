# Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid;
# there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits
# and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 100,000.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# 인코딩된 문자열이 주어졌을 때, 해당 문자열을 디코딩하여 반환합니다.

# 인코딩 규칙은 다음과 같습니다: k[인코딩된_문자열],
# 여기서 대괄호 내에 있는 인코딩된 문자열이 k번 반복됩니다.
# k는 양의 정수임이 보장됩니다.

# 입력 문자열이 항상 유효하다고 가정합니다;
# 추가 공백이 없으며, 대괄호가 잘 형성되어 있습니다 등.
# 또한, 원래 데이터에 숫자가 포함되어 있지 않으며, 숫자는 반복 횟수 k만을 위한 것입니다.
# 예를 들어, 3a나 2[4]와 같은 입력이 없습니다.

# 테스트 케이스는 출력의 길이가 항상 100,000를 초과하지 않도록 생성됩니다.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ""

        for c in s:
            if c.isdigit():
                curNum = curNum*10 + int(c)
            elif c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * num
            else:
                curString += c

        return curString
    
sol = Solution()

print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]")) # a2[c]a2[c]a2[c] > accaccacc
print(sol.decodeString("2[abc]3[cd]ef"))