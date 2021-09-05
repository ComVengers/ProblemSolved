import sys
input = sys.stdin.readline

def init(start, end, idx):
    # Base case
    if start == end:
        tree[idx] = number[start]
        return tree[idx]

    # Recursive case
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

def change_num(start, end, idx, num, tree_idx):
    # Base case
    if idx < start or idx > end:
        return

    # Rercursive case
    tree[tree_idx] += num

    # leaf 노드가 아닌 경우에 관련 부모 노드의 값도 변경해줘야 함
    if start != end:
        change_num(start, (start+end)//2, idx, num, tree_idx*2)
        change_num((start+end)//2+1, end, idx, num, tree_idx*2+1)
        return tree

def sum_num(start, end, idx1, idx2, tree_idx):
    # Base case
    if idx1 > end or idx2 < start:
        return 0

    # Recursive case
    # [idx1:idx2]가 [start:end] 범위에 있어야 함!
    if idx1 <= start and idx2 >= end:
        return tree[tree_idx]

    result = sum_num(start, (start+end)//2, idx1, idx2, tree_idx*2) + sum_num((start+end)//2+1, end, idx1, idx2, tree_idx*2+1)
    return result

N, M, K = map(int, input().split())
number = []
tree = [0] * (N*4)

for _ in range(N):
    number.append(int(input()))

init(0, len(number)-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        change_num(1, len(number), b, c-number[b-1], 1)
        number[b-1] = c
    elif a == 2:
        print(sum_num(1, len(number), b, c, 1))