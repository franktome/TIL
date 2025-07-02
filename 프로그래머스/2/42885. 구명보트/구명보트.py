def solution(people, limit):
    # 무거운 사람부터 보자
    people.sort(reverse = True)
    h_start = 0
    l_start = len(people)-1
    count=0
    while(l_start>h_start):
        if people[h_start] + people[l_start]<=limit:
            count+=1
            h_start+=1
            l_start-=1
        else:
            h_start+=1
            count+=1
        # 끝까지 한 사람씩 들어간 경운는 인덱스가 서로 같게 되고 마지막 사람이 count가 안된다. 이 부분은 따로 처리
        if (l_start==h_start):
            count+=1
    
         
    return count