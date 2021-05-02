perct: int = int(input('Введите количество процентов от 0 до 20:   '))

a = [1]
b = [2, 3, 4]
c = [i for i in range(5, 20+1)]
d = [0]

if perct in a:
    print(perct, 'Процент')
elif perct in b:
    print(perct, 'Процента')
elif perct in c:
    print(perct, 'Процентов')
elif perct in d:
     print(perct, 'Процентов')
