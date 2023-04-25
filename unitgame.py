import numpy as np

number = np.random.randint(1,101)
predict_number = np.random.randint(1, 101) # предполагаемое число
count = 0

while True:
    count += 1
    print('count NEW - ', count)
    print('Predict number - ', predict_number)
    print(number)
    if number == predict_number:
        break # выход из цикла, если угадали
    elif count > 50:
        predict_number += 1
    elif predict_number > number:
        predict_number //= 3
    elif predict_number < number:
        predict_number +=3
    

print(f'Число угаданно за {count} попыток')