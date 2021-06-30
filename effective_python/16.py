## get

# counters = {"품퍼니켈": 2, "사워도우": 2}
# key = "밀"
# count = counters.get(key, 0)  # 키가 없으면 추가해주고 value 0 설정
# counters[key] = count + 1
# print(counters)

## warlus opeartor
# key = "쌀"
# if (count := counters.get(key)) is None:
#     counters[key] = 10  # 없으면 새로 추가
# else:
#     print(counters.get(key))


## Counter
import collections

# a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
h = "hello"
b = collections.Counter(h)
print(b)

# b = collections.Counter(a)  # Counter: 아이템에 대한 개수를 계산해 딕셔너리로 리턴한다.
# print(b)
# print(b.most_common(1))

## ex
# participant_1 = ["leo", "kiki", "eden"]
# completion_1 = ["eden", "kiki"]
# participant_2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion_2 = ["josipa", "filipa", "marina", "nikola"]
# participant_3 = ["mislav", "stanko", "mislav", "ana"]
# completion_3 = ["stanko", "ana", "mislav"]

# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)

#     print(answer)  # Counter 객체
#     print(answer.keys())  # key(이름)만 뽑는다
#     print(list(answer.keys()))  # dict_keys -> list
#     print(list(answer.keys())[0])  # list의 0번째 원소

#     return list(answer.keys())[0]


# print(solution(participant_1, completion_1))
# print(solution(participant_2, completion_2))
# print(solution(participant_3, completion_3))

## setdefault
