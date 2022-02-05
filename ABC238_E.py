import io
import sys

_INPUT = """\
6
3 3
1 2
2 3
2 2
4 3
1 3
1 2
2 3
4 4
1 1
2 2
3 3
1 4
4 1
1 4
5 5
1 2
2 3
2 5
3 3
3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #BFS
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  N,Q=map(int,input().split())
  G=[[] for _ in range(N+1)]
  for i in range(Q):
    l,r=map(int,input().split())
    G[l-1].append(r)
    G[r].append(l-1)
  if bfs(G,0)[-1]==10**30:
    print('No')
  else:
    print('Yes')