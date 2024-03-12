# 10진수를 2진수로 변환 ★

# 10진수를 입력받아 2진수로 변환해 반환하는 solution() 구현

def solution(decimal):
    stack = []
    while decimal > 0:
        stack.append(str(decimal % 2))  # 문자열로 변환하여 stack에 push
        decimal //= 2

    binary = ''
    while stack:
        binary += stack.pop()
    return binary

print(solution(10)) # 1010
print(solution(27)) # 11011
print(solution(12345)) # 11000000111001
