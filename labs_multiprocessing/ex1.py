import multiprocessing # Импорт модуля multiprocessing

# Определяем функцию, которая будет выполняться каждым процессом
def worker():

    """worker function"""

    print ('Worker') #Вывод сообщения "Worker"

    return


if __name__ == '__main__':
    # Выводим количество доступных процессорных ядер
    print('Threads available: ',multiprocessing.cpu_count())

    # Инициализируем пустой список jobs для хранения объектов процессов
    jobs = []

    # Цикл в котором запускаются 5 процессов
    for i in range(5):

        p = multiprocessing.Process(target=worker) # Создае нового процесса, вызывающего функцию worker

        jobs.append(p) # Добавляем созданный процесс в список jobs

        p.start() # Запускаем процесс
    
        p.join() # Ждем завершения процесса перед переходом к следующему
    print (jobs)# Выводим список созданных процессов


# Результат выполнения
#----------------------
# Threads available:  5
# Worker
# Worker
# Worker
# Worker
# Worker
# [<Process name='Process-1' pid=4399 parent=4398 stopped exitcode=0>, 
# <Process name='Process-2' pid=4400 parent=4398 stopped exitcode=0>, 
# <Process name='Process-3' pid=4401 parent=4398 stopped exitcode=0>, 
# <Process name='Process-4' pid=4402 parent=4398 stopped exitcode=0>, 
# <Process name='Process-5' pid=4403 parent=4398 stopped exitcode=0>]
