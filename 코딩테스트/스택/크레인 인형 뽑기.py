# 크레인 인형 뽑기 게임 ★★

# 게임 화면은 1x1 크기의 격자로 구성된 NxN 크기의 격자
# 인형이 담긴 N x N 크기의 인형이 담긴 배열이 있고
# 크레인을 작동시킨 위치 moves가 주어질 때,
# 크레인을 모두 작동 시킨 후 사라진 인형의 개수를 반환

# 같은 인형이 2칸 쌓이면 펑 터지면서 사라짐
# 인형이 없는 곳은 아무 일도 일어나지 않음

# 배열(인형이 담긴 배열)
# [[0,0,0,0,0],
#  [0,0,1,0,3],
#  [0,2,5,0,1],
#  [4,2,4,4,2],
#  [3,5,1,3,1]]

# 크레인을 작동시킨 위치
# moves = [1, 5, 3, 5, 1, 2, 1, 4]

# 결과 → 4

def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    return answer

board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))

# 시간 복잡도는 크레인이 작동한 위치마다 해당 열을 순회하면서 인형을 찾고 처리하기 때문에 O(N)

# 해설지 풀이
def solution(board, moves):
    lanes = [[] for _ in range(len(board[0]))]

    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])

    bucket = []
    answer = 0

    for m in moves:
        if lanes[m-1]:
            doll = lanes[m-1].pop()
            if bucket and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)

    return answer

# 앞서 직접 푼 코드는 주어진 보드를 순회하면서 크레인이 인형을 집는 동작을 구현
# 각 열에서 해당 열의 맨 위부터 인형이 있는지 확인하고, 만약 인형이 있다면 스택에 추가하고 격자를 비워줌

# 해설지는 보드를 순회하여 각 열마다 해당 열의 인형을 스택에 넣어주는 방식을 사용
# 크레인이 작동한 위치에서 스택을 확인하여 인형을 처리하는 방식

# 두 코드 모두 시간 복잡도는 크게 차이나지 않음. O(M*N)의 시간 복잡도