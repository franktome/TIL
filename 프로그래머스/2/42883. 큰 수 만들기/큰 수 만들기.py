# 계속 시간 초과 뜬다. number와 k가 모두 100만이라서 2중 반복문 쓰면 최악의 경우 10^12번 돌아가서 시간 초과 
def solution(number, k):
    stack = []
    for num in number:
        while k and stack and stack[-1]< num:
            stack.pop()
            k-=1
        stack.append(num)
    if k>0:
        n=len(stack)
        stack = stack[:n-k]
    answer = ''
    for i in stack:
        answer += i
    return answer