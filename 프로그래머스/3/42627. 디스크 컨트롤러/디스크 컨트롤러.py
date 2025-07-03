import heapq

def solution(jobs):
    n = len(jobs)
    heapq.heapify(jobs)
    queue=[]    
    total_time = 0
    current_time = 0
    while(jobs or queue):
        if queue==[]:
            queue.append(heapq.heappop(jobs))
            current_time  = queue[0][0]
        task = queue[0]
        total_time+=(current_time + task[1]-task[0])
        current_time +=task[1]
        queue.pop(0)
        while(jobs):
            if jobs[0][0]<=current_time:
                queue.append(heapq.heappop(jobs))
            else:
                break
        if (queue):        
            queue.sort(key = lambda x:(x[1],x[0]))

    return int(total_time/n)