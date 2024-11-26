import heapq

heap = []
caches = {}

def update(key):
    value, counter = caches[key]
    caches[key] = (value, counter + 1)
    heapq.heappush(heap, (counter + 1, key))

def get(key):
    if key not in caches:
        return -1
    update(key)
    return caches[key][0]

def put(key, value, capacity):
    if key in caches:
        caches[key] = (value, caches[key][1])
        update(key)
        return
    if len(caches) >= capacity:
        remove()
    caches[key] = (value, 1)
    heapq.heappush(heap, (1, key))

def remove():
    while heap:
        counter, key = heapq.heappop(heap)
        if key in caches and caches[key][1] == counter:
            del caches[key]
            return

def solve(n, q, operations):
    result = []
    for t, key, value in operations:
        if t == 1:
            result.append(get(key))
        else:
            put(key, value, n)
    return result

print(solve(2, 7, [[2, 2, 3], [2, 1, 2], [2, 1, 5], [2, 3, 4], [1, 1, -1], [1, 2, -1], [1, 3, -1]]))