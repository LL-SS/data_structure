from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append('태호')
queue.append('현승')
queue.append('지웅')
queue.append('동욱')
queue.append('신의')

# 큐의 가장 앞 데이터에 접근
print(queue[0])

# 큐의 맨 앞 데이터 삭제
queue.popleft()
queue.popleft()
print(queue.popleft())

print(queue)