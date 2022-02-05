import io
import sys

_INPUT = """\
6
5
2
623947744
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n=int(input())
  if 2**n>n**2:
    print('Yes')
  else:
    print('No')