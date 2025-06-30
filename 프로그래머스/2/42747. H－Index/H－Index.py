# 기존의 코드의 반례
# [1,4,5,9,13,16,16,17,18,20]

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c<i+1:
            return i
    # [9999,9998,9997,9996] 과연 이 반례를 생각할 수 있을까.. 시험장에서... 시험장 나오기 전에 최대한 다양한 반례로 테스트 해보고 나와야 한다.
    # 이 문제에서 중요한 건 인덱스(갯수)와 원소 값. 각각이 최대, 최소일때, 원소값에 비해서 각각의 값이 매우  클때, 매우 자을때 등을 비교해 봐야 한다.
    answer = len(citations)
    return answer