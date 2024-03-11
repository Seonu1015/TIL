# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# 주어진 두 개의 문자열 word1과 word2가 있습니다.
# word1로 시작하여 번갈아가며 문자를 추가하여 두 문자열을 병합합니다.
# 한 문자열이 다른 문자열보다 길면 추가된 문자를 병합된 문자열의 끝에 추가합니다.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

# 풀이
class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ''
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        res += word1[i:]
        res += word2[j:]

        return res

# 다른 사람 풀이를 보고 다시 해봄
class Solution(object):
    def mergeAlternately(self, word1, word2):
        str = ''

        i = 0
        while i < min(len(word1), len(word2)):
            str += word1[i] + word2[i]
            i += 1

        return str + word1[i:] + word2[i:]

sol = Solution()

print(sol.mergeAlternately("ab", "pqrs"))

# 첫 번째 코드에서는 두 문자열을 번갈아가며 처리하기 위해 두 개의 포인터를 사용
# → 문자열의 길이에 비례하는 반복이 발생 → 문자열의 길이가 큰 경우에는 처리 시간이 증가할 수 있음

# 두 번째 코드에서는 두 문자열의 길이 중에서 더 작은 길이를 찾아 일르 기준으로 반복문을 실행
# → 더 적은 반복 횟수로 같은 작업을 수행
# → 또한 문자열 결합을 위해 + 연산자를 사용하는 것이 아니라 문자열을 직접 더하는 방식을 사용

# 시간 복잡도는 두 경우 모두 O(n)

