# from collections import Counter

# def solution(nums):
#     k = len(nums)/2
#     n = len(Counter(nums))
#     if k>=n:
#         return n
#     elif k<n:
#         return k
#     return answer

# 굳이 Counter안쓰고 set으로 풀 수도 있네
def solution(nums):
    k = len(nums)/2
    n = len(set(nums))
    return min(k,n)