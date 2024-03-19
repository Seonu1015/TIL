# 완주하지 못한 선수 ★

# 많은 선수 중 단 함녕의 선수를 제외하고 모든 선수가 마라톤을 완주했다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완수한 선수들의 이름이 담긴 배열 completion이 있을 때,
# 완주하지 못한 선수의 이름을 반환하는 solution() 을 구현

# participant = ["leo", "kiki", "eden"] completion = ["eden", "kiki"] → leo
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"] completion = ["josipa", "filipa", "marina", "nikola"] → vinko
# participant = ["mislav", "stanko", "mislav", "ana"] completion = ["stanko", "ana", "mislav"] → mislav

def solution(participant, completion):
    hashtable = {}

    for p in participant:
        if p in hashtable:
            hashtable[p] += 1
        else:
            hashtable[p] = 1

    for c in completion:
        hashtable[c] -= 1

    for key in hashtable.keys():
        if hashtable[key] > 0:
            return key
        
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# 문자열의 길이가 길지 않기 때문에 굳이 문자열 해싱까지 진행하지 않아도 충분