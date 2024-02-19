from multiprocessing import Pool # Импорт модуля multiprocessing
from math import sin, cos # Импорт необходимых математических функций
from time import time # Импорт функции time для измерения времени выполнения

# Определение функции some_slow_calc
def some_slow_calc(x):
    #Цикл выполняющийся 100
    for i in range(100):
       y = sin(cos(sin(cos(x+i)))) #Вычисление y
    return y

if __name__ == '__main__':
    t_start = time() # Начало отсчета времени
    #Цикл выполняющийся 100000 раз последовательно
    for x in range(100000):
        z = some_slow_calc(x)
    t_end = time() # Окончание отсчета времени
    # Вывод времени выполнения последовательных вычислений
    print('time of non parallel version', t_end - t_start)
    
    # Проведение тестирования параллельных вычислений для разного числа процессов
    for n in [1, 2, 3, 4]:
        t_start = time() # Начало отсчета времени
        # Создание пула процессов с числом процессов, равным n-каждое число из массива
        p = Pool(processes=n)
        # Запуск параллельных вычислений выполняющийся 100000 раз с использованием map
        p.map(some_slow_calc, [x for x in range(1000000)])
        t_end = time() # Окончание отсчета времени

        # Вывод времени выполнения параллельных вычислений
        print('time of parallel calc on', n, 'proc', t_end - t_start)


# Результат выполнения
#----------------------
# time of non parallel version 6.805924415588379
# time of parallel calc on 1 proc 66.46336340904236
# time of parallel calc on 2 proc 32.89520287513733
# time of parallel calc on 3 proc 25.91966700553894
# time of parallel calc on 4 proc 23.194501399993896