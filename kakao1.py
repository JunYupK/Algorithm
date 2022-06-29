from collections import deque
data = ["a", "MUZI", "muzi", "mUzi","a","ac","b","add"]
q = deque(data)
q = q.reverse()
print(data[::-1])