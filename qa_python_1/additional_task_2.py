print('Введите число, для которого нужно рассчитать цифровой корень:')
num = int(input())

while True:
    if num <=0:
        print('Введено недопустимое число. Расчет корня будет неверен.')
        break
    elif num > 10**7:
        print('Введено недопустимое число. Расчет корня будет неверен.')
        break
    
def digital_root(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

print('Цифровой корень равен:', digital_root(num))