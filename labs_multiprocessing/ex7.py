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
    n.start() # Запуск недемонического процесса

    d.join(1) # Ожидание завершения демонического процесса в течение 1 секунды

    print ('d.is_alive()', d.is_alive(), time.time()) # вывод информации о состоянии процесса
    # метод is_alive() объекта процесса p, который возвращает True, 
    # если процесс жив, и False, если он завершен.
    
    n.join() # Ожидание завершения недемонического процесса
    print ('End main ', time.time()) # Вывод информации о завершении главного процесса и времени


# Результат выполнения
#----------------------
# Starting: daemon 1708203169.8705626
# Starting: non-daemon 1708203169.8713648
# Exiting : non-daemon 1708203169.871433
# d.is_alive() True 1708203170.8869717
# End main  1708203170.887095