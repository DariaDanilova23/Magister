import multiprocessing
import logging
import sys

def worker():
    print ('Doing some work') #Вывод сообщения 'Doing some work'
    sys.stdout.flush() # Принудительный сброс буфера стандартного потока вывода

if __name__ == '__main__':
    # Настройка вывода журнала для процесса без указания уровня, по умолчанию будет WARNING
    multiprocessing.log_to_stderr()

    # Получение объекта логгера для текущего процесса
    logger = multiprocessing.get_logger()

     # Установка уровня логгера на INFO, что позволяет выводить информационные сообщения
    logger.setLevel(logging.INFO)

    p = multiprocessing.Process(target=worker) # Создание процесса p, вызывающего ф-ию worker
    p.start() # Запуск процесса p
    p.join() # Ожидание завершения процесса p


# Результат выполнения 
#----------------------
# [INFO/Process-1] child process calling self.run()
# Doing some work
# [INFO/Process-1] process shutting down
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down