import sys

s = set()
l = input()
for i in sys.stdin:
    s.add(i.strip())
print(len(s))
