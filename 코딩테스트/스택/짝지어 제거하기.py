# 짝지어 제거하기 ★

# 알파벳 소문자로 구성된 문자열에서 같은 알파벳이 2개 붙어있는 짝을 찾는다
# 짝을 찾은 다음 그 둘을 제거하고 앞뒤로 문자열을 이어붙인다
# 이 과정을 반복해서 문자열을 모두 제거하면 짝지어 제거하기가 종료
# 성공적으로 수행되면 1을 아니면 0을 반환하는 solution() 함수 구현

# s = "baabaa" → 1
# s = "cdcd" → 0

def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    return 1 if not stack else 0

print(solution("baabaa"))
print(solution("cdcd"))
print(solution("baacaa"))