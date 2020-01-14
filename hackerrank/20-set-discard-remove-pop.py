import sys

n = int(input())
s = set(map(int, input().split()))
ops = int(input())

sentaku = {}
for line in sys.stdin:
    line = line.strip()
    sentaku = line.split(' ')
    if(sentaku[0] == "remove"):
        s.remove(int(sentaku[1]))
    if(sentaku[0] == "pop"):
        s.pop()
    if(sentaku[0] == "discard"):
        s.discard(int(sentaku[1]))
        
print(sum(s))
