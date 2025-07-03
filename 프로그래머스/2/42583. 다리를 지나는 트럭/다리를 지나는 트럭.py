from collections import deque 

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 현재 도로 위의 자동차의 무게 
    present_weight=0
    queue = deque([0] * bridge_length)
    # 다리를 대기하는 제일 앞 쪽 자동차 인덱스
    idx = 0
    while(idx<len(truck_weights)):
        # 무조건 자동차이든 빈값이든 빼냄
        past = queue.popleft()
        present_weight-=past
        # 만약 다리위에 차를 올릴 수 있으면 올리기
        if present_weight + truck_weights[idx] <= weight:
            present_weight+=truck_weights[idx]
            queue.append(truck_weights[idx])
            idx+=1
        # 만약 다리위에 차릉 못올릴 것 같으면 빈값 넣기
        else:
            queue.append(0)
        answer +=1
    answer+=bridge_length # 가장 마지막에 들어간 자동차의 도로위 시간 계산
            
    return answer