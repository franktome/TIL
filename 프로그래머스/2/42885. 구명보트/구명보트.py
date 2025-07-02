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
        if (l_start==h_start):
            count+=1
    
         
    return count