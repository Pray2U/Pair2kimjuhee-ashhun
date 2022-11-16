# N-Queens 문제
# 기본 : 같은 행 (row)에는 퀸을 놓지 않는다. 
#       why? 퀸의 이동방향이 가로, 세로, 대각선이니까 
# 조건 1 : 같은 열 (col) 체크
#     col[i] : i번째 행(row)에서 퀸이 놓여있는 열(column)의 위치
#     col[j] : j번째 행(row)에서 퀸이 놓여있는 열(column)의 위치
#     if col[i] == col[j] : 같은 열에 퀸이 놓여있으므로 promising하지 않다!
# 조건 2 : 대각선 (diagonal) 체크, 각 퀸이 위치해 있는 col, row의 차이가 일치하는지 파악
#     left diagonal : differ to col[i], col[j] == differ to row[i] - row[j]
#     right diagonal : abs(differ to col[i], col[j]) == differ to row[i] - row[j]

ans = []
def n_queens(i, col):
    global ans

    def promising(i, col):
        k=1
        flag=True
        while(k<i and flag):
            if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
                flag=False
            k += 1
        return flag

    n = len(col)-1 # index start is 0
    if(promising(i, col)):
        if(i==n):
            # print(col[1: n+1]) # this is answer
            ans.append(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

    return len(ans)


from itertools import combinations, combinations_with_replacement
def brute_force(s, k):
    res = []
    for item in combinations(s, k):
        res.append(sum(item))

    # for item in combinations_with_replacement(s, k):
    #     res.append(sum(item))

    return set(res)


n = 8
col = [0]*(n+1)
print(n_queens(0, col)) # N-Queens의 가짓수

S = [1,2,3,4,5,6,7]
k = 2
print(brute_force(S, k)) # 브루트포스 : 임의의 정수를 뽑아 만든 합의 갯수
