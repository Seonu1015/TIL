# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# 주어진 문자열 s에서 모음만 거꾸로 배치하고 그것을 반환하세요.
# 모음은 'a', 'e', 'i', 'o', 'u'이며, 대소문자를 가리지 않고 여러 번 나타날 수 있습니다.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_vowels = [char for char in s if char in vowels]
        s_list = list(s)

        for i, char in enumerate(s_list):
            if char in vowels:
                s_list[i] = s_vowels.pop()  # s_vowels에서 마지막 모음을 가져와 현재 위치의 문자로 대체

        return ''.join(s_list)
    
sol = Solution()

print(sol.reverseVowels("hello"))