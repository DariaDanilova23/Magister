import  multiprocessing # Импорт модуля multiprocessing

# Определяем функцию, которая будет выполняться каждым процессом
def pipe_func(ch, N_iter):
    a = 0 #Инициализируем переменную  a
    for i in range(N_iter): # Цикл выполняемый N_iter раз, N_iter равен номеру процесса
        a += 1 # Увеличиваем значение переменной а
        ch.send(a) # Отправляем значение переменной а по трубе

     # Посылаем сигнал 'STOP' для завершения цикла в основном процессе
    ch.send('STOP')

if __name__ == '__main__':
    parent, child = multiprocessing.Pipe() # Создаем двусторонний канал (трубу) между родительским и дочерним процессами
    
    # Цикл в котором создаются и запускаются 4 процесса
    for iter in range(4):
        # Создаем новый процесс, каждый из которых вызывает функцию pipe_func 
        # с параметрами (один конец канала-трубы, номер процесса)
        p = multiprocessing.Process(target=pipe_func,args=(child, iter)) 
        p.start() # Запускаем процесс

        result = None # Инициализируем переменную result
        while result != 'STOP': #Цикл пока result не равен 'STOP'
            result = parent.recv()  #Присваиваем result данных переданных потрубе из функции pipe_func
            print(iter,result) # Вывод полученных данных на экран
        

# Результат выполнения
#----------------------
# 0 STOP
# 1 1
# 1 STOP
# 2 1
# 2 2
# 2 STOP
# 3 1
# 3 2
# 3 3
# 3 STOP