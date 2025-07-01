def solution(n, lost, reserve):
    common = [x for x in reserve if x in lost]
    lost = [x for x in lost if x not in common]
    reserve = [x for x in reserve if x not in common]
    lost.sort()
    count=0
    for l in lost:
        if l-1 in reserve:
            count+=1
            reserve.remove(l-1)
        elif l+1 in reserve:
            count+=1
            reserve.remove(l+1)
    answer = n-(len(lost)-count)
    return answer