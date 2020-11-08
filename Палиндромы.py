chislo = int(input())
count = 0
c = chislo
while c > 0:
    count += 1
    c = c // 10
c = 0
if count % 2 != 0:
    for i in range(1, int((count-1)/2)+1):
        a = chislo % (10 ** i) // (10 ** (i-1))
        b = chislo // (10 ** (count - i)) % 10
        if a != b:
            c += 1
else:
    for i in range(1, int(count)):
        a = chislo % (10 ** i) // (10 ** (i-1))
        b = chislo // (10 ** (count - i)) % 10
        if a != b:
            c += 1
if c != 0:
    print("Не палиндром")
else:
    print("Палиндром")