import multiprocessing

# Определение функции worker, которая будет выполняться каждым процессом
def worker(num):
    """thread worker function"""
    print ('Worker:', num) # Вывод сообщения "Worker:" и номера процесса
    return

if __name__ == '__main__':
    jobs = []  # Инициализация списка jobs для хранения объектов процессов
    # Цикл в котором запускаются 5 процессов
    for i in range(5):
        # Создание нового процесса, вызывающего функцию worker с аргументом номера процесса
        p = multiprocessing.Process(target=worker, args=(i,)) 
        jobs.append(p) # Добавление созданного процесса в список jobs
        p.start()  # Запуск созданного процесса


# Результат выполнения
#----------------------
# Worker: 0
# Worker: 1
# Worker: 2
# Worker: 3
# Worker: 4