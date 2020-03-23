table = data.split('\n')
table_all = [i.rstrip(';;;').split(';') for i in table]
c = []
col = input().split(' ')

if len(col) == 1:
    for h in table_all[: int(col[0]) + 1]:
        print(*h, sep='\t')

elif len(col) == 2:
    for i in table_all[1:-5]:
        if col[1] == i[1]:
            c.append(i[0])
    for j in c[:int(col[0])]:
        print(*j, ' | Школа №' + str(col[1]), sep='')

elif len(col) == 3:
    for i in table_all[1:-5]:
        if col[1] == i[1] and int(i[2]) + int(i[3]) < int(col[2]):
            c.append(i)
    for j in c[:int(col[0])]:
        print(*j[0], ' | Школа №' + str(col[1]), ' | ', int(j[2]) + int(j[3]), sep='')

table = data.split('\n')
table_all = [i.rstrip(';;;').split(';') for i in table]
c = []
col = input().split(' ')


num = int(input())
table = data.split('\n')
c = 0
table_all = [i.rstrip(';;;').split(';') for i in table]

for j in table_all[1: -5]:
    if num == int(j[1]):
        c += 1
        print(*j, sep='\t')
print()
print('Количество учеников в школе №' + str(num) + ':', c)

table = data.split('\n')
table_all = [i.rstrip(';;;').split(';') for i in table]
a, b = map(str, input().split(' '))
a = a.capitalize()
b = b.capitalize()

for j in table_all[1:-5]:
    c, d = map(str, j[0].split(' '))
    if a == c and b == d:
        print('Ученик:', j[0])
        print('Балл по географии:', j[2], '| Балл по информатики:', j[3])
        print('Средний балл', float(((int(j[2]) + int(j[3])) / 2)))
        print('Школа №' + str(j[1]))

table = data.split('\n')
table_all = [i.rstrip(';;;').split(';') for i in table]
a, b = map(str, input().split(' '))
a = a.capitalize()
b = b.capitalize()

for j in table_all[1:-5]:
    c, d = map(str, j[0].split(' '))
    if a == c and b == d:
        print('Ученик:', j[0])
        print('Балл по географии:', j[2], '| Балл по информатики:', j[3])
        print('Средний балл', float(((int(j[2]) + int(j[3])) / 2)))
        print('Школа №' + str(j[1]))

t = a.split("\n")
n = 0
table = [i. rstrip(";;;").split(";") for i in t]
y = input()
r = y.lower()
for h in table:
    if h[0].lower() == r:
        print( 'Ученик: ' + h[0] )
        print( 'Балл по географии: ' + h[2] + ' | Балл по информатики: ' + h[3] )
        n = float( (int( h[2] ) + int( h[3] )) / 2 )
        print( 'Средний балл ' + str( n ) )
        print( 'Школа №' + h[1] )
    else:
        b = str(h[0].lower()).split()
        if (r == b[0][:len(r)]) or (r == b[1][:len(r)]):
            print('Ученик: ' + h[0])
            print('Балл по географии: ' + h[2] + ' | Балл по информатики: ' + h[3])
            n = float((int(h[2]) + int(h[3])) / 2)
            print('Средний балл ' + str(n))
            print('Школа №' + h[1])