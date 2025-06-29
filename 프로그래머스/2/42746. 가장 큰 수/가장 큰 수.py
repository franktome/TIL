def solution(numbers):
    answer = ''
    tmp=[]
    s= list(map(str, numbers))
    for i in range(len(s)):
        tmp.append(   (s[i], (s[i]*4)[:4] ))
    tmp.sort(key = lambda x: x[1],reverse = True)
    for a,b in tmp:
        answer+=a
    
    return str(int(answer))