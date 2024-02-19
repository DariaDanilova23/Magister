import multiprocessing
import time
import sys

def daemon():
    # Вывод информации о запуске демонического процесса и времени
    print ('Starting:', multiprocessing.current_process().name, time.time())
    time.sleep(2) # Приостановка выполнения на 2 секунды

    # Вывод информации о завершении демонического процесса и времени
    print ('Exiting :', multiprocessing.current_process().name, time.time())

def non_daemon():
    # Вывод информации о запуске недемонического процесса и времени
    print ('Starting:', multiprocessing.current_process().name, time.time())

    # Вывод информации о завершении недемонического процесса и времени
    print ('Exiting :', multiprocessing.current_process().name, time.time())

if __name__ == '__main__':
    # Создание демонического процесса с явным именем 'daemon', вызывающего ф-ию daemon 
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    # Создание недемонического процесса с явным именем 'non-daemon', вызывающего ф-ию non_daemon
    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start() # Запуск демонического процесса
    time.sleep(1) # Приостановка выполнения главного процесса на 1 секунду
    n.start() # Запуск недемонического процесса

    # Ожидание завершения демонического и недемонического процессов
    d.join()
    n.join()
    
    print ('End main ', time.time()) # Вывод информации о завершении главного процесса и времени

# Результат выполнения
#----------------------
# tarting: daemon 1708203153.768431
# Starting: non-daemon 1708203154.7719839
# Exiting : non-daemon 1708203154.7720995
# Exiting : daemon 1708203155.7749152
# End main  1708203155.777911
