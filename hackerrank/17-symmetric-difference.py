a = input()
listA = set(input().split())
b = input()
listB = set(input().split())

listC = listA.union(listB) - listA.intersection(listB)
listC = [int(x) for x in listC]
listC = sorted(listC)
for element in listC:
    print(element)
