def solution(numbers, target):
    answer = 0
    
    def dfs(i, value):
        # nonlocal 개념 처음 알아간다.
        nonlocal answer
        if i==len(numbers):
            if value==target:
                answer+=1
            return
        for j in (0,1):
            if i < len(numbers):
                # value를 다시 원래대로 되돌려야 하네
                temp = value
                value = value + numbers[i] if j==0 else value + (-1)*numbers[i]
                dfs(i+1,value)
                value = temp
                
    dfs(0,0)
    return answer