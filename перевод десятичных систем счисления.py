n = int(input('Введите число: '))
m = int(input('В какую систему счисления будем переводить?: '))

s = ''
vol=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]


while n != 0:
    ch = n % m
    s = str(vol[ch]) + s
    n //= m
print(s)