def solution(answers):
    n = len(answers)
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    a1 = n//5
    a2 = n%5
    b1 = n//8
    b2 = n%8
    c1 = n//10
    c2 = n%10
    af=a*a1+a[:a2]
    bf=b*b1+b[:b2]
    cf=c*c1+c[:c2]
    count_a, count_b, count_c=0,0,0
    
    for i in range(n):
        if answers[i]==af[i]:
            count_a+=1
        if answers[i]==bf[i]:
            count_b+=1
        if answers[i]==cf[i]:
            count_c+=1
    k =max(count_a,count_b,count_c)
    answer = []
    if count_a==k:
        answer.append(1)
    if count_b==k:
        answer.append(2)
    if count_c==k:
        answer.append(3)
    if k==0:
        answer=[]
    return answer