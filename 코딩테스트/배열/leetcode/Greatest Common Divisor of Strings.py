# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
# (i.e., t is concatenated with itself one or more times)
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2

# 두 개의 문자열 s와 t에 대해, "t가 s를 나눈다"라고 말할 때는 오직 s가 t + t + t + ... + t + t (즉, t가 자신을 한 번 이상 연결한 것)인 경우에만 해당합니다.
# 두 개의 문자열 str1과 str2가 주어졌을 때, str1과 str2 모두를 나누는 가장 큰 문자열 x를 반환하세요.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):  # 두 문자열 길이의 최대 공약수를 구하는 함수
            while b:    # while b > 0: 으로 작성하지 않아도 된다. 파이썬에서 0은 False로 처리되기 때문!
                a, b = b, a % b
            return a
        
        length = gcd(len(str1), len(str2))

        return str1[:length]

sol = Solution()

print(sol.gcdOfStrings("ABCABC", "ABC"))
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print(sol.gcdOfStrings("LEET", "CODE"))

