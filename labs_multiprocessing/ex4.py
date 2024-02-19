import multiprocessing # Импорт модуля multiprocessing
import time # Импорт модуля time

# Определение функции worker
def worker():
    name = multiprocessing.current_process().name # Получение имени текущего процесса
    print (name, 'Starting', time.time()) # Вывод информации о запуске и времени
    time.sleep(2)  # Приостановка выполнения на 2 секунды
    print (name, 'Exiting', time.time())  # Вывод информации о завершении и времени

def my_service():
    name = multiprocessing.current_process().name # Получение имени текущего процесса
    print (name, 'Starting', time.time()) # Вывод информации о запуске и времени
    time.sleep(3)  # Приостановка выполнения на 3 секунды
    print (name, 'Exiting', time.time()) # Вывод информации о завершении и времени

if __name__ == '__main__':
    # Создание процесса с именами 'my_service' вызывающего ф-ию my_service
    service = multiprocessing.Process(name='my_service', target=my_service)
    # Создание процесса с именами 'worker 1' вызывающего ф-ию worker
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    # Создание процесса с автоматически сгенерированным именем и вызывающего ф-ию worker
    worker_2 = multiprocessing.Process(target=worker) # use default name

    # Запуск процессов
    worker_1.start()
    worker_2.start()
    service.start()


# Результат выполнения
#----------------------
# worker 1 Starting 1708197487.7906108
# Process-3 Starting 1708197487.793788
# my_service Starting 1708197487.795338
# worker 1 Exiting 1708197489.8076253
# Process-3 Exiting 1708197489.8078525
# my_service Exiting 1708197490.7975037