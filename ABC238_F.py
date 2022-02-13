import io
import sys

_INPUT = """\
6
4 2
2 4 3 1
2 1 4 3
33 16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
15 7
4 9 7 5 6 13 2 11 3 1 12 14 15 10 8
4 14 9 12 7 15 1 2 8 11 3 5 13 6 10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,K=map(int,input().split())
  P=list(map(int,input().split()))
  Q=list(map(int,input().split()))
  O=[[P[i],Q[i]] for i in range(N)]
  O.sort(key=lambda x: x[0])
  O=[O[i][1]-1 for i in range(N)]
  dp=[[[0]*(N+1) for j in range(N+1)] for i in range(N+1)]
  dp[0][0][N]=1
  #i番目の人まで見る
  for i in range(N):
    #j人選ぶ
    for j in range(N+1):
      #選ばれなかった人の一番小さい順位
      for k in range(N+1):
        dp[i+1][j][min(k,O[i])]=(dp[i+1][j][min(k,O[i])]+dp[i][j][k])%mod
        if j<N and O[i]<k:
          dp[i+1][j+1][k]=(dp[i+1][j+1][k]+dp[i][j][k])%mod
  print(sum(dp[-1][K])%mod)