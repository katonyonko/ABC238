import io
import sys

_INPUT = """\
6
2
1 8
4 2
4
201408139683277485 381410962404666524
360288799186493714 788806911317182736
18999951915747344 451273909320288229
962424162689761932 1097438793187620758
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for i in range(T):
    a,s=map(int,input().split())
    ans='Yes'
    k=0
    for i in range(61):
      #1,1ではない
      if (a>>i)&1==0:
        if (s>>i)&1==0:
          if k==0:
            pass
          else:
            pass
        #足すと1
        else:
          if k==0:
            pass
          else:
            k=0
      #1,1
      else:
        if (s>>i)&1==0:
          if k==0:
            k=1
          else:
            ans='No'
        else:
          if k==0:
            ans='No'
          else:
            pass
    if k==1: ans='No'
    print(ans)