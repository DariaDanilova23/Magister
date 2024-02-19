import multiprocessing
import time
import sys

# Определение функции daemon
def daemon():
    p = multiprocessing.current_process() # Получение информации о текущем процессе
    print ('Starting:', p.name, p.pid)  # Вывод информации о запуске, имени и идентификаторе процесса

    # принудительно выполняет сброс буфера стандартного вывода
    # Это означает, что все данные, которые были буферизированы 
    # для вывода в стандартный поток вывода, будут немедленно записаны в устройство вывода.
    sys.stdout.flush() 

    time.sleep(2) # Приостановка выполнения на 2 секунды
    print ('Exiting :', p.name, p.pid) # Вывод информации о завершении, имени и идентификаторе процесса
    sys.stdout.flush()

# Определение функции non_daemon
def non_daemon():
    p = multiprocessing.current_process() # Получение информации о текущем процессе
    print ('Starting:', p.name, p.pid)  # Вывод информации о запуске, имени и идентификаторе процесса
    sys.stdout.flush() # принудительно выполняет сброс буфера стандартного вывода
    print ('Exiting :', p.name, p.pid) # Вывод информации о завершении, имени и идентификаторе процесса
    sys.stdout.flush() # принудительно выполняет сброс буфера стандартного вывода

if __name__ == '__main__':
    # Создание процесса-демона с явным именем и указанием, что он является демоническим 'daemon'
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    # Создание недемонического процесса с явным именем 'non-daemon'
    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()  # Запуск демонического процесса
    time.sleep(1) # Приостановка выполнения на 1 секунду
    n.start()  # Запуск недемонического процесса


# Результат выполнения
#----------------------
# Starting: daemon 19029
# Starting: non-daemon 19030
# Exiting : non-daemon 19030
