import numpy as np

number = np.random.randint(1,100)
count = 0
predict = 50
high_border = 100
low_border = 1
while number != predict:
    predict = int ((high_border + low_border)/2)
    count+=1
    if number > predict: 
        low_border = predict
    elif number < predict:
        high_border = predict
    else:
        break
print("Компьютер угадал число", number, "за", count, "попыток")