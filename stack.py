from collections import deque

stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append('T')
stack.append('a')
stack.append('e')
stack.append('h')
stack.append('o')

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
stack.pop()
stack.pop()
print(stack.pop())

print(stack)