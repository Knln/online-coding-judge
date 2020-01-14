n, m = input().split()
list = input().split(' ')
a = set(input().split(' '))
b = set(input().split(' '))
happiness = 0
for element in list:
    if element in a:
        happiness = happiness + 1
    if element in b:
        happiness = happiness - 1
print(happiness)
