import io
import sys

_INPUT = """\
6
4
90 180 45 195
1
1
10
215 137 320 339 341 41 44 18 241 149
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  cut=[0]
  for i in range(N):
    cut.append((cut[-1]+A[i])%360)
  cut.sort()
  ans=0
  for i in range(N):
    ans=max(ans,cut[i+1]-cut[i])
  ans=max(ans,360-cut[-1])
  print(ans)