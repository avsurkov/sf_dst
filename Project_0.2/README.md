# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Результат)    
[6. Выводы](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток (не больше 20 попыток)

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python

:arrow_up:[к оглавлению](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Оглавление)

### Краткая информация о данных
....
  
:arrow_up:[к оглавлению](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Оглавление)


### Этапы работы над проектом  

**Загадываем число**

При помощи функции "random" из библиотеки NumPy генерируем случайные числа от 1 до 100.

**Объявляем функцию "random_predict()", которая на вход будет принимать загаданное число "number".**

При помощи цикла "While" перебираем рандомные предполагаемые числа.

**Объявляем функцию "score_game()", определяющую среднее количество попыток угадывания числа**

Аргументом функции будет "random_predict()"

**Корректируем функцию "random_predict()"**

Так как среднее колличество попыток за которое программа угадывает число превышало необходимый показатель, было необходимо скорректировать работу функции "random_predict()":
- был добавлен механизм корректировки предполагаемого числа;
- был добавлен список, в котором программа собирала неподошедшие предполагаемые числа, для того, чтобы исключить их повторение.

:arrow_up:[к оглавлению](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Оглавление)


### Результаты:  
В результате программа подбирает угадываемое число в среднем за 20 попыток.

:arrow_up:[к оглавлению](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Оглавление)


### Выводы:  
....

:arrow_up:[к оглавлению](https://github.com/avsurkov/sf_dst/blob/main/Project_0.2/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами