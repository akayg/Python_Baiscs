from collections import deque
dq= deque()

dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
dq.appendleft(0)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
