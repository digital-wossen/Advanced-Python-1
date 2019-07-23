# JTSK-350112
# a1 6.py

def is_empty(pq):
    return len(pq) <= 0

def insert_with_priority(pq, x, p):
    pq.append((x, p))

def pull_highest_priority_element(pq):
    if is_empty(pq):
        return -1
    ind = 0
    min = pq[0][1]
    for i in range(len(pq)):
        if pq[i][1] < min:
            index = i
            min = pq[i][1]
    temp = pq.pop(ind)
    return temp
pq = []
insert_with_priority(pq, 5, 2)
print(pq)
insert_with_priority(pq, 3, 3)
print(pq)
insert_with_priority(pq, 13, 1)
print(pq)
insert_with_priority(pq, 6, 1)
print(pq)
pull_highest_priority_element(pq)
print(pq)
print(is_empty(pq))