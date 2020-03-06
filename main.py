import numpy as np

high_border = 100                                  # Можно через int(input())                      
low_border = 1
number = np.random.randint(low_border,high_border) # Компьютер загадывает номер от 1 до 100
count = 0                                          # Счётчик попыток     

while number != predict:                           # Цикл который повторяется пока программа не угадает номер 
    predict = int ((high_border + low_border)/2)   # Предположительное число равно половине интервала
    count+=1
    if number > predict:                           # При неверном предположении границы возможных чисел сужаются
        low_border = predict
    elif number < predict:
        high_border = predict
    else:
        break
print("Компьютер угадал число", number, "за", count, "попыток")