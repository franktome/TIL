def solution(clothes):
    
    answer=1
    count = {}
    for i in range(len(clothes)):
        if clothes[i][1] in count:
            count[clothes[i][1]]+=1
        else:
            count[clothes[i][1]]=1
    for k in count.keys():
        answer*=count[k]+1
    
    return answer-1