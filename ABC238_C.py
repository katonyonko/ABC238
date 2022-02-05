import io
import sys

_INPUT = """\
6
16
238
999999999999999999
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  mod=998244353
  ans=(N*(N+1)//2)%mod
  k=max([i for i in range(20) if N//(10**i)>0])
  for i in range(k):
    ans=(ans-(10**i-1)*9*(10**i))%mod
  ans=(ans-(10**k-1)*(N-10**k+1))%mod
  print(ans)