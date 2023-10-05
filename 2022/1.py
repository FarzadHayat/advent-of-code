# Day 1: Calorie Counting

file = open("1.in", "r").read()
lines = file.splitlines()

curr = 0
most = 0

for line in lines:
    line = line.strip()
    if line == "":
        most = max(most, curr)
        curr = 0
    else:
        curr += int(line)

print(most)

# Part Two

import heapq

k = 3

file = open("1.in", "r").read()
lines = file.splitlines()

curr = 0
heap = []

for line in lines:
    line = line.strip()
    if line == "":
        heapq.heappush(heap, -curr)
        curr = 0
    else:
        curr += int(line)

sum = 0
for i in range(k):
    sum -= heapq.heappop(heap)
print(sum)
